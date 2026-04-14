# Game-Theoretic Foundations Needed for Weeks 2–3

*Teaching prep note — what Master's students in political science (and some economics) need to already know, or be taught early, to read the Week 2 and Week 3 readings with real comprehension.*

This note works in three layers:

1. **Part I** — Paper-by-paper: which concepts each paper assumes.
2. **Part II** — Consolidated concept inventory, organized by teaching tier.
3. **Part III** — A concrete 2-lecture sequence that front-loads what unlocks the most papers.
4. **Part IV** — Political-science framings for each concept (so it sticks with a non-econ audience).
5. **Part V** — What to skip.

---

## Part I — Prerequisites paper by paper

### Week 2

#### P1. Horton, Filippas & Manning — *Homo Silicus* (NBER w31122)
Mostly *behavioral economics* prerequisites, not hard GT.
- **Homo economicus** as a modeling convention (endow agent with utility, preferences, info → deduce behavior)
- **Experimental economics** methodology: vignettes, between-subject design, fairness elicitation
- **Social preferences** in the Charness–Rabin sense: equity / efficiency / self-interest / altruism
- **Fairness norms** (Kahneman–Knetsch–Thaler 1986 price-gouging paradigm)
- **Status-quo bias** (Samuelson–Zeckhauser)
- **Prospect-theory fourfold pattern** and the more recent "complexity-heuristic" critique (Oprea 2024)
- Intuition for *minimum wage / labor-market* substitution (one experiment)

Students who have had *any* behavioral-econ exposure will be fine. Students who have only had classical rational-choice will need the social-preferences typology up front.

#### P2. Lorè & Heydari — *Strategic Behavior: Game Structure vs. Contextual Framing*
This is the most **canonical 2×2 games** paper on the list. Students must be fluent in:
- **Payoff matrices** and the standard (R, T, S, P) labels
- **Four 2×2 social dilemmas** explicitly studied:
  - **Prisoner's Dilemma** (T > R > P > S)
  - **Stag Hunt** (R > T > P > S) — assurance / coordination under risk
  - **Snowdrift / Chicken** (T > R > S > P)
  - **Harmony / Prisoner's Delight** (R > T > P > S with C individually and socially optimal — an "anti-dilemma")
- **Nash equilibrium** (pure and mixed)
- **Dominant strategy** (why defection dominates in PD)
- **Mixed strategies** (why some of these games have mixed equilibria)
- **Framing effects** in behavioral econ (Tversky–Kahneman 1981)
- Light idea of **theory of mind** (the authors invoke "context-informed ToM")

