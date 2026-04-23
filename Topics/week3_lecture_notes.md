# Week 3 — The LLM / Game-Theory Literature, in Four Papers

---

## Reading guide
**🟦 Programmatic proposal** — *what are LLMs, as research subjects?*

- `Horton, Filippas & Manning (2023)` — *Large Language Models as Simulated Economic Agents: What Can We Learn from Homo Silicus?* NBER w31122. Persona prompting as a theory tool.

**🟩 Field maps and methodological frameworks** — *describe or critique the space*

- `Sun, Wu, Wang, Chen, Cheng, Deng & Chu (2025)` — *Game Theory Meets Large Language Models: A Systematic Survey with Taxonomy and New Frontiers.* Four-branch taxonomy of the field.
- `Kozlowski & Evans (2025)` — *Simulating Subjects: The Promise and Peril of AI Stand-Ins.* Six-weakness validity framework. Jingyao presents.

**🟨 Static behavioral evaluation** — *run LLM through games, measure aggregate behavior*

- `Lorè & Heydari (2024)` — *Structure vs. Framing.* One-shot 2×2 social-dilemma factorial.
- `Fan et al. (2024)` — *Can LLMs Serve as Rational Players? A Systematic Analysis.* 
- `MindGames (2025)` — Theory-of-mind + strategic-game benchmark.

**🟥 Dynamic / multi-agent evaluation** — *iterate, see what happens*

- `Akata, Schulz et al. (2025)` — *Playing Repeated Games with LLMs.* Ten rounds × 1,224 games, seven families.
- `Willis et al. (2025)` — *Will Systems of LLM Agents Cooperate?* LLM-authored strategies compete in a Moran-process tournament.

**🟪 Fine-tuning alternative** — *train a new model rather than prompt an existing one*

- `Binz et al. (2025) — Centaur.` Llama 3.1 70B fine-tuned on 10.7M human choices from 160 psychology experiments.


### Questions to bring with you

Anyone reading this literature for the first time surfaces roughly the same two threads. They are worth naming early, because the chapter comes back to each.

- **Is this reasoning, or is it pattern-matching?** When an LLM cooperates in a Prisoner's Dilemma, defects against a defector, or shifts its answer across narrative framings, is it *reasoning about the game* — or reproducing patterns from the vast amount of training text that describes such games? 
- **Does any of it generalize beyond toy games?** Every paper here uses stylized, short-horizon, binary, stakes-free interactions. The natural objection — can an LLM's play in a 2×2 PD tell us anything about how it would behave in a continuous-choice negotiation, a high-pressure medical decision, a multi-party institutional setting? This is a question of external validity; this lecture focuses on internal-validity. This mirrors the longstanding lab-to-field gap in Behavioral Economics, where controlled experiments identify behavioral primitives without guaranteeing real-world predictiveness. As a result, such toy models should be interpreted as isolating basic response patterns rather than providing robust forecasts of LLM behavior in naturalistic settings, a gap that ongoing work in richer multi-agent simulations (which we will look at in future lectures) seeks to address but has not yet resolved.


### Group-project pause

The LLM-behavior literature is no longer an unexplored frontier: the canonical experiments have largely been run, and their answers are now familiar. LLMs respond to incentives, they are sensitive to framing, they sometimes coordinate, and in repeated interactions like the Prisoner's Dilemma their cooperation depends heavily on the specific model and prompt. Extending this paradigm—by testing a new model, adding another context, or introducing yet another game—is technically straightforward but typically yields only incremental insights, effectively appending another entry to an already well-established list. The more promising direction may not be in further variations of the same setups, but in identifying qualitatively new puzzles—especially those emerging at the boundary of patterned heterogeneity, where systematic, non-random variation in behavior across contexts, prompts, or model architectures.

---

## 2. 🟦 Horton's programmatic move — *Homo silicus*

`Horton et al.` observe that LLMs, prompted to adopt a persona, produce verbal responses that read as plausibly human — and, crucially, that these responses shift in systematic ways when the persona shifts. 
A "socialist" persona and a "libertarian" persona, given the same scenario, produce different answers about fairness. A persona trained on equity considerations and one trained on efficiency produce different dictator-game allocations. A persona of a labor-market participant shifts hiring decisions when the minimum wage is raised.

The paper's proposal is to treat this capacity as a **theory tool**. The agents are called *Homo silicus*, in deliberate parallel to *Homo economicus* — stipulated rather than empirical, a modeling convention rather than a population. The five experiments re-run classic behavioral-economics paradigms:

1. `Kahneman, Knetsch & Thaler (1986)` — price-gouging fairness study;
2. `Charness & Rabin (2002)` — unilateral dictator games across preference types;
3. `Samuelson & Zeckhauser (1988)` — status-quo-bias federal-budget experiment;
4. `Oprea (2024)` — certainty-equivalent / prospect-theory paradigm;
5. `Horton`'s own minimum-wage hiring experiment.

