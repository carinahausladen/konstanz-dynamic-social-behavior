"""Konstanz heatwave simulation — apparatus.

The companion notebook ``6_konstanz.ipynb`` imports from this module and
provides commentary, visualization, and interpretation. Everything that
*defines* the simulation lives here; everything that *narrates* or
*analyses* it lives in the notebook.

Sections (in order of dependence):

1.  LLM helpers + cache + cost tracker
2.  World data: districts, temperature schedule, cooling centres
3.  Personas + social network                   (Horton 2023)
4.  Information environment: channels + posts   (Larooij & Tornberg 2025)
5.  Cognitive scaffold: memory + retrieval      (Park 2023 §4.1-4.2)
6.  Reflection                                  (Park 2023 §4.3)
7.  Decision loop with selective deliberation   (Akata 2025 + WhatIf 2026)
8.  Simulation engine + outcome model
"""

from __future__ import annotations

import hashlib
import json
import math
import os
import random
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import numpy as np
import pandas as pd



# ============================================================
# 1. LLM helpers + cache + cost tracker
# ============================================================

CACHE_DIR = Path(__file__).parent / "6_konstanz_cache"
CACHE_DIR.mkdir(exist_ok=True)
CACHE_FILE = CACHE_DIR / "llm_cache.json"

if CACHE_FILE.exists():
    with open(CACHE_FILE) as _f:
        _cache = json.load(_f)
else:
    _cache = {}

_env_file = Path(__file__).parent.parent.parent / ".env"
if _env_file.exists():
    for _line in _env_file.read_text().splitlines():
        _line = _line.strip()
        if _line and not _line.startswith("#") and "=" in _line:
            _k, _v = _line.split("=", 1)
            os.environ.setdefault(_k.strip(), _v.strip().strip('"').strip("'"))

_api_key = os.environ.get("OPENAI_API_KEY")
if _api_key:
    import openai
    client = openai.OpenAI(api_key=_api_key)
else:
    client = None

PRICING_PER_TOKEN = {
    "gpt-4o-mini":            {"in": 0.15 / 1e6, "out": 0.60 / 1e6},
    "text-embedding-3-small": {"in": 0.02 / 1e6, "out": 0.0},
}
_usage = {"tokens": {}, "calls": {"chat_live": 0, "chat_cached": 0,
                                   "embed_live": 0, "embed_cached": 0}}


def _bump(model, kind, n):
    _usage["tokens"][(model, kind)] = _usage["tokens"].get((model, kind), 0) + n


def _cache_key(kind, model, payload):
    h = hashlib.sha256(json.dumps([kind, model, payload], sort_keys=True).encode()).hexdigest()[:16]
    return f"{kind}:{model}:{h}"


def _save_cache():
    with open(CACHE_FILE, "w") as f:
        json.dump(_cache, f, indent=2)


def llm(prompt, model="gpt-4o-mini", temperature=0.7, max_tokens=400):
    """Single-prompt completion, cached by (model, prompt, temperature)."""
    key = _cache_key("chat", model, {"prompt": prompt, "temperature": temperature})
    if key in _cache:
        _usage["calls"]["chat_cached"] += 1
        return _cache[key]
    if client is None:
        raise RuntimeError(f"Prompt not in cache and no API key set:\n{prompt[:200]}...")
    r = client.chat.completions.create(
        model=model, temperature=temperature, max_tokens=max_tokens,
        messages=[{"role": "user", "content": prompt}],
    )
    out = r.choices[0].message.content.strip()
    _bump(model, "in", r.usage.prompt_tokens)
    _bump(model, "out", r.usage.completion_tokens)
    _usage["calls"]["chat_live"] += 1
    _cache[key] = out
    _save_cache()
    return out


def embed(text, model="text-embedding-3-small"):
    """Embed one string, cached by (model, text)."""
    key = _cache_key("embed", model, {"text": text})
    if key in _cache:
        _usage["calls"]["embed_cached"] += 1
        return np.array(_cache[key])
    if client is None:
        raise RuntimeError(f"Embedding not in cache and no API key set: {text[:80]}")
    r = client.embeddings.create(model=model, input=text)
    vec = r.data[0].embedding
    _bump(model, "in", r.usage.prompt_tokens)
    _usage["calls"]["embed_live"] += 1
    _cache[key] = vec
    _save_cache()
    return np.array(vec)