#### P3. Akata et al. — *Playing Repeated Games with LLMs* (Nature Human Behaviour)
Adds a *repeated-games* layer on top of P2's prerequisites.
- **Finitely repeated 2×2 games** and the notion that strategies become *histories → actions*
- **Backward-induction paradox** in finite PD (why theory predicts ALLD but humans cooperate) — *helpful motivation*
- Canonical repeated-PD strategies: **ALLD, ALLC, TFT, Grudger, Defect-Once-Then-Cooperate**
- **Coordination games vs. social dilemmas** — *different failure modes* (this is the paper's central contrast)
- **Battle of Sexes** as the canonical mixed-motive coordination game
- **Behavioral game theory** as a research program (Camerer 2003) — the idea that we measure human deviations from Nash play
- **Theory of Mind** (explicit: the failure mode in BoS is lack of partner-modeling)
- *Optional:* **Chain-of-Thought / reasoning prompting** (LLM method, easy to explain)

#### P4. Sun et al. — *Game Theory Meets LLMs: A Systematic Survey*
This is the paper with the **widest** prerequisite footprint. Students need a *map* of the field — but depth in any one area is not required. They need to recognize these terms:
- **Cooperative vs. non-cooperative GT**
- **Perfect vs. imperfect information**; **complete vs. incomplete information**
- **Symmetric vs. asymmetric games**; **single-turn vs. repeated**
- **Solution concepts:** Nash, minimax, **Stackelberg**, mixed-strategy Nash
- **Shapley value** (intuitively: fair credit-assignment in a cooperative game)
- **Mechanism design** (one sentence: designing rules so desired behavior is incentive-compatible)
- **Social choice theory** (Arrow-style preference aggregation)
- **Bargaining / negotiation** games (one-line idea each)
- **Auctions** (Bertrand, first-/second-price) — just as examples
- **Bayesian games** / types (briefly)
- Specific games they'll see named: **Avalon, Werewolf** (hidden-role / identity games), **Hanabi, Overcooked** (cooperative coordination), **Diplomacy** (mixed bargaining/negotiation)

Teach as a *map*, not a deep dive. Goal: student recognizes the terms when they appear.

### Week 3

#### P5. Fan et al. — *Can LLMs Serve as Rational Players?* (AAAI 2024)
Introduces a **decomposed model of rationality** (desire / belief / action). Students need:
- Formal **rational-player model**: preference 𝓟 → desire D(·), information 𝓘 → belief Ω, optimal action π*
- **Expected-utility maximization** (even if only at the intuitive level: "choose the action whose expected value is highest")
- **Bayesian belief updating** (conceptually: posterior ∝ prior × likelihood)
- **Dictator game** with explicit preference conditions: Equality, Common-Interest, Self-Interest, Altruism
- **Rock-Paper-Scissors** as the archetypal zero-sum, mixed-Nash game — and as a test of *pattern-detection* / belief refinement
- **Zero-sum vs. non-zero-sum** distinction
- **Dominant strategies** in asymmetric payoff matrices (for the ring-network game)
- **Information sets** in game theory (informal version)

This is the single *most-GT-dense* paper among the readings. Students who understand it deeply will understand most of the others.

#### P6. Binz et al. — *Centaur: A Foundation Model for Human Cognition* (Nature)
Not strictly game theory — it's **cognitive science** — but needs adjacent foundations:
- **Decision theory under uncertainty** (expected utility, choice under risk)
- **Multi-armed bandit** problem + **exploration–exploitation tradeoff** (central to Psych-101)
- **Horizon task, Iowa gambling task** — informal intuition
- **Model-free vs. model-based reinforcement learning** (briefly; mentioned in the paper's evaluation)
- **Prospect theory** (one of the cognitive models Centaur beats)
- **Cognitive modeling / computational rationality** (the idea that behavior ≈ "optimal given cognitive constraints")
- **Fine-tuning / foundation models** (LLM method, easy to explain)

Poli-sci students may find this the most foreign paper. A one-shot primer on "decision-making under uncertainty as a research paradigm" will pay off.

#### P7. Willis, Du, Leibo & Luck — *Will Systems of LLM Agents Cooperate?*
Heavy **evolutionary game theory** content. Students need:
- **Iterated Prisoner's Dilemma** (must already be solid from P3)
- **Axelrod's tournaments** (1980s): tit-for-tat, the shadow of the future, "niceness / provocability / forgiveness"
- **Beaufils tournament** and the canonical opponent strategies: **Tit-for-Tat, Grudger, Prober, Soft-Go-By-Majority, Win-Stay-Lose-Shift (Pavlov), Suspicious TFT, Random**
- **Evolutionarily Stable Strategy (ESS)** — Smith & Price 1973; the concept that aggressive strategies can be ESS under certain conditions
- **Moran process** as a finite-population evolutionary dynamic (simpler than replicator dynamics; good for teaching)
- **Reactive strategies in IPD** (Wahl & Nowak 1999): cooperate with probability p after C, probability q after D
- **Noise in IPD** (Wu & Axelrod 1995) — why a single misperception can unravel cooperation
- Brief idea of **replicator dynamics** (continuous-population counterpart — needed only to recognize the term)

This paper synthesizes ~40 years of IPD research; devoting a chunk of Week 3 to IPD tradition is worthwhile.

#### P8. MindGames Challenge (NeurIPS 2025, first two talks)
- **Social-deduction games** (Werewolf / Mafia, Avalon) — structure: hidden roles, asymmetric information, natural-language communication
- **Games of incomplete information** (Harsanyi types)
- **Theory of Mind** formalized: first-order ("what does X believe?"), higher-order ("what does X believe that Y believes?")
- **Deception** as strategic communication (cheap talk vs. signaling — very briefly)

Minimal GT prerequisites beyond what P3 and P4 already cover; the ToM layer is the new thing.

#### P9. Kozlowski & Evans — *Simulating Subjects* (Sociological Methods & Research)
**Methodological**, not game-theoretic. Needs only:
- Basic grasp of **experimental validity** concepts (internal, external, construct, ecological)
- **Measurement equivalence** / invariance
- **WEIRD-sample critique** (Henrich et al. 2010)

Can be paired as the *critical counterweight* to Horton (P1).

---

## Part II — Consolidated concept inventory, organized by teaching tier

I'm using three tiers by impact: how many of the nine readings a concept unlocks.

### Tier 1 — Non-negotiable foundations (unlock ≥5 papers)

| # | Concept | Unlocks | Min. teach time |
|---|---|---|---|
| 1 | **Strategic interaction & payoff matrices** — normal-form notation, actions, payoffs | All | 10 min |
| 2 | **Dominant strategy & Nash equilibrium** (pure) | All except P6, P9 | 15 min |
| 3 | **Prisoner's Dilemma** — structure, rational prediction, cooperation puzzle | P1, P2, P3, P4, P5, P7, P8 | 15 min |
| 4 | **Social dilemma vs. coordination distinction** — why PD and BoS fail differently | P2, P3, P4, P7 | 10 min |
| 5 | **Coordination games**: Stag Hunt, Battle of the Sexes, Harmony/Delight | P2, P3, P4 | 15 min |
| 6 | **Finitely repeated games + canonical IPD strategies** (ALLD, ALLC, TFT, Grudger) | P3, P4, P7 | 20 min |
| 7 | **Behavioral game theory vs. classical GT** — that humans deviate from Nash in systematic ways | P1, P2, P3, P5, P7, P9 | 10 min |
| 8 | **Social preferences** (Fehr–Schmidt inequity aversion; efficiency; altruism; self-interest) | P1, P4, P5 | 15 min |

### Tier 2 — Should-teach (unlock 2–4 papers each)

| # | Concept | Unlocks | Min. teach time |
|---|---|---|---|
| 9 | **Mixed strategies** — especially for RPS and BoS | P2, P4, P5 | 15 min |
| 10 | **Dictator & Ultimatum games** — canonical bargaining setups and the fairness findings | P1, P5 | 10 min |
| 11 | **Axelrod's IPD tournaments** — historical context, "niceness / provocability / forgiveness" | P3, P7 | 10 min |
| 12 | **Theory of Mind** (first- and higher-order) — informal plus a formal sketch | P2, P3, P8 | 15 min |
| 13 | **Bayesian updating / belief formation** — prior × likelihood ∝ posterior, at an intuitive level | P5, P8 | 10 min |
| 14 | **Zero-sum vs. non-zero-sum distinction** | P4, P5 | 5 min |

### Tier 3 — Briefly-introduce (paper-specific, teach on-demand)

| # | Concept | Needed for | Min. teach time |
|---|---|---|---|
| 15 | **Evolutionary GT**: ESS, Moran process, replicator dynamics, reactive IPD strategies | P7 | 25 min |
| 16 | **Shapley value, cooperative GT, mechanism design, social choice theory** — as *vocabulary* | P4 | 15 min |
| 17 | **Games of incomplete information** (Harsanyi types, hidden roles) | P4, P8 | 10 min |
| 18 | **Decision theory under uncertainty**: EU, multi-armed bandits, exploration–exploitation | P6 | 20 min |
| 19 | **Prospect theory** (fourfold pattern) + Oprea's complexity critique | P1, P6 | 10 min |

Tier 1 is the core ~110 min of pure teaching — fits Week 2's 1.5-hour block with room for examples. Tier 2 adds another ~70 min (Week 3 opening). Tier 3 is on-demand alongside the specific papers.

---

## Part III — Suggested 2-lecture sequence

### Week 2 lecture (≈90 min)

Frame: "Game theory as the *diagnostic language* for strategic LLM behavior."

1. **Open with motivation** (5 min) — Why game theory for studying LLMs? (From `game_theory.md` already.)
2. **Building blocks** (15 min) — Normal form, payoff matrix, dominant strategy, Nash equilibrium. Use a single 2×2 for all four concepts.
3. **The Prisoner's Dilemma + its variants** (20 min) — PD, Stag Hunt, Chicken, Harmony/Delight. Show the (R,T,S,P) ordering as the game-class taxonomy. This is exactly Lorè & Heydari's setup and most of Akata's.
4. **Coordination vs. cooperation** (10 min) — Battle of the Sexes, why "coordination failure" is a different beast from "defection." Preview Akata's central finding.
5. **Classroom public-goods game** (as already planned — 15 min)
6. **Behavioral findings & social preferences** (15 min) — Canonical behavioral findings (already in game_theory.md) + Fehr–Schmidt inequity aversion, Charness–Rabin preference typology. Introduces Horton's framework.
7. **Theory of Mind + preview of Week 3** (10 min)

### Week 3 lecture (≈90 min)

Frame: "From single-shot to repeated to populations — and what LLMs get wrong at each level."

1. **Finitely repeated games & the backward-induction paradox** (15 min) — Motivate why humans cooperate.
2. **Axelrod's tournaments + canonical IPD strategies** (15 min) — TFT, Grudger, ALLD, ALLC, Pavlov. Directly sets up Willis et al.
3. **Evolutionary game theory** (20 min) — ESS, Moran process. Motivate with "what happens when aggressive LLMs interact with cooperative LLMs?"
4. **Formal rational-player model** (15 min) — Desire / Belief / Action framework from Fan et al. Include light Bayesian updating. This is the scaffold for critiquing LLM "rationality."
5. **Games of incomplete information + ToM** (10 min) — Harsanyi types informally; Werewolf as the canonical social-deduction game. Sets up MindGames.
6. **Decision-making-under-uncertainty primer** (10 min) — Expected utility, multi-armed bandit, exploration–exploitation. One slide on prospect theory. Sets up Centaur and Oprea.
7. **Wrap — the methodology debate** (5 min) — Homo Silicus vs. Kozlowski–Evans. "Are LLMs valid stand-ins? The rest of the course builds on this question."

---

## Part IV — Political-science framings (for each concept)

Master's students in political science will retain concepts better if each is tied to a canonical poli-sci example. Suggested hooks:

| Concept | Political-science hook |
|---|---|
| Prisoner's Dilemma | Cold-War arms race; climate-change free-riding; tax evasion |
| Stag Hunt | Security dilemma (Jervis 1978); alliance commitment; regime-change coordination |
| Chicken / Snowdrift | Crisis bargaining; brinkmanship (Cuban Missile Crisis) |
| Battle of the Sexes | International-standard coordination (WTO rules, internet protocols) |
| Finitely repeated PD | Why congressional logrolling works despite incentive to defect |
| Axelrod's tournaments | Cooperation in anarchy (Keohane); WWI trench warfare "live and let live" |
| Social preferences / fairness | Redistribution preferences; Rawlsian justice; public-opinion research |
| Nash vs. actual behavior | Why rationalist IR theory under-predicts cooperation |
| Evolutionary GT / ESS | Norm emergence in international society; cultural evolution of institutions |
| Theory of Mind | Intelligence analysis; deterrence credibility; signaling in diplomacy |
| Mechanism design | Voting-rule design; constitutional design; procurement auctions |
| Social choice theory | Arrow's theorem; majority-cycling in legislatures; Condorcet |
| Bayesian games / types | Bargaining with private information (Fearon 1995 on war); spy games |
| Multi-armed bandits | Foreign-policy learning; policy experimentation in federalism |
| Games of incomplete information (Werewolf) | Counter-intelligence; insurgency-vs-government |

Many of these map to Fearon, Powell, Keohane, Jervis — classic IR references your students likely already know.

---

## Part V — What to skip

Given the 3-hour total budget across Weeks 2–3, do **not** teach:

- **Extensive-form games** beyond a 2-minute acknowledgment — none of the papers work in extensive form (except Diplomacy, which is mentioned but not read)
- **Subgame-perfect equilibrium, trembling-hand perfection, sequential equilibrium** — far too technical; no paper requires them formally
- **Folk theorem formal statement** — the *intuition* ("cooperation can be sustained with sufficient patience") is enough
- **Full Bayesian-game formalism** (type spaces, Bayesian Nash) — only the informal idea is needed
- **Auction theory beyond the name** — Sun et al. mention it but no paper uses it
- **Signaling games / cheap talk formalism** — relevant for MindGames but a one-slide informal gloss is enough
- **Cooperative solution concepts beyond Shapley** — no need for core, kernel, nucleolus
- **Full replicator-dynamics math** — Moran process is more than enough for Willis et al.

The goal for a Master's seminar is *vocabulary + intuition* so students can read and critique, not *proof-level mastery*.

---

## Quick mapping — concept × paper

| Concept (Tier) | P1 Horton | P2 L&H | P3 Akata | P4 Sun | P5 Fan | P6 Binz | P7 Willis | P8 MG | P9 K&E |
|---|---|---|---|---|---|---|---|---|---|
| Payoff matrices (1) | – | ● | ● | ● | ● | – | ● | ● | – |
| Nash / dominant (1) | – | ● | ● | ● | ● | – | ● | ● | – |
| Prisoner's Dilemma (1) | – | ● | ● | ● | – | – | ● | – | – |
| Coord. games (1) | – | ● | ● | ● | – | – | – | – | – |
| Repeated games (1) | – | – | ● | ● | – | – | ● | – | – |
| Social preferences (1) | ● | – | – | ● | ● | – | – | – | – |
| Behavioral GT (1) | ● | ● | ● | ● | ● | – | ● | – | ● |
| Mixed strategies (2) | – | ● | – | ● | ● | – | – | – | – |
| Dictator / Ultimatum (2) | ● | – | – | – | ● | – | – | – | – |
| Axelrod IPD (2) | – | – | ● | – | – | – | ● | – | – |
| Theory of Mind (2) | – | ● | ● | – | – | – | – | ● | – |
| Bayesian updating (2) | – | – | – | – | ● | ● | – | ● | – |
| Evolutionary GT (3) | – | – | – | ● | – | – | ● | – | – |
| Coop GT / mechanism design (3) | – | – | – | ● | – | – | – | – | – |
| Incomplete info (3) | – | – | – | ● | – | – | – | ● | – |
| Decision theory / bandits (3) | – | – | – | – | – | ● | – | – | – |
| Prospect theory (3) | ● | – | – | – | – | ● | – | – | – |

---

*Last compiled after reading all eight PDFs in `papers/game theory/` directly; Kozlowski & Evans from abstract only.*