The paper is careful about what it is *not* claiming. It does not claim that LLM responses are equivalent to human responses. It does not claim that the LLM is the human subject. It claims, more modestly, that running experiments on LLMs is cheap, fast, and conceptually useful as a way of **generating and pre-testing hypotheses** before paying human subjects.

The social-science reading of `Horton` is that he has re-opened an old question — what kind of object is *Homo economicus*? — with a new instrument. The LLM is not a homo-economicus replica; it is a new thing. Whether it is a better or worse stand-in for a person than the idealized maximizer of neoclassical theory is the question the subsequent literature picks up.

---

## 3. 🟩 Sun et al.'s field map — four branches where the research sits

A little over two years after `Horton`, the field needed a map. `Sun` and colleagues — a team based primarily at Peking University and Microsoft Research Asia — provide one. Their 2025 survey is explicitly a **taxonomy paper**: it does not run new experiments, it organizes the existing ones.

Their central contribution is Figure 1, a four-branch taxonomy of the intersection of game theory and LLM research.

```
  Game Theory  ×  Large Language Models   (Sun et al. 2025)
  │
  ├── §2  Evaluating LLMs in game-based playgrounds          ◀── most of our W2/W3 papers
  │   │
  │   ├── behavioral features     (what do LLMs do when they play?)
  │   │     🟦 Horton (W2)             — personas × classical behavioral paradigms
  │   │     🟨 Lorè & Heydari (W2)     — 2×2 games, structure vs. framing
  │   │     🟥 Akata (W2)              — repeated games, PD/BoS asymmetry
  │   │
  │   └── strategized agents      (can we engineer them to play better?)
  │         🟥 Akata SCoT (W2)         — prompt-level ToM scaffold
  │         🟥 Willis et al. (W3)      — evolutionary selection as engineering loop
  │
  ├── §3  Improving LLMs with game-theoretic methods
  │   ├── §3.1  interpretability (Shapley values)
  │   ├── §3.2  preference alignment (social choice)
  │   ├── §3.3  heterogeneity     ◀── ⚠ means "heterogeneous users",
  │   │                                 NOT within-model behavioral variance
  │   └── §3.4  dynamic adaptation
  │         🟩 Kozlowski & Evans (W3)  — straddles §2/§3; validity framework
  │                                      for LLM-as-subject simulation
  │
  ├── §4  Characterizing LLM-related events through game models
  │                                  (policy: developer competition, deployer incentives;
  │                                   no W2/W3 paper sits here)
  │
  └── §5  Advancing game theory with LLMs
                                     (LLMs as method, not subject;
                                      no W2/W3 paper sits here)

  Outside the taxonomy:
    🟩 Sun (W2)                    — is the taxonomy itself
    🟪 Binz et al. Centaur (W3)    — foundation model of human cognition, not GT
```

Rather than walk each branch abstractly, the more useful move is to ask a concrete question of each: *what would it mean, in practice, for research in this branch to "benefit humanity"?* The slogan is Willis's closing line, but it is standard in closing paragraphs of survey and policy papers more broadly. Each of Sun's four branches picks out a distinct *downstream* consequence that a political scientist, economist, or data scientist would recognise as the real stake.

**§2 — Knowing in advance where LLMs break.** This branch runs LLMs through games and catalogues the failures, producing a shortlist of deployment hazards with experimental evidence behind them. The consequences visible to this audience: LLMs "display adaptive economic strategies, *such as tacit collusion in pricing*" in Bertrand competition — an **antitrust concern** as soon as platforms deploy LLMs as pricing agents. They "regress to selfish or inconsistent strategies in complex scenarios without social scaffolding" — a concern for any **multi-party negotiation** an LLM is asked to represent. They lose "role consistency and logical coherence under pressure" in identity games — a **reliability** concern for any high-stakes role-playing deployment, from citizen service bots to legal triage. The downstream payoff of §2 is that these hazards are documented, so deployment and regulatory conversations can reference evidence rather than intuition.

**§3 — Making the model you interact with more accountable.** The technical repairs in this branch look inside-the-stack, but their downstream consequences are directly political. *Interpretability*: attributing a model's decision to specific inputs or components is the precondition for **audit** — which is in turn the precondition for algorithmic-accountability law (the EU AI Act, GDPR's "right to explanation"). *Alignment via min-max equilibrium* drops the assumption that human preferences are transitive and scalar — real preferences, including voting preferences, are neither, so an alignment procedure that assumes otherwise systematically misrepresents the people it is supposed to serve. *Preference heterogeneity*: Sun reports a striking finding — canonical RLHF is mathematically equivalent to **Borda count**, a voting rule with known **tyranny-of-the-majority** properties. Left uncorrected, this means the model you interact with is implicitly doing majority voting over whose preferences to honour, silently under-serving any subgroup that is a minority among the annotators. Social-choice axioms and mechanism design are being used to fix this. *Dynamic adaptation* stops the model from "reward-hacking" its own training signal as it improves. The §3 payoff is models that are **auditable**, **fairly-aligned across subgroups**, and **less likely to drift** — all things that matter in politics and economics long before they matter in ML.