def print_cost_summary():
    print(f'API calls: {_usage["calls"]["chat_live"]} live chat + {_usage["calls"]["chat_cached"]} cached chat; '
          f'{_usage["calls"]["embed_live"]} live embed + {_usage["calls"]["embed_cached"]} cached embed')
    print()
    total_cost = 0.0
    if not _usage["tokens"]:
        print("No live API calls made. Cost: $0.00 (entire notebook served from cache).")
        return
    print(f'{"model":<28} {"in tok":>10} {"out tok":>10} {"cost (USD)":>12}')
    print("-" * 64)
    for model in sorted({m for m, _ in _usage["tokens"]}):
        in_tok = _usage["tokens"].get((model, "in"), 0)
        out_tok = _usage["tokens"].get((model, "out"), 0)
        rate = PRICING_PER_TOKEN.get(model, {"in": 0.0, "out": 0.0})
        cost = in_tok * rate["in"] + out_tok * rate["out"]
        total_cost += cost
        print(f'{model:<28} {in_tok:>10,} {out_tok:>10,} {"$" + format(cost, ".5f"):>12}')
    print("-" * 64)
    print(f'{"total":<28} {"":>10} {"":>10} {"$" + format(total_cost, ".5f"):>12}')


# ============================================================
# 2. World: districts, temperature schedule, cooling centres
# ============================================================

DISTRICTS = pd.DataFrame([
    {"name": "Altstadt",     "pop_share": 0.18, "ac_penetration": 0.12, "tree_cover": 0.05, "lake_distance_km": 0.2},
    {"name": "Petershausen", "pop_share": 0.22, "ac_penetration": 0.30, "tree_cover": 0.18, "lake_distance_km": 0.6},
    {"name": "Paradies",     "pop_share": 0.10, "ac_penetration": 0.20, "tree_cover": 0.25, "lake_distance_km": 0.3},
    {"name": "Wollmatingen", "pop_share": 0.20, "ac_penetration": 0.45, "tree_cover": 0.30, "lake_distance_km": 1.5},
    {"name": "Egg",          "pop_share": 0.10, "ac_penetration": 0.40, "tree_cover": 0.45, "lake_distance_km": 2.0},
    {"name": "Staad",        "pop_share": 0.08, "ac_penetration": 0.25, "tree_cover": 0.20, "lake_distance_km": 0.1},
]).set_index("name")

COOLING_CENTRES = {
    "Altstadt":     {"name": "Stadtbibliothek Altstadt",  "capacity": 40, "open_hours": (10, 20)},
    "Petershausen": {"name": "Bürgerzentrum Petershausen", "capacity": 60, "open_hours": (9, 19)},
    "Paradies":     {"name": "Universität Paradies-Foyer", "capacity": 80, "open_hours": (8, 22)},
    "Wollmatingen": {"name": "Wollmatinger Gemeindesaal",  "capacity": 50, "open_hours": (10, 18)},
    "Egg":          {"name": "Kirchenzentrum Egg",         "capacity": 30, "open_hours": (10, 18)},
    "Staad":        {"name": "Staad Schwimmbad-Cafeteria", "capacity": 40, "open_hours": (9, 21)},
}

DAILY_PEAKS = [33, 35, 36, 37, 37, 35]   # °C, days 0..5
DAILY_LOWS  = [22, 23, 24, 25, 25, 22]
HUMIDITY    = [0.55, 0.60, 0.68, 0.72, 0.72, 0.60]


def district_temperature(district, day, hour):
    """Outdoor temperature in district at (day, hour)."""
    peak, low = DAILY_PEAKS[day], DAILY_LOWS[day]
    base = low + (peak - low) * max(0, math.sin(math.pi * (hour - 6) / 14))
    d = DISTRICTS.loc[district]
    cooling = 2 * d["tree_cover"] + 0.5 * math.exp(-d["lake_distance_km"])
    return round(base - cooling, 1)


