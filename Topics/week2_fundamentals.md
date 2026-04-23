# Chapter 2 — Game Theory as a Diagnostic Language

*A companion to Week 2 of the Konstanz seminar on Dynamic Social Behavior. The week's purpose is to supply the game-theoretic vocabulary with which the rest of the course will interrogate LLM behavior. Every paper this week, and most of what follows, takes a position — implicit or explicit — on whether strategic language agents behave as self-interested maximizers, as bounded-rational humans, or as something else. We cannot adjudicate without the framework.*

---

## Reading Guide

- 🟦 **Horton, Filippas & Manning (2023)** — *Large language models as simulated economic agents: What can we learn from Homo Silicus?* NBER w31122. The paper that opened "silicon sampling" in economics.
- 🟩 **Lorè & Heydari (2024)** — *Strategic Behavior of Large Language Models and the Role of Game Structure vs. Contextual Framing.* *Scientific Reports*. Tests LLMs across the 2×2 social-dilemma taxonomy.
- 🟨 **Akata, Schulz et al. (2025)** — *Playing repeated games with large language models.* *Nature Human Behaviour*. Repeated PD and Battle of the Sexes; a striking asymmetry in how LLMs fail.
- 🟥 **Sun, Huang, Pompili (2025)** — *Game Theory Meets LLMs and Agentic AI: A Systematic Survey.* The field's atlas.

Bridge paper (not tagged, cited as context): 🧭 **Hausladen, Engel & Schubert (2026)** — on latent intentions in repeated linear Public Goods Games. Used as the behavioral-GT anchor you already know from the PGG data.

A paper-to-concept reverse index closes the chapter.

---

## 1. The strategic-interaction picture

The starting point for everything in this week, and most of what follows, is an idea so familiar that social-science students occasionally miss how strong it is: **when the outcome of your choice depends on someone else's choice, and vice versa, we are no longer in decision theory — we are in game theory.**

**von Neumann & Morgenstern** published *Theory of Games and Economic Behavior* in 1944 against the backdrop of wartime strategic analysis. The book's radical move was to treat economic and social interaction as **games** — formal objects with players, strategies, and payoffs — and to ask what a rational outcome would be. **Nash (1950)** proved that equilibria exist in a broad class of games under reasonable assumptions. The 1994 Nobel Prize recognized the centrality of the framework (Nash, Harsanyi, Selten).

A **normal-form** (or strategic-form) game consists of:
- a set of **players**,
- for each player, a set of **strategies**,
- for each strategy profile, a **payoff** for each player.

A **Nash equilibrium** is a strategy profile in which no player can gain by unilaterally changing strategy, given what the others are doing. A **dominant strategy** is one that is best regardless of what others do. The Prisoner's Dilemma is the cleanest case of a game with a dominant strategy (defect) that leads to a collectively bad outcome.

The social-science reason to learn this carefully is that it is the **diagnostic language** for every subsequent claim about rationality, cooperation, and deviation. When Akata 🟨 finds that LLMs fail at Battle of the Sexes and succeed at Prisoner's Dilemma, the finding is only legible if you know that those games have different equilibrium structures and different failure modes. Without the framework, it is just a list of results.

---

## 2. The 2×2 taxonomy of social dilemmas