**§4 — Predicting what the AI-rollout market will do before it does it.** This is the branch most directly relevant to economists and political scientists, because it treats LLMs as *institutional players* and models the strategic equilibria their deployment produces. Three concrete results give a sense of the leverage. `Taitler et al.` adapt **Braess's Paradox** to GenAI: a platform optimising for user revenue draws users away from the human knowledge forum it depends on (think Stack Overflow), which drains future training data, which eventually degrades the platform. Everyone ends up worse off despite each actor playing locally well — a classic system-level failure a regulator can actually aim policy at. `Laufer et al.` show that imposing safety standards only on *downstream* fine-tuners can incentivise *upstream* developers to underinvest in safety — a textbook **regulatory arbitrage** result, recognisable to anyone who has read the economics-of-regulation literature. `Buening et al.` derive payment rules that stop RLHF annotators from strategically misreporting their preferences, so the training data is not corrupted by the annotators' own incentives. These are the pieces that give regulators and platform designers real system-level failure modes to intervene on.

**§5 — Extending game-theoretic analysis into the domains classical mechanism design couldn't reach.** Classical mechanism design requires problems expressible in numbers, which rules out most of the coordination problems social scientists care about — citizen deliberation, policy bargaining, procurement on qualitative criteria, democratic preference elicitation. LLMs remove that restriction. *Generative social choice* (`Fish et al.`, `Boehmer et al.`) extracts preferences from free-text deliberation and produces representative policy slates — directly applicable to **Polis-style citizens' assemblies**, a growing instrument in democratic governance. *Semantic-enhanced auctions* (`Sun et al.`) let Vickrey and combinatorial auctions run on natural-language valuations — relevant to **public procurement** and policy design. *Verbalised Bayesian persuasion* models dialogue in real negotiations. *Mechanism-design as code generation* (`Liu et al.`) has the LLM write the mechanism itself, in human-readable form. The §5 payoff is **practical governance artefacts** for problems previously approachable only through qualitative analysis — many of which are the problems political science cares about most.

Sun writes the connective tissue himself at the close of §3: *"the game-theoretic methods used to enhance LLM interpretability, alignment, and adaptation do not exist in a vacuum. They are developed in response to the immense economic and social pressures that define the LLM ecosystem."* The four branches are not independent. §2 documents what LLMs get wrong; §3 builds accountability and fairness into the models themselves; §4 models the market and regulatory environment that determines whether those fixes actually get deployed; §5 uses LLMs to extend governance mechanisms into language-based domains previously out of reach. Willis's slogan "benefit humanity" means one of these four specific things, depending which branch the paper sits in. Our three empirical papers (Lorè & Heydari, Fan, Akata) live entirely inside §2, so the benefit story for *their* work is the surveillance one — they tell us what not to trust LLMs with in the domains that matter to this audience.

One load-bearing clarification from the taxonomy itself, before we move on: Sun's §3.3 "heterogeneity" node names *heterogeneous users* — different people wanting different things from their model — not within-model behavioural variance. The question of whether the *same* GPT-4, run a thousand times on the same prompt, behaves as one agent or as a mixture of behavioural types is **not on the list**. Patterned heterogeneity of LLM behaviour is the category Sun's taxonomy does not contain — and that absence is what Part II of this chapter is about.

*Group-project pause.* Read `Sun`'s taxonomy as a heatmap of saturation. The most saturated quadrant is §2 behavioral features — the place where a new 2×2 game with a new model produces the smallest marginal contribution. §3.3 (user-heterogeneity alignment) is well-populated. §5 (LLMs as a method for game theory) is underexplored and technically demanding. §4 is policy-relevant and needs social-science training rather than computer-science training. And the *genuine gap* — the category Sun's taxonomy does not contain at all — is the within-model, within-prompt heterogeneity question Part II will develop. 

---

## 4. 🟪 Centaur — fine-tuning instead of prompting

The four papers in the yellow and red sections below all *prompt* an existing model: the LLM is taken as given, situated in a game or task, and observed. `Binz et al. (Nature, 2025)` make a different move. Rather than ask what a pre-trained model does in a new situation, they **fine-tune a language model directly on human behavioral data** and evaluate whether the resulting model predicts the next choice of a held-out human subject. The distinction here is the same one you know from econometrics between *using someone else's published model* and *re-estimating its parameters on your own dataset*. On Sun's taxonomy, this move sits outside §2–§5 entirely — it is neither an evaluation of an existing model, nor an alignment fix, nor a game *about* LLMs, nor a use of LLMs *for* game theory. Within this chapter it is 🟪, the fifth category, and it is the paper on the reading list whose title most directly matches the title of this course.

### What Centaur is