def district_indoor_temperature(district, day, hour, has_ac):
    """Indoor temperature, accounting for AC and overnight non-cooling.

    Note: the AC branch caps at 24 °C, which means AC-haves accumulate zero
    heat-degree-hours in the outcome model. This is the known artefact in
    `compute_outcomes` documented in the run-interpretation file.
    """
    outdoor = district_temperature(district, day, hour)
    if has_ac:
        return min(outdoor, 24.0)
    daily_indoor_avg = (DAILY_PEAKS[day] + DAILY_LOWS[day]) / 2 + 1.0
    return round(0.4 * outdoor + 0.6 * daily_indoor_avg, 1)


# ============================================================
# 3. Personas + social network (Horton 2023 — Homo silicus)
# ============================================================

PERSONAS = [
    {"id": "frau_mueller", "name": "Frau Margarete Müller", "age": 81, "district": "Altstadt",
     "language": "de", "has_ac": False, "mobility": "limited", "trust_inst": "low",
     "paragraph": "Frau Margarete Müller is 81. She has lived in the same Altstadt attic apartment since 1968 and refuses to consider moving. Her husband died in 2014. She reads the local paper but distrusts municipal SMS warnings (\"they always exaggerate\"). She does not have air conditioning, considers it wasteful, and rarely leaves the apartment in summer. Her closest contact is Frau Bauer two floors below, but Frau Bauer is in Bavaria visiting grandchildren this week."},
    {"id": "herr_schmidt", "name": "Herr Klaus Schmidt", "age": 76, "district": "Petershausen",
     "language": "de", "has_ac": True, "mobility": "normal", "trust_inst": "low",
     "paragraph": "Herr Schmidt is a retired civil servant, 76, living alone in a Petershausen flat. He has air conditioning installed but considers it self-indulgent and rarely turns it on. He had a bad experience with social services in 2021 (a misunderstanding about a wellness check) and has refused all subsequent municipal contact. His daughter Marlene calls him every Sunday at 3 pm."},
    {"id": "anna", "name": "Anna Lindqvist", "age": 22, "district": "Paradies",
     "language": "multi", "has_ac": False, "mobility": "normal", "trust_inst": "medium",
     "paragraph": "Anna Lindqvist is a 22-year-old Erasmus student in environmental science. She lives in a Paradies shared flat. She speaks German, English, Swedish, and decent Portuguese from a year in Lisbon. She is a heavy WhatsApp user and has been gradually getting to know the elderly residents in her building, including Frau Müller two streets over for whom she sometimes shops."},
    {"id": "costa_silva", "name": "Maria Costa Silva", "age": 38, "district": "Wollmatingen",
     "language": "pt-de", "has_ac": False, "mobility": "normal", "trust_inst": "low",
     "paragraph": "Maria Costa Silva, 38, works in elderly care at a Konstanz nursing home. She lives in Wollmatingen with her husband and two children. Her primary news source is a Portuguese-language Facebook community. She speaks functional German but reads it slowly and tends to skim official municipal messages. Her family relies on lake swimming for cooling."},
    {"id": "lena_swiss", "name": "Dr. Lena Hoffmann", "age": 34, "district": "Petershausen",
     "language": "de", "has_ac": True, "mobility": "normal", "trust_inst": "high",
     "paragraph": "Lena Hoffmann is a 34-year-old physician at the cardiology clinic in Altstadt. She lives in Petershausen but lived in Kreuzlingen until 2023, so her phone receives both German DWD and Swiss MeteoSchweiz alerts. She is professionally aware of heat-mortality risks and has been considering whether to organise something for elderly patients."},
    {"id": "oma_pia", "name": "Pia Brandt", "age": 79, "district": "Altstadt",
     "language": "de", "has_ac": False, "mobility": "normal", "trust_inst": "medium",
     "paragraph": "Pia Brandt is 79, widowed, in an Altstadt apartment with a small inner courtyard. Active member of her parish; wide circle of friends she sees daily. No AC. Skeptical of \"modern\" warnings but follows what her parish friend Greta does."},
    {"id": "tomas_student", "name": "Tomáš Novák", "age": 24, "district": "Paradies",
     "language": "multi", "has_ac": False, "mobility": "normal", "trust_inst": "medium",
     "paragraph": "Tomáš is a 24-year-old Czech graduate student in physics. He lives in Anna's building. He follows Czech news primarily and is on a Telegram channel for Czech students in Germany. He spends most days in the lab and hardly notices outside conditions."},
    {"id": "tourist_smith", "name": "The Smith family", "age": "family", "district": "Staad",
     "language": "en", "has_ac": True, "mobility": "normal", "trust_inst": "na",
     "paragraph": "The Smiths — two parents (early 40s) and two children (10, 7) — are British tourists staying in a Staad hotel. They speak no German. Booked a Bodensee swimming holiday in February; unfamiliar with how hot it can get here. Receive no local warning channels."},
    {"id": "herr_wagner", "name": "Herr Wagner", "age": 84, "district": "Wollmatingen",
     "language": "de", "has_ac": False, "mobility": "limited", "trust_inst": "medium",
     "paragraph": "Herr Wagner, 84, has heart disease and lives alone in a Wollmatingen ground-floor flat. Daughter visits weekly; Caritas wellness-call subscription. No AC, one fan. Nominally on the local heat-vulnerability registry but not always reachable."},
    {"id": "family_rainer", "name": "Familie Rainer", "age": "family", "district": "Egg",
     "language": "de", "has_ac": True, "mobility": "normal", "trust_inst": "high",
     "paragraph": "The Rainer family — two parents (40s), two teenagers — comfortable Egg house with central AC and a garden. Follow DWD warnings carefully, plan around them, check on Oma Rainer (in Altstadt) by phone. Well-resourced, well-informed."},
    {"id": "bashir", "name": "Bashir Yousef", "age": 47, "district": "Altstadt",
     "language": "de-ar", "has_ac": True, "mobility": "normal", "trust_inst": "medium",
     "paragraph": "Bashir runs a small café in Altstadt. 47, has lived in Konstanz for 18 years, knows most of his Altstadt neighbours by name including Frau Müller. Commercial AC at the café. On local Arabic-speaking community WhatsApp groups; watches German news daily."},
    {"id": "caritas_admin", "name": "Greta Hofer", "age": 56, "district": "Egg",
     "language": "de", "has_ac": True, "mobility": "normal", "trust_inst": "high",
     "paragraph": "Greta Hofer, 56, manages the Caritas wellness-call program in Konstanz. Her list has ~120 elderly residents who get a daily check-in. Capacity is limited; the program covers maybe a third of the actual heat-vulnerable population."},
]