Social interaction can be classified, to first approximation, by the rank ordering of four payoffs: **R** (reward for mutual cooperation), **T** (temptation to defect), **S** (sucker's payoff), **P** (punishment for mutual defection). Different orderings pick out different games, and these games have strikingly different structures.

- **Prisoner's Dilemma** — T > R > P > S. Defection is dominant; mutual defection is the unique equilibrium; mutual cooperation is Pareto-superior but unstable. The canonical social dilemma. **Axelrod (1984)** is the reference point for how cooperation can nonetheless emerge under iteration.
- **Stag Hunt** (assurance game) — R > T > P > S. Two equilibria: (cooperate, cooperate) and (defect, defect). Cooperation is risky but not dominated; the coordination problem is about **trust and expectations**. **Rousseau's** hunt in the *Discourse on Inequality* is the origin. **Jervis (1978)** made Stag Hunt the frame for the **security dilemma** in international relations.
- **Chicken / Snowdrift** — T > R > S > P. Two asymmetric pure equilibria (one defects, one cooperates) plus a mixed-strategy equilibrium. The game of **brinkmanship** (Schelling 1960). The 1962 Cuban Missile Crisis is the canonical example.
- **Harmony** (or "Prisoner's Delight") — R > T > P > S with S > P — cooperation is dominant. Not a dilemma at all; the "good" 2×2.

**Lorè & Heydari 🟩** is structured around this taxonomy. Their central finding is that LLMs respond not only to the **game structure** (which payoff ordering) but also to the **contextual framing** (what the game is called, what the choices are labeled). This is the computational rediscovery of the **framing effect** (Tversky & Kahneman 1981, *Science*), now applied to machine agents.

A coordination game like **Battle of the Sexes** deserves a line: two players want to coordinate (e.g., both go to the opera, or both go to the boxing match) but disagree on which equilibrium. There is no dominant strategy; the failure mode is **coordination failure**, not defection. **Akata 🟨's** central finding is that LLMs handle PD reasonably but fail badly at BoS, because coordination requires modeling the other player's beliefs rather than simply inferring their incentive.

---

## 3. The two failure modes: defection vs. coordination failure

A distinction the week's readings sharpen and that every student should own.

**Defection** is what happens when individual rationality leads away from collective benefit. Its paradigm is the Prisoner's Dilemma. The remedy, when there is one, is structural: iteration (Axelrod), punishment (Fehr & Gächter 2000), or institutions (Ostrom 1990; see Chapter 7).

**Coordination failure** is what happens when multiple equilibria exist and the parties cannot align on one. Its paradigm is Battle of the Sexes or the pure coordination game. The remedy is informational: focal points (Schelling 1960), convention (Lewis 1969; see Chapter 5), or correlated signals.

That LLMs can navigate one failure mode but not the other — 🟨's striking result — suggests that they are not simply "rational agents with bugs." They have a specific cognitive profile that social-science methods can diagnose, if we are careful about which question we are asking.

---

## 4. Repeated games and the shadow of the future

The backward-induction paradox of finitely repeated Prisoner's Dilemma: if defection is dominant in the last round, rational players defect in the last round; by backward induction, they defect in the second-to-last, and so on back to round one. Rational play predicts ALLD. Humans, empirically, do not play ALLD.

**Axelrod's tournaments** (1980, 1984) addressed the puzzle by running computer-simulated round-robin contests among submitted strategies. **Tit-for-Tat** — cooperate first, then mirror the opponent's last move — won both tournaments. Axelrod distilled the conditions for cooperation into memorable slogans: *niceness* (don't defect first), *provocability* (retaliate), *forgiveness* (don't hold grudges), *clarity* (be easy to read). The **shadow of the future** — the probability that interaction continues — is the central parameter. Long shadows sustain cooperation; short shadows destroy it.

**Nowak & Sigmund (1993)** added **Win-Stay-Lose-Shift (Pavlov)**, which outperforms TFT in noisy environments. **Wu & Axelrod (1995)** showed why: a single misperception under TFT triggers mutual defection that cannot be repaired without an explicit forgiveness move. Every subsequent IPD study is in dialogue with this lineage.

🟨 Akata et al. run LLMs through the iterated PD and find broadly cooperative behavior under ideal conditions, with characteristic breakdowns. The finding is interesting because it is *exactly* the shape of the findings in the behavioral-GT literature (Camerer 2003) for human subjects. What differs is not the pattern but the mechanism producing it.

---

## 5. Social preferences: the departure from Homo economicus

Classical economic theory treats agents as **self-interested expected-utility maximizers**. The tradition of **behavioral economics** — associated with Kahneman & Tversky, Thaler, Fehr — has produced a half-century of evidence that real humans are systematically different.

Three families of results that matter here:

**Fairness and equity.** In the **Ultimatum Game** (Güth, Schmittberger & Schwarze 1982), proposers offer a split of a pie; responders accept or reject. Rational theory says responders should accept any positive offer; empirically, offers below about 30% are routinely rejected, even in high-stakes experiments and across cultures (Henrich et al. 2001, *AER*). In the **Dictator Game**, proposers give without any enforcement; most give positive amounts. **Fehr & Schmidt (1999, *QJE*)** formalized **inequity aversion**: agents dislike payoff inequality, more so when it disadvantages them. **Charness & Rabin (2002, *QJE*)** extended the typology to include efficiency concerns and reciprocity.

**Altruistic punishment.** **Fehr & Gächter (2000, 2002, *AER / Nature*)** showed that in public-goods games, allowing costly punishment of free-riders sustains cooperation at near-efficient levels. Punishment is costly to the punisher and therefore irrational under narrow self-interest; the finding is a behavioral cornerstone.

**Framing and heuristic response.** **Tversky & Kahneman (1981, *Science*)** demonstrated that equivalent decisions presented in different terms (gains vs. losses; lives saved vs. lives lost) produce different choices. This is **prospect theory** in its applied register; **Oprea (2024, *AER*)** has argued that much of what looks like prospect-theoretic curvature is instead a **complexity heuristic** — agents economize on cognitive effort when evaluations are hard.

🟦 Horton's *Homo Silicus* proposes that LLMs can be run through the same experimental paradigms and will produce similar deviations — endowed with appropriate prompts, they behave like Fehr-Schmidt-style agents, not like cold maximizers. The paper is a bridge: if LLMs systematically reproduce behavioral-economics findings, they may be usable as **pilot subjects** in experimental design. The literature since has both confirmed and complicated this. Charness, Jabarian & List (2023) survey the state of play.

---

## 6. Homo economicus, Homo silicus, and the older philosophical argument

Homo economicus is a modeling convention, not an empirical claim. **Persky (1995)** traced its history: the "economic man" of Mill and the marginalist tradition was always a deliberate abstraction, acknowledged by its users to differ from the flesh-and-blood agent. The behavioral critique reopened an old question: once we specify that our agent has fairness preferences, loss aversion, limited cognitive resources, and social context, are we still doing economics, or are we doing psychology?

🟦 Horton's Homo Silicus is a third entry in this lineage. The LLM, given an experimental prompt, produces behavior that can be measured against both Homo economicus and empirical human data. The epistemic status of the result depends on what we think we are measuring — a feature of the model, a feature of its training corpus, or a feature of human social behavior reflected in text.

The same question recurs in every subsequent chapter of this book. Week 2's job is to make it articulable.

---

## 7. The panorama: what game theory knows, at a glance

🟥 **Sun, Huang & Pompili** provide the field's atlas. They survey the intersections of classical game theory and LLM research across:
- cooperative vs. non-cooperative games,
- perfect vs. imperfect information,
- complete vs. incomplete information,
- symmetric vs. asymmetric games,
- single-shot vs. repeated interaction,
- the solution concepts: Nash, minimax, Stackelberg, Bayesian equilibrium, Shapley value.

Students do not need to master all of these. They need to **recognize the vocabulary** so that when it appears in later readings (Diplomacy's bargaining in Chapter 6, mechanism design in Chapter 7), the reference is legible rather than opaque. Sun et al. function as the course's dictionary.

A minimum fluency checklist:

- **Zero-sum vs. non-zero-sum** — whether one player's gain is necessarily another's loss.
- **Cooperative vs. non-cooperative** — whether binding agreements are available.
- **Perfect information** — whether all players observe all past moves (chess yes, poker no).
- **Complete information** — whether players know each other's payoffs and types (Harsanyi's extension to Bayesian games when they don't — Chapter 6).
- **Stackelberg leader-follower** — sequential move; the leader commits first.
- **Shapley value** — a fair allocation in cooperative games, based on average marginal contribution.

That is the vocabulary. Whether you use it heavily or lightly, you should recognize it.

---

## 8. Behavioral game theory as an empirical discipline

One conceptual move worth making explicit. **Classical game theory** tells us what rational players should do. **Behavioral game theory** — the program associated with **Camerer (2003, *Behavioral Game Theory*)** — measures what actual humans do, and quantifies the systematic gap.

The behavioral-GT project rests on three empirical programs:

1. **Level-k / cognitive hierarchy models** (Stahl & Wilson 1994; Camerer, Ho & Chong 2004) — people reason a finite number of steps deep about their opponents' reasoning. The data fit level-1 and level-2 players more than infinitely-rational Nash players.
2. **Learning models** (Erev & Roth 1998; Camerer & Ho 1999) — people adjust strategies over time based on experience, in ways captured by reinforcement learning and belief-learning models. This is the social-science ancestor of the RL frameworks we will see in Chapters 6 and 7.
3. **Social-preference models** (Fehr-Schmidt; Charness-Rabin) — equilibrium predictions change once utility functions include fairness, efficiency, or reciprocity.

Behavioral GT is the natural home for everything this course does with LLMs. When we ask whether an LLM is a "rational player," we are implicitly asking about the distance between its behavior and the Nash prediction, in exactly the way behavioral GT asks about humans. Fan et al. (Chapter 3) make this explicit.

---

## 9. The bridge from behavioral GT to the PGG data

One reason Week 2 anchors in the repeated **Public Goods Game** is that PGGs are the workhorse of experimental cooperation research. **Ledyard (1995)** surveyed the literature and established the canonical findings: contributions start at roughly half the efficient level and decay toward the free-riding equilibrium over repeated rounds, absent punishment or communication.

The Hausladen, Engel & Schubert 🧭 paper accompanying the seminar studies **latent intentions** in repeated linear PGGs. The methodological move is to extract unobserved cooperative or defective *intentions* from observed contribution trajectories using dynamic time-warping and hierarchical latent models. The paper sits in the behavioral-GT tradition — it takes human data seriously, classifies players into behavioral types, and treats the type distribution as the object of study.

This is the **bridge** between behavioral GT and the LLM literature. When LLMs play these games (🟨 Akata; and extensions in subsequent papers), the natural comparison is not to the Nash prediction — which we already know humans violate — but to the **distribution of human behavioral types** documented over fifty years of PGG research. Whether an LLM population matches that distribution, or produces a characteristically different one, is the empirically answerable question.

---

## Paper-to-concept reading map

- 🟦 **Horton — Homo Silicus.** Bring §1 (strategic interaction as framework), §5 (social preferences: Fehr-Schmidt inequity aversion; Ultimatum and Dictator games), §6 (Homo economicus as modeling convention; Persky's history; the epistemic status of a model agent). The central debate is whether LLM-generated behavior that matches behavioral-economics findings is a **property of the model** or a **reflection of human behavior preserved in training text**.
- 🟩 **Lorè & Heydari — Game Structure vs. Contextual Framing.** Bring §2 (the 2×2 taxonomy in full — PD, Stag Hunt, Chicken, Harmony), §3 (coordination vs. defection as distinct failure modes), §5 (framing effects from Tversky & Kahneman; prospect theory; Oprea's complexity critique). The central debate is whether sensitivity to framing is a bug, a feature, or a property LLMs share with humans.
- 🟨 **Akata — Playing Repeated Games.** Bring §3 (coordination vs. defection), §4 (repeated-game theory; shadow of the future; Axelrod tournaments and canonical strategies), §8 (behavioral GT as empirical discipline), §9 (PGG behavioral types as the natural comparison class). The central debate is why LLMs pass PD and fail BoS — what this says about machine theory of mind.
- 🟥 **Sun — Game Theory Meets LLMs survey.** Bring §7 (the panorama: vocabulary the student should recognize). Use this paper for map-reading, not depth.

---

## Further reading from the social sciences

- von Neumann, J. & Morgenstern, O. (1944). *Theory of Games and Economic Behavior*. Princeton UP.
- Nash, J. (1950). Equilibrium points in n-person games. *PNAS*.
- Schelling, T. C. (1960). *The Strategy of Conflict*. Harvard UP.
- Axelrod, R. (1984). *The Evolution of Cooperation*. Basic Books.
- Jervis, R. (1978). Cooperation under the security dilemma. *World Politics*.
- Camerer, C. F. (2003). *Behavioral Game Theory*. Princeton UP.
- Fehr, E. & Schmidt, K. M. (1999). A theory of fairness, competition, and cooperation. *QJE*.
- Charness, G. & Rabin, M. (2002). Understanding social preferences with simple tests. *QJE*.
- Fehr, E. & Gächter, S. (2000, 2002). Cooperation and punishment. *AER / Nature*.
- Henrich, J. et al. (2001). In search of Homo economicus: behavioral experiments in 15 small-scale societies. *AER*.
- Güth, W., Schmittberger, R. & Schwarze, B. (1982). An experimental analysis of ultimatum bargaining. *JEBO*.
- Tversky, A. & Kahneman, D. (1981). The framing of decisions and the psychology of choice. *Science*.
- Oprea, R. (2024). Decisions under risk are decisions under complexity. *AER*.
- Ledyard, J. O. (1995). Public goods: a survey of experimental research. In *Handbook of Experimental Economics*.
- Persky, J. (1995). Retrospectives: The ethology of Homo economicus. *Journal of Economic Perspectives*.
- Nowak, M. A. & Sigmund, K. (1993). A strategy of win-stay, lose-shift that outperforms tit-for-tat in the Prisoner's Dilemma game. *Nature*.
- Wu, J. & Axelrod, R. (1995). How to cope with noise in the iterated Prisoner's Dilemma. *Journal of Conflict Resolution*.