Centaur is Llama 3.1 70B **fine-tuned** on **Psych-101**, a corpus the Binz group curated by transcribing 160 psychological experiments into natural language: 60,092 participants, 10.7 million choices, 253 million tokens. The fine-tuning technique used (QLoRA) updates only about 0.15% of the model's weights, which is why the whole training run fits on one GPU in five days instead of a cluster in months. The training objective is set up so the model learns to predict *the subject's next choice*, not to complete the experimental stimulus. One selection criterion is worth naming: Psych-101 is restricted to experiments whose stimuli and responses can be expressed in natural language — which rules out purely image-based tasks, motor tasks, and anything whose critical structure lives outside text.

The paradigms in Psych-101 are cognitive psychology, not game theory — multi-armed bandits, decision-making under risk, memory, categorization, Markov decision tasks. The case for putting Centaur on a game-theory reading list is that it is the state of the art at the job `Horton` proposed. Where *Homo silicus* is a theory tool — plausible, consistent with stylized facts, useful for pre-testing — Centaur is a trained prediction model, evaluated on negative log-likelihood against held-out responses.

### Where Centaur predicts well

On 32 held-out experiments it outperforms both the base Llama model and the best domain-specific cognitive model in nearly every case, across six domains:

```
  multi-armed bandits    ─ spatially correlated, structured, horizon, drifting 4-armed, ...
  decision-making        ─ choices13k, Iowa Gambling Task, intertemporal choice,
                           balloon analogue risk, two-step, multi-attribute, ...
  memory                 ─ digit span, N-back, recent probes
  supervised learning    ─ Shepard / Medin categorization, weather prediction
  Markov decision tasks  ─ two-step, Maggie's farm
  miscellaneous          ─ THINGS odd-one-out, grammar judgement, go/no-go, ...
```

Three generalization tests go beyond held-out participants:

1. **Modified cover story.** The two-step task with spaceships-and-aliens swapped for magic-carpets-and-planets. Centaur still predicts behavior; the domain-specific cognitive model breaks.
2. **New problem structure.** The horizon task extended from two-armed to three-armed bandits ("Maggie's Farm"). Centaur generalizes; the domain-specific model cannot be applied — its parameterization assumes two arms.
3. **Entirely new domain.** Logical-reasoning items from the LSAT — not represented in Psych-101 at all. Centaur beats the base Llama.

Centaur also predicts **response times**. The logic is Hick's law — harder decisions take longer — and "harder" is measured by how uncertain the model is about its own next-token answer on each trial. Plug that uncertainty measure into a linear mixed-effects regression on log-RT and Centaur explains substantially more variance than Llama or the cognitive baselines (conditional R² = 0.87 vs. 0.75 vs. 0.44).

### Alignment with human brain activity

A separate result from the paper, worth naming because it is a different *kind* of evidence — not behavioral prediction but representational similarity. After fine-tuning, Centaur's hidden-layer activations on a given trial correlate more strongly with aggregated human fMRI signal on the same trial than Llama's activations do (Fig. 4 in the paper). The procedure is straightforward: run each model on the trials the human subjects saw in a scanner, record the internal activations layer-by-layer, regress the averaged brain signal onto those activations, and compare the fits. Centaur wins, with the alignment peaking in the middle layers of the network. The modest claim is that fine-tuning on *behavior* has reshaped the model's internal *representations* toward something more brain-aligned — not the stronger claim that Centaur is mechanistically a brain.

### Where Centaur struggles

Two paradigms show *negative* Δ log-likelihood on Fig. 2a — Centaur predicts held-out behavior *worse* than the cognitive-model baseline: **grammar judgement** and **probabilistic instrumental learning.** Near-zero gains on the THINGS odd-one-out task and the serial reaction-time task.

A separate evaluation uses the four canonical economic games from `Dubois & Hauser`, in which the original study asked participants to predict both other humans and an artificial agent. Centaur predicts the *human* responses at 64% accuracy (matching humans); it predicts the *artificial-agent* responses at 35% (again matching humans — but well below what an optimizer would need). The authors frame this as evidence that Centaur is "human-like." For this course the sharper reading is that Centaur is tuned to the distribution Psych-101 contains, and its generalization does not extend to agent behavior the distribution does not contain. For multi-agent use downstream, that matters.

### One figure §8 will come back to

On the two-step task — a paradigm designed to separate *model-free* learners (who track which actions paid off before) from *model-based* learners (who plan using an internal map of the task) — Centaur's **open-loop simulations** (the model playing the task on its own rather than predicting one human trial at a time) produce a **bimodal** distribution on the model-based parameter (Fig. 2c). Some simulated trajectories are purely habit-driven, others purely planning-driven, with mixtures in between. The distribution matches the corresponding human distribution. The authors' sentence is worth noting: Centaur "does not merely capture the behaviour of the average participant, but rather the distribution over trajectories produced by the entire population." On this paradigm Centaur does what the prompt-based papers in the next two sections do not: produce the within-prompt, within-condition population structure that the behavioral-GT tradition learned to look for.

### What Centaur does not do