SOCIAL_NETWORK = {
    "frau_mueller":  ["anna", "bashir", "oma_pia"],
    "herr_schmidt":  ["lena_swiss"],
    "anna":          ["frau_mueller", "tomas_student"],
    "costa_silva":   [],
    "lena_swiss":    ["herr_schmidt", "caritas_admin"],
    "oma_pia":       ["frau_mueller"],
    "tomas_student": ["anna"],
    "tourist_smith": [],
    "herr_wagner":   ["caritas_admin"],
    "family_rainer": [],
    "bashir":        ["frau_mueller"],
    "caritas_admin": ["herr_wagner", "lena_swiss"],
}


# ============================================================
# 4. Information environment (Larooij & Törnberg 2025)
# ============================================================

POSTS = {
    "dwd_official": [
        (0, "de", "DWD: Hitzewarnung für die Bodenseeregion ab Sonntag. Tagestemperaturen bis 36 °C, nachts kaum unter 23 °C.", 7),
        (1, "de", "DWD: Amtliche Hitzewarnung dauert an. Vermeiden Sie körperliche Anstrengung in der Mittagshitze.", 7),
        (2, "de", "Stadt Konstanz: Kühlräume in der Stadtbibliothek und im Bürgerzentrum geöffnet bis 20:00.", 6),
        (3, "de", "DWD: Hitzewarnstufe 2. Besondere Gefahr für ältere Menschen und Kleinkinder.", 8),
        (4, "de", "Klinikum Konstanz: deutlich erhöhte Notaufnahme-Belastung. Bitte unnötige Wege vermeiden.", 8),
        (5, "de", "DWD: Hitzephase nähert sich Ende, Kaltfront ab Freitagabend.", 5),
    ],
    "whatsapp_local": [
        (0, "de", "🌡️ Hitzewelle ab morgen. Wer braucht Hilfe beim Einkaufen?", 5),
        (1, "de", "Im Café von Bashir war es heute angenehm kühl, falls jemand raus muss.", 4),
        (2, "de", "Hat jemand Frau Müller heute gesehen? Ihre Vorhänge sind seit Sonntag zu.", 7),
        (3, "de", "Die Stadtbibliothek war heute überfüllt. Vielleicht morgen Bürgerzentrum probieren.", 5),
        (4, "de", "Ich glaube wir sollten in unserem Haus eine kleine Liste machen wer wen anruft.", 6),
        (5, "de", "Endlich Abkühlung in Sicht. War aber wirklich extrem die letzten Tage.", 4),
    ],
    "pt_facebook": [
        (0, "pt", "Vai fazer muito calor esta semana. Bebam muita água!", 4),
        (2, "pt", "Onde fica o lago menos cheio? Os filhos querem nadar.", 3),
        (4, "pt", "Alguém sabe se posso levar criança ao posto médico só por causa do calor?", 6),
    ],
}

SUBSCRIPTIONS = {
    "frau_mueller":  ["dwd_official"],
    "herr_schmidt":  ["dwd_official"],
    "anna":          ["dwd_official", "whatsapp_local"],
    "costa_silva":   ["pt_facebook"],
    "lena_swiss":    ["dwd_official", "whatsapp_local"],
    "oma_pia":       ["whatsapp_local"],
    "tomas_student": ["whatsapp_local"],
    "tourist_smith": [],
    "herr_wagner":   ["dwd_official"],
    "family_rainer": ["dwd_official"],
    "bashir":        ["dwd_official", "whatsapp_local"],
    "caritas_admin": ["dwd_official", "whatsapp_local"],
}


def todays_news(persona_id, day):
    """Return list of (channel, language, content) the persona sees on day."""
    items = []
    for ch in SUBSCRIPTIONS.get(persona_id, []):
        for d, lang, content, _imp in POSTS.get(ch, []):
            if d == day:
                items.append((ch, lang, content))
    return items


# ============================================================
# 5. Cognitive scaffold (Park 2023 §4.1-4.2)
# ============================================================

@dataclass
class Memory:
    content: str
    created_at: float        # game-hours since simulation start
    last_accessed: float
    importance: float        # 1-10
    embedding: Optional[np.ndarray] = None

    def __repr__(self):
        return f'Memory(t={self.created_at:.1f}h, imp={self.importance:.0f}, "{self.content[:60]}...")'


class MemoryStream:
    def __init__(self, agent_name):
        self.agent_name = agent_name
        self.memories: list[Memory] = []

    def add(self, content, created_at, importance, with_embedding=True):
        m = Memory(
            content=content,
            created_at=created_at,
            last_accessed=created_at,
            importance=importance,
            embedding=embed(content) if with_embedding else None,
        )
        self.memories.append(m)
        return m

    def __len__(self):
        return len(self.memories)


IMPORTANCE_PROMPT = '''On a scale of 1 to 10, where 1 is purely mundane (e.g., brushing teeth, making bed) and 10 is extremely poignant (e.g., a break up, college acceptance), rate the likely poignancy of the following piece of memory.

Memory: {memory}

Respond with a single integer between 1 and 10, then a brief one-sentence reason. Format: "<integer>. <reason>"'''


def rate_importance(memory_content):
    raw = llm(IMPORTANCE_PROMPT.format(memory=memory_content), temperature=0)
    try:
        score_str, reason = raw.split(".", 1)
        return int(score_str.strip()), reason.strip()
    except Exception:
        import re
        m = re.search(r"\d+", raw)
        return int(m.group()) if m else 5, raw


def cosine(a, b):
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))


def normalize(values):
    arr = np.array(values, dtype=float)
    span = arr.max() - arr.min()
    if span < 1e-9:
        return np.zeros_like(arr)
    return (arr - arr.min()) / span