The persona input `Horton` uses is absent: age, demographics, personality, clinical status are not features of the model. The Fig. 2c bimodality is a clean match on one paradigm; whether the same individual participants are in the "model-based" cluster across multiple paradigms — the behavioral-GT question of whether types *generalize* — is not evaluated, though Psych-101's repeated-subject structure in principle contains enough signal for a follow-up to ask.

Worth naming explicitly for a course on *social* behavior: Psych-101 is cognitive psychology. There are no voting studies in it, no survey experiments, no negotiation datasets, no bargaining corpora. A reader hoping Centaur will predict voter choice, treaty positions, or coalition formation will find those domains outside its training distribution — the *Homo silicus* gesture `Horton` made covers that ground more directly (by persona-prompting off-the-shelf LLMs on political questions), at the cost of Centaur's trial-level predictive precision.

### What the 🟪 category adds up to

Centaur is the only paper on this reading list whose methodological move is *training* rather than prompting. The category is small because fine-tuning a 70B-parameter model on curated human-behavioral data is a capital-intensive research program; the output, when successful, is a model whose trial-level predictions beat cognitive models on most paradigms in its training distribution, and that generalizes to modified cover stories, new problem structures, and one new domain. The category's limits inherit its design choices: no persona input, a training distribution that does not include adversarial or non-human agents, and, on two paradigms (grammar judgement, probabilistic instrumental learning), an accuracy the cognitive baseline still outperforms.

Where the category matters for the rest of this chapter is the mixture signal of Fig. 2c. The default reading of the prompt-based papers in §5 and §6 below is that the field reports aggregate means and stops there. Centaur, on at least one paradigm, does not: it reproduces the human *distribution* of model-based vs. model-free trajectories. §8 treats this as the one partial counterexample to the missed-mixture diagnosis.

---

## 5. 🟨 Static behavioral evaluation — Lorè & Heydari, Fan, MindGames

The move these three papers share is the simplest one in the literature: take a catalogue of games whose equilibria theory already understands, run an LLM through them many times, and report how often the LLM plays each strategy. No iteration, no opponent learning, no strategic context beyond what the prompt describes. The unit of analysis is the model; the datum is the proportion of trials on which the model played each action; the comparison is across models, games, and framings.

This is the aggregate-means playbook of early behavioral game theory applied to a new subject. It is where the field starts, and — as Part II will argue — it is where most of the field still sits. The three papers in this category differ chiefly in how wide they cast the net: Lorè & Heydari run a tight factorial, Fan runs a broader battery, MindGames packages the move into a standardized benchmark.

### Lorè & Heydari — structure vs. framing

`Lorè and Heydari` ask a cleanly delimited question: in a one-shot 2×2 game, does the LLM respond to **the structure of the payoffs** or to **how the game is narratively framed** — and how does that trade-off differ across models?


```
                        models  (3)       games  (4)              contexts  (5)
                       ─────────────    ──────────────────      ──────────────────
                       GPT-3.5          Prisoner's Dilemma      international summit
                       GPT-4       ×    Stag Hunt           ×   business meeting
                       Llama-2 70B      Snowdrift (Chicken)     environmental negot.
                                        Prisoner's Delight      conversation, friends
                                                                chat among teammates
```

The findings differ sharply across models — but what matters is less *which* model does *what* and more *along which axes* they differ.

```
  axis of variation          GPT-3.5           GPT-4                 Llama-2
  ────────────────────────   ────────────      ─────────────────     ───────────────────
  response to payoffs        weak              strong                strong
  response to framing        strong            modulated             calibrated
  within-cell distribution   weakly mixed      near-bimodal, pure    genuinely mixed
```

*Reading these three axes through the reasoning-vs-pattern-matching lens.* This is the question flagged at the start of the chapter, and `Lorè and Heydari`'s factorial is one of the few places where it can be asked cleanly. A reasoner about the game should respond to **payoff structure** and be **invariant across framings** — the structure carries the information, the wrapper is decoration. A pattern-matcher should do the reverse: respond to the narrative wrapper, be largely insensitive to payoffs, because in training text a "game-like" situation is more reliably indexed by its surface story than by its payoff matrix.

On this axis: GPT-3.5 sits near the pattern-matcher end. Llama-2 sits near the reasoner end. GPT-4 sits between — structure-sensitive across cells but, within a cell, collapsing to two near-pure modes. That middle position is precisely what Part II will come back to.

The finding that will reward close attention in Part II is the bimodality of GPT-4's behavior. Three hundred initializations of the same prompt produce a distribution that bunches at the two extremes of the response scale. In the human experimental literature, a bimodal distribution across many runs of the same manipulation is a textbook signature of a **two-type population** — the kind of finding that, in the 1990s, drove the decomposition of PGG contributors into conditional cooperators and free-riders.

### Fan et al. — the systematic version