def retrieve(stream, query, now_hours, k=5,
             alpha_recency=1.0, alpha_importance=1.0, alpha_relevance=1.0):
    """Return top-k Memory objects by composite score. Park 2023 retrieval rule."""
    if not stream.memories:
        return []
    q_emb = embed(query)
    rec  = [0.995 ** max(now_hours - m.last_accessed, 0) for m in stream.memories]
    imp  = [m.importance / 10.0 for m in stream.memories]
    rel  = [cosine(m.embedding, q_emb) if m.embedding is not None else 0.0
            for m in stream.memories]
    scores = (alpha_recency * normalize(rec)
              + alpha_importance * normalize(imp)
              + alpha_relevance * normalize(rel))
    order = np.argsort(-scores)[:k]
    return [stream.memories[i] for i in order]


# ============================================================
# 6. Reflection (Park 2023 §4.3)
# ============================================================

IMPORTANCE_TRIGGER = 25   # paper uses 150 over a much longer horizon

SALIENT_QUESTIONS_PROMPT = '''Below are statements about {agent_name}'s recent observations and identity:

{memories}

Given only this information, what are the 2 most salient high-level questions about {agent_name}'s current situation? Format as a numbered list, one question per line.'''


INSIGHTS_PROMPT = '''Statements about {agent_name}, each prefixed with a number:

{numbered_memories}

What 3 high-level insights help answer this question:

   "{question}"

For each insight, cite supporting statement numbers (e.g., "[1, 4]"). Format:
  <insight> [<citations>]

One insight per line. No preamble.'''


def importance_sum_of_recent(stream, n=15):
    return sum(m.importance for m in stream.memories[-n:])


def maybe_reflect(stream, now_hours, n_recent=15, max_questions=2):
    """If recent importance sum crosses threshold, run a round of reflection.

    Generates 2 salient questions, retrieves memories for each, asks the LLM
    for insights, writes the insights back to the stream as new memories.
    Returns the list of new insight strings written.
    """
    if importance_sum_of_recent(stream, n_recent) < IMPORTANCE_TRIGGER:
        return []

    recent = stream.memories[-n_recent:]
    memories_block = "\n".join(f"- {m.content}" for m in recent)
    qs_raw = llm(SALIENT_QUESTIONS_PROMPT.format(
        agent_name=stream.agent_name, memories=memories_block,
    ), temperature=0.5)
    questions = []
    for line in qs_raw.split("\n"):
        line = line.strip().lstrip("0123456789.)- ").strip()
        if line:
            questions.append(line)
    questions = questions[:max_questions]

    new_insights = []
    for q in questions:
        top = retrieve(stream, q, now_hours=now_hours, k=8)
        numbered = "\n".join(f"{i+1}. {m.content}" for i, m in enumerate(top))
        raw = llm(INSIGHTS_PROMPT.format(
            agent_name=stream.agent_name, numbered_memories=numbered, question=q,
        ), temperature=0.5)
        for line in raw.split("\n"):
            line = line.strip().lstrip("0123456789.)- ").strip()
            if len(line) < 10:
                continue
            score, _ = rate_importance(line)
            stream.add(line, created_at=now_hours, importance=score)
            new_insights.append(line)
    return new_insights


# ============================================================
# 7. Decision loop (Akata 2025 + WhatIf 2026 selective deliberation)
# ============================================================

DAILY_DECISION_PROMPT = '''You are role-playing as {persona_name}.

Background:
{persona_paragraph}

Today is Day {day} of an extreme heatwave in Konstanz.
- Outdoor temperature peak today: {peak_temp:.1f}°C
- Indoor temperature in your home (no AC = warm): {indoor_temp:.1f}°C
- Last night did not cool below {night_low}°C.

Today's news in your information channels:
{news_block}

Your recent salient memories:
{memories_block}

Your acquaintances (people you might call or visit): {acquaintances}

Choose ONE primary action for today:
A. Stay home, normal routine.
B. Stay home but take precautions (close blinds, drink more water, avoid going out).
C. Visit the cooling centre at {cooling_centre_name}.
D. Check on a specific acquaintance: <name>.
E. Other (describe briefly).

Respond with the letter, then ONE short sentence in {persona_name}'s voice explaining the choice. Format: "<letter>. <one-sentence rationale>". If D, name the acquaintance.'''


def _apply_framing(content, framing):
    """Toggle the warning wording. The Lorè-Heydari ablation in §9 of the
    notebook uses this to vary only the wrapper around identical payoffs."""
    if framing == "extremhitzewarnung":
        return content.replace("Hitzewarnung", "Extremhitzewarnung").replace("Hitzewarnstufe", "Extremhitzewarnstufe")
    if framing == "lebensgefahr":
        return content.replace("Hitzewarnung", "LEBENSGEFAHR durch Hitze").replace("Hitzewarnstufe", "Lebensgefahrstufe")
    return content


def decide_day(agent_state, day, framing="hitzewarnung"):
    """One-day decision for one agent. Returns dict with choice + rationale."""
    p = agent_state["persona"]
    stream = agent_state["stream"]
    district = p["district"]

    peak = max(district_temperature(district, day, h) for h in range(10, 18))
    indoor = max(district_indoor_temperature(district, day, h, p["has_ac"]) for h in range(10, 18))
    night_low = min(district_temperature(district, day, h) for h in range(0, 6))

    raw_news = todays_news(p["id"], day)
    if framing != "hitzewarnung":
        raw_news = [(ch, lang, _apply_framing(content, framing) if ch == "dwd_official" else content)
                    for ch, lang, content in raw_news]
    news_block = "\n".join(f"  [{ch}] {content}" for ch, lang, content in raw_news) or "  (no news in your channels today)"

    query = f"It is hot today. What should I do? Day {day} of the heatwave."
    top = retrieve(stream, query, now_hours=day * 24 + 12, k=5)
    memories_block = "\n".join(f"  - {m.content}" for m in top) or "  (no relevant memories yet)"

    acquaintances = ", ".join(SOCIAL_NETWORK.get(p["id"], [])) or "(none nearby)"

    prompt = DAILY_DECISION_PROMPT.format(
        persona_name=p["name"], persona_paragraph=p["paragraph"],
        day=day, peak_temp=peak, indoor_temp=indoor, night_low=night_low,
        news_block=news_block, memories_block=memories_block,
        acquaintances=acquaintances,
        cooling_centre_name=COOLING_CENTRES[district]["name"],
    )
    raw = llm(prompt, temperature=0.7, max_tokens=120)

    choice = raw.strip()[:1].upper() if raw.strip() else "?"
    rationale = raw.strip()
    return {"persona_id": p["id"], "day": day, "choice": choice, "raw": rationale,
            "peak_temp": peak, "indoor_temp": indoor}


# ============================================================
# 8. Simulation engine + outcome model
# ============================================================

def initialise_agents(persona_subset=None, with_seeded_grim_trigger=True):
    """Build a fresh world of agents with seeded backstories.

    `with_seeded_grim_trigger` adds Akata-style importance-9 memory of a
    bad municipal interaction to Herr Schmidt. Toggle off to ablate.
    """
    persona_subset = persona_subset or [p["id"] for p in PERSONAS]
    agents = {}
    for pid in persona_subset:
        p = next(p for p in PERSONAS if p["id"] == pid)
        s = MemoryStream(p["name"])
        chunks = [c.strip() for c in p["paragraph"].split(". ") if c.strip()]
        for chunk in chunks[:4]:
            score, _ = rate_importance(chunk)
            s.add(chunk, created_at=0.0, importance=score)
        if with_seeded_grim_trigger and pid == "herr_schmidt":
            s.add(
                "In 2021 a social-services wellness-check led to a humiliating misunderstanding that I have never forgotten; I refuse all subsequent municipal contact.",
                created_at=0.0, importance=9,
            )
        agents[pid] = {"persona": p, "stream": s, "decisions": []}
    return agents