`Fan et al. (2024)` is the systematic cousin of Lorè & Heydari: a wider battery of games, an explicit rationality criterion drawn from classical solution concepts, and aggregation across a similar cross-model panel. Fan asks which models track which equilibrium predictions across the battery — which dominate-strategy-reason, which backward-induct, which best-respond to stated beliefs — and reports, unsurprisingly, that model capability tracks these rationality metrics in the direction one would expect.

What is structurally identical to Lorè & Heydari is the unit of analysis. When there are hundreds of runs per cell, the within-cell distribution is not examined. A GPT-4 rationality score of 0.78 on a given game could come from a coherent model reasoning about the payoffs correctly 78% of the time, or from a mixture in which one sub-population plays rationally on every run and another plays at random. Fan cannot distinguish the two, because the question is not asked. Read Fan as the broader evidence for the empirical pattern Lorè & Heydari report on a smaller panel; read its silence on within-model distributions as the same silence this chapter will diagnose in Part II.

---

## 6. 🟥 Dynamic / multi-agent evaluation — Akata, Willis

The move these two papers share is to put time back into the experiment. Where the yellow category collapses each interaction to a single decision and averages over many such decisions, the red category iterates: the model sees its own past moves and its partner's past moves, the partner's next move is a response to the model's last one, and the unit of analysis is a *trajectory* rather than a trial.

What changes with iteration is which questions can be asked. Theory of mind becomes visible because tracking a partner's beliefs matters only across time. Cooperation norms become visible because forgiveness and retaliation are time-indexed concepts. Equilibrium selection becomes visible because an alternating Battle-of-the-Sexes equilibrium can only exist over repeated play. The two papers here represent two natural places to iterate: Akata iterates the game (the same two players play many rounds), Willis iterates the strategies (a population of LLM-authored strategies competes across generations).

### Akata et al. — repeated dyadic play

The natural extension of `Lorè and Heydari` is to ask what happens when the games are iterated rather than one-shot. `Akata` and colleagues do exactly that.

The core finding is an **asymmetry** between two kinds of strategic situation.

```
                    self-interest dominant        coordination dominant
                    ──────────────────────       ──────────────────────
  family            Prisoner's Dilemma            Battle of the Sexes

  GPT-4 behavior    defects when rational;        picks own preferred point;
                    retaliates on defection;      refuses to alternate even
                    NEVER forgives                with an alternating partner

  vocabulary        pure grim-trigger             failure to track beliefs

  assessment        rational ✓                    theory of mind ✗
                    (bad for collective)          (bad for the joint payoff)

  SCoT repair?      not needed                    YES — asking GPT-4 to
                                                  predict partner first
                                                  substantially improves play
```

**In self-interest-dominant games** — the Prisoner's Dilemma family — GPT-4 performs very well by individual-rationality standards. It defects where rational theory says it should. Against an opponent that defects once, GPT-4 retaliates — and, critically, **never forgives**. This is excellent for GPT-4's individual payoff, worse for the collective. The behavior reads as a pure-grim-trigger strategy: cooperate until defection, then defect forever.

**In coordination-dominant games** — Battle of the Sexes most sharply — GPT-4 fails. It picks its own preferred coordination point and refuses to alternate, even when paired with an explicitly alternating partner. The failure is not that GPT-4 is selfish; the failure is that it cannot model a partner who is also trying to coordinate. In behavioral-GT vocabulary, this is a failure of **theory of mind**: modeling what the other player is doing requires tracking their beliefs, not just their past actions.

The paper adds an interesting **intervention**. Prompting GPT-4 to first *predict the partner's next move* before choosing its own — what the authors call Social Chain-of-Thought prompting — substantially improves coordination-game play. Human evaluators, shown interaction transcripts blind, rate the SCoT-prompted GPT-4 partner as more human-like than the unprompted version.

The SCoT finding sharpens a design tension worth naming, because it is the one reasonable readers are fastest to raise. Unprompted GPT-4 plays the Prisoner's Dilemma in a way that is *individually rational* — it retaliates against defectors and collects the higher payoff that the grim-trigger strategy affords. SCoT-prompted GPT-4 plays more like a human — more cooperative, more coordinated, more forgiving, and judged more human-like by blind evaluators. But "more human-like" is not the same as "more rational," and is sometimes its opposite. When we nudge the model with an explicit theory-of-mind scaffold, are we *improving* it, or are we *moving it away* from the cold-rational behavior that an optimizer might actually want? The answer depends on what the LLM is being built to do. For joint welfare in a coordination problem, SCoT wins; for unilateral payoff maximization in a PD against a defector, the unprompted model wins. The field has not settled which of these its default evaluative criterion should be. "Human-like" is not the only option, and it is not obviously the correct one.