def run_simulation(persona_subset=None, framing="hitzewarnung", verbose=False):
    """Run the full 6-day Konstanz simulation. Returns (decisions_df, agents)."""
    agents = initialise_agents(persona_subset)

    for day in range(6):
        if verbose:
            print(f"--- Day {day} ---")

        for pid, a in agents.items():
            p = a["persona"]
            indoor = max(district_indoor_temperature(p["district"], day, h, p["has_ac"]) for h in range(10, 18))
            obs = f'Day {day}: indoor peak {indoor:.1f}°C in {p["district"]}.'
            score, _ = rate_importance(obs)
            a["stream"].add(obs, created_at=day * 24 + 14, importance=score)

            for ch, lang, content in todays_news(pid, day):
                if framing != "hitzewarnung" and ch == "dwd_official":
                    content = _apply_framing(content, framing)
                obs2 = f"Day {day} on {ch}: {content}"
                score2, _ = rate_importance(obs2)
                a["stream"].add(obs2, created_at=day * 24 + 9, importance=score2)

        for pid, a in agents.items():
            maybe_reflect(a["stream"], now_hours=day * 24 + 19)

        for pid, a in agents.items():
            d = decide_day(a, day=day, framing=framing)
            a["decisions"].append(d)
            if verbose:
                print(f'  {a["persona"]["name"]:30} → {d["choice"]}')

    rows = []
    for pid, a in agents.items():
        for d in a["decisions"]:
            rows.append({**d, "district": a["persona"]["district"],
                         "has_ac": a["persona"]["has_ac"],
                         "age": a["persona"]["age"]})
    return pd.DataFrame(rows), agents


def compute_outcomes(decisions_df, agents):
    """Compute per-agent heat-risk score from exposure × decisions × checks × age.

    Outcome model is deterministic and uncalibrated — for studying mechanisms,
    not forecasting. Known artefact: AC-haves get exposure_dh = 0 because
    `district_indoor_temperature` caps at 24 °C, which never crosses the 26 °C
    threshold below. See run-interpretation file for the fix.
    """
    rows = []
    for pid, a in agents.items():
        p = a["persona"]
        decisions = [d["choice"] for d in a["decisions"]]

        exposure = sum(
            max(0, district_indoor_temperature(p["district"], day, h, p["has_ac"]) - 26)
            for day in range(6) for h in range(24)
        )

        decision_modifier = 1.0
        for c in decisions:
            if c == "B":
                decision_modifier *= 0.90
            elif c == "C":
                decision_modifier *= 0.75
            elif c == "D":
                decision_modifier *= 0.95

        received_checks = sum(
            1 for other_pid, other in agents.items()
            for d in other["decisions"]
            if d["choice"] == "D" and pid in SOCIAL_NETWORK.get(other_pid, [])
        )
        check_modifier = 0.85 ** received_checks

        age = p["age"]
        if isinstance(age, int):
            age_modifier = 1 + max(0, (age - 65) / 30) ** 1.5
        else:
            age_modifier = 1.0

        risk = exposure * decision_modifier * check_modifier * age_modifier / 100.0
        rows.append({
            "persona_id": pid, "name": p["name"], "district": p["district"],
            "age": age, "has_ac": p["has_ac"],
            "exposure_dh": round(exposure, 1),
            "decision_modifier": round(decision_modifier, 3),
            "check_modifier": round(check_modifier, 3),
            "age_modifier": round(age_modifier, 2),
            "risk_score": round(risk, 2),
            "received_checks": received_checks,
            "choices": "".join(decisions),
        })
    return pd.DataFrame(rows).sort_values("risk_score", ascending=False).reset_index(drop=True)


__all__ = [
    # data
    "DISTRICTS", "COOLING_CENTRES", "DAILY_PEAKS", "DAILY_LOWS", "HUMIDITY",
    "PERSONAS", "SOCIAL_NETWORK", "POSTS", "SUBSCRIPTIONS",
    "IMPORTANCE_PROMPT", "SALIENT_QUESTIONS_PROMPT", "INSIGHTS_PROMPT",
    "DAILY_DECISION_PROMPT", "IMPORTANCE_TRIGGER",
    # cache + cost
    "client", "_cache", "_usage", "PRICING_PER_TOKEN", "CACHE_DIR",
    # functions
    "llm", "embed", "print_cost_summary",
    "district_temperature", "district_indoor_temperature",
    "todays_news",
    "Memory", "MemoryStream", "rate_importance", "cosine", "normalize", "retrieve",
    "importance_sum_of_recent", "maybe_reflect",
    "decide_day", "_apply_framing",
    "initialise_agents", "run_simulation", "compute_outcomes",
]