`Akata et al.` is, methodologically, the closest thing in this literature to classical behavioral game theory. The design is in the tradition of Camerer's experimental-GT corpus, scaled up. The measurements are clean. The findings are interpretable. The one place where the paper steps back from the full behavioral-GT playbook is precisely where `Lorè and Heydari` also step back: the analysis is cross-model. GPT-4 retaliates; Claude 2 retaliates differently; Llama-2 is more forgiving. Each model is reported as an agent with a strategic profile. Within-model heterogeneity — whether GPT-4 itself has, say, a "forgiving cluster" and an "unforgiving cluster" across its 1,224 × 10 = 12,240 possible behavioral trajectories — is not the question the paper asks.

### Willis et al. — evolutionary selection among strategies

`Willis et al. (2025)` takes the dyadic repeated-PD setting one level up. Rather than asking an LLM to play, Willis asks the LLM to *write* IPD strategies as Python code; those strategies are then entered into a **Moran-process tournament** — an evolutionary simulation in which successful strategies reproduce and unsuccessful ones drop out — and the equilibrium mix is whatever composition selection converges on. The empirical finding is cross-model in exactly the sense Akata's finding is cross-model: GPT-4o's strategies evolve toward aggression, Claude's toward cooperation. The unit of analysis is the LLM-as-author, not the strategy-as-distribution.

Read Willis as `Axelrod (1984)` rerun with LLM-authored strategies in place of hand-submitted ones — and with the same analytic ceiling. The evolutionary frame also surfaces a problem worth flagging: adding 10% action noise breaks coordination, and the paper does not address whether a single model could generate a *diversity* of noise-robust strategies rather than one dominant type. That is, once again, a mixture question. It is implicit in the setup; it is not analyzed.

### What the red category adds up to

Iterating does what one-shot cannot: it makes theory of mind, equilibrium selection, and norms of retaliation and forgiveness visible as behavioral data. That is the payoff of the red category over the yellow one, and it is real — Akata's PD/BoS asymmetry is not a finding the static evaluations could have produced, and Willis's aggression/cooperation split across model authors would have been invisible without an evolutionary tournament to play it out in.

What iteration does *not* do, on its own, is surface within-model heterogeneity. Akata reports model-level strategic profiles. Willis reports model-level evolutionary tendencies. In neither paper does the distribution of *trajectories within a model* become the object of analysis — despite the fact that, with 1,224 games × 10 rounds in Akata's panel, the data to ask the question exist. The red category extends what the field sees along the time axis without extending what it sees along the population axis. Both extensions are available. Part II is about what happens when you take the second one.

---

## 7. Interim Conclusion

Three positive claims the literature can reasonably make:
1. **LLMs respond to game-theoretic structure.** Payoff orderings that theory says should matter do matter to LLM responses, at least for the more capable models (`Lorè & Heydari`; `Akata`).
2. **LLMs are sensitive to framing.** Context modulates behavior even when payoffs are held constant, in ways reminiscent of the Tversky–Kahneman framing literature (`Lorè & Heydari`).
3. **LLMs reproduce classical behavioral-economics effects directionally.** Fairness judgments, dictator-game allocations, and other workhorse findings shift in the directions human subjects would shift under analogous manipulations (`Horton`).

One methodological gap, consistent across the empirical papers, is what the second part of this chapter is about.

---

## 8. 🧭 The methodological move the literature has not yet made

Behavioral game theory was, from the 1960s through the early 1990s, a field that reported aggregate means. Subjects cooperated at some fraction; rejection rates in the ultimatum game clustered around some value; fairness judgments split by some proportion. Papers reported these aggregates and compared them across conditions.

Then the literature took a methodological step that redefined what its outputs were. In the late 1990s, researchers began to ask whether the aggregate was hiding the structure — whether behind a 45% cooperation rate there was a population in which some subjects cooperated 80% of the time, others 15%, with essentially no one cooperating close to the mean. The now-classic result is `Fischbacher, Gächter & Fehr (2001)`, published in *Economics Letters*, which took the public-goods game and showed that the population decomposed into roughly half conditional cooperators (contributing proportionally to their beliefs about others), a third free-riders (contributing near zero regardless), and a residual of other types. Subsequent work extended the taxonomy. `Kurzban & Houser (2005)` and `Fischbacher & Gächter (2010)` added altruists, hump-shaped contributors, and a category of inconsistent or switching players. `Andreoni & Miller (2002)` did the analogous decomposition for dictator-game preferences using revealed-preference methods.


The pattern, for a reader with a foothold in either tradition, is clear. The move from *aggregate means* to *patterned heterogeneity* — the recognition that the population is a mixture of types and that the types can be recovered from the data — was not a decorative addition to the field. It was the methodological shift that made behavioral game theory into the empirical science it is today. The questions the mixture-view lets you ask (are types stable? do they predict behavior in other games? are they correlated with demographics? do they respond to interventions?) are orthogonal to the questions the aggregate-view lets you ask, and they are the questions the modern literature spends most of its time on.

The four LLM-behavior papers we have read are where behavioral GT was in 1996. The findings are interesting, the experimental designs are clean, and the reports are of aggregates. The step from aggregates to types has not been taken — not by Horton (whose heterogeneity is imposed via the persona prompt, not recovered from data), not by `Lorè and Heydari` (who report bimodal GPT-4 and move past it without fitting the two components), not by Akata (whose heterogeneity is cross-model only, not within-model), and not by Sun's survey taxonomy (whose "heterogeneity" node is about users, not model behavior).

§4's 🟪 `Binz et al. Centaur` — now behind us — is the most important partial counterexample to the diagnosis above. On the two-step task, Fig. 2c of the Centaur paper shows the model reproducing the full bimodal distribution of human trajectories: purely model-free, purely model-based, and mixtures thereof. The aggregate-means reading of the LLM-behavior literature does not extend to Centaur on this paradigm; the mixture that behavioral GT learned to look for is there, and Centaur captures it.

The counterexample is specific, and its edges are worth drawing. Centaur reproduces the population distribution *on paradigms Psych-101 contains in volume* (two-step, horizon), and it does so as a byproduct of fitting the full distribution of training data rather than via an explicit mixture-model architecture. What Centaur does not yet do is run the behavioral-GT program *as* a behavioral-GT program: persona features are not an input, types are not recovered as clusters, and the stability of types across paradigms — the question that distinguishes a stable behavioral phenotype from a task-specific strategy — is not evaluated, though Psych-101's repeated-subject structure could in principle support that evaluation. The 1996 step is partially taken, on one figure of one paper, and has not yet been built on.

The field's default object of analysis is still the aggregate. The single clear counterexample in this week's reading sits in Fig. 2c of the Centaur paper; the prompt-based literature has not followed Centaur's move onto the distribution side of the problem, and Centaur has not yet taken the next step of recovering types explicitly. The missed-mixture pattern is still a feature of the research question the field has chosen to ask — attenuated, on one axis, by one paper.

This is not a criticism of the papers. Each of them is a well-executed piece of work in its own frame. It is a diagnosis of where the literature as a whole is in its methodological cycle. The field is one methodological step away from the equivalent of its own Fischbacher-Gächter-Fehr moment, and the step is identifiable: treat every LLM trajectory — each of `Lorè and Heydari`'s 300 runs per cell, each of Akata's 10-round games, each of Horton's persona replications — as a unit of behavior. Ask whether the trajectories form clusters. Ask whether the clusters are stable across seeds, prompts, and games. Ask whether the latent structure they reveal is an artifact of the prompt or a property of the model.


---

## 9. 🟩 What Kozlowski and Evans add

`Kozlowski and Evans` approach the same literature from a different angle. Where we have spent this lecture asking whether the behavioral-GT *method* has fully transferred to LLMs, they ask whether the *validity apparatus* that social science developed for human subjects transfers at all. Their answer is a structured list of six reasons to worry: bias, uniformity, atemporality, linguistic cultures, disembodiment, and "alien intelligence."

The uniformity concern in particular — their Figure 6, which shows GPT-4 responding to the General Social Survey with far lower variance than the human population does — sits very close to what we just discussed. Low variance within a persona is a *symptom* of the missed-mixture problem from the other direction. If GPT-4's response distribution is bunched at one or two modes where the human distribution is spread, then either the model has a few behavioral types that the interview prompt fails to separate, or the model lacks the kind of within-subject variability that makes humans a population rather than a prototype. Either interpretation has consequences for simulation-based research.

`Kozlowski and Evans` are careful and measured. They do not argue that LLM simulation is useless; they argue that it is technically difficult in specific ways that do not correspond neatly to the social-science validity vocabulary we are used to. Their two proposed paradigms — *validate-then-simulate* and *simulate-then-validate* — are a structured response to the same fundamental question we have been asking: *what are we measuring when we measure an LLM, and how would we know if we were measuring it wrong?*

Two specific references in the chapter are worth flagging now — neither is on the syllabus, but both point outward to directions the course should acknowledge and either could seed a group-project angle:

- **`Park et al. (2024)` — the "1,000 persona" study.** Each simulated person is prompted with the transcript of a two-hour interview they themselves gave; the paper reports 85% test-retest agreement between a human and their LLM twin on a survey battery. `Kozlowski and Evans` cite this as the strongest *positive* case for LLM simulation. The method is worth naming: **many-shot prompting with the individual's own words in the context window** — not fine-tuning — which sidesteps the uniformity and bias failure modes by anchoring the model to a specific voice rather than a learned aggregate.
- **`Vong et al. (2024)` — and the first-person-video frontier.** A vision-language model trained on roughly 65 hours of head-mounted first-person video from a child aged 6–25 months; the resulting model grounds words to visual referents rather than to other words. `Kozlowski and Evans` flag it as the remedy-direction for the *disembodiment* weakness. The larger point: this is the entry to a research programme that industry labs (Meta Ego4D and Project Aria, DeepMind, Apple) are investing in heavily, and that may become central to multi-agent social simulation in the next few years. **For anyone scouting a future group-project angle: first-person / embodied data as an alternative to text-only training is a live, open frontier.** 

---
