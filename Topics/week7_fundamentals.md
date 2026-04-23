# Chapter 7 — Designing Institutions, Governing Commons, Learning Together

*A companion to Week 7 of the Konstanz seminar on Dynamic Social Behavior. The week asks whether computational systems can help us **design rules that make humans cooperate better**, and what happens when groups use information collectively to decide under uncertainty. Two of the three papers sit in the PNAS 2024–2025 *Collective Artificial Intelligence and Evolutionary Dynamics* special feature; the third is its immediate cousin in *Nature Communications*.*

---

## Reading Guide

- 🟦 **Koster, Tacchetti et al. (2024)** — *Deep Mechanism Design: Learning Social and Economic Policies for Human Benefit.* PNAS 2024. Programmatic paper on using deep RL to design auctions, redistribution schemes, and voting rules.
- 🟩 **Koster, Pîslar, Tacchetti et al. (2025)** — *Deep reinforcement learning can promote sustainable human behaviour in a common-pool resource problem.* *Nature Communications*. An RL-designed redistributive mechanism for an iterated multiplayer trust game, with an emphasis on interpretability and human popularity.
- 🟪 **Suganuma, Katahira, Ohtsuki & Kameda (2025)** — *How social learning enhances — or undermines — efficiency and flexibility in collective decision-making under uncertainty.* PNAS 2025. Agent-based analysis of individual vs. social learning strategies; mixed populations as adaptive.

A paper-to-concept index closes the chapter.

---

## 1. The institution problem

Before mechanism design, before deep learning, the question was already there. **Thomas Hobbes** (*Leviathan*, 1651) asked how order could arise among self-interested agents whose natural state was conflict. His answer — a sovereign — was political. **Adam Smith** (*The Wealth of Nations*, 1776) offered a different answer: an **invisible hand**, a set of background rules under which individual self-interest was metabolized into collective prosperity. **David Hume** (*A Treatise of Human Nature*, 1739) had already glimpsed the mechanism: conventions of property and contract, emerging from repeated interaction, create the possibility of trust.

The modern reformulation of this problem is **mechanism design**. Given a population of agents with preferences and private information, and a desired collective outcome, **what rules should the institution have** so that agents acting in their own interests produce the outcome we want? This is the question Leonid Hurwicz posed in the 1960s, for which he, Eric Maskin, and Roger Myerson received the Nobel Prize in 2007.

The Week 7 papers extend the question in two directions.

🟦 🟩 **Deep mechanism design** replaces the analyst with an optimizer. Rather than solving for an incentive-compatible mechanism in closed form, a neural network searches the space of mechanisms and finds one that performs well on a simulated population. The question is no longer *what does theory say the best rule is* but *what rule does the search find*.

🟪 **Collective learning under uncertainty** asks a complementary question from the side of the agents rather than the institution. When agents can learn individually or by copying others, when does the group as a whole decide well, and when does it lock into bad equilibria?

Both moves are deeply continuous with the social-science tradition, and both become legible when read with Hobbes, Smith, Hume, Hurwicz, and (most of all) Ostrom in view.

---

## 2. Mechanism design, stated compactly

The classical formulation. We have a set of agents; each has a type (private information about preferences, endowments, or beliefs). The designer chooses a **mechanism** — a rule that takes reported types and produces an outcome (an allocation, a decision, a transfer). The designer's goal is to pick a mechanism that, when agents play the game the mechanism induces, yields a socially desirable outcome.

The complications that animate the field:

- **Strategic reporting.** Agents will not always report their types truthfully; the mechanism must anticipate this.
- **Incentive compatibility.** A mechanism is **IC** if truthful reporting is a best response. The strongest form is **dominant-strategy IC** — truth-telling is optimal regardless of what others do. A weaker form is **Bayesian IC** — truth-telling is optimal in expectation over others' types.
- **Individual rationality.** Agents must be willing to participate; the mechanism must leave them at least as well off as not participating.
- **The revelation principle (Myerson 1979).** Any outcome achievable by any mechanism is achievable by a direct mechanism in which agents truthfully report types. This simplifies the design problem dramatically.

Two canonical mechanisms:

- **Vickrey (1961) second-price auction.** The highest bidder wins and pays the second-highest bid. Truth-telling is a dominant strategy. This is the minimal, elegant example of incentive-compatible design.
- **Vickrey-Clarke-Groves (VCG).** Generalizes the second-price auction to settings with multiple goods and externalities; remains IC under quasilinear preferences.

And two foundational impossibility results students should know as **constraints**, not as theorems to prove:

- **Arrow's impossibility theorem (1951).** No rule for aggregating individual rankings into a social ranking satisfies all of: universal domain, non-dictatorship, Pareto, independence of irrelevant alternatives, when there are three or more alternatives.
- **Gibbard-Satterthwaite (1973/75).** Any non-dictatorial voting rule defined over three or more alternatives is manipulable — there exist situations in which some agent can benefit by misreporting preferences.

These results tell us that the mechanism designer is always making trade-offs. There is no rule that does everything. The modern response — present in 🟦 — is to optimize explicitly for the trade-offs we care about, rather than to hope that a closed-form solution exists.

---

## 3. From analytic to learned mechanisms

The move in 🟦 is to replace the analyst's derivation with a **neural network trained by reinforcement learning**. The network produces candidate mechanisms; a simulated population plays the game; the designer updates the network toward mechanisms that score well on whatever welfare criterion has been specified.

The epistemic status of the output is different from a classical mechanism-design proof.

- A classical proof tells us the mechanism is optimal under specified assumptions — typically strong ones about agent rationality, utility structure, and information.
- A learned mechanism tells us the mechanism performed well in simulation. Whether it generalizes depends on whether the simulated agents were faithful models of real ones. This is the **simulation-to-real** (sim-to-real) transfer question, and it is where most of the methodological weight lands.

🟦 reports one such case in the voting setting: an AI-designed mechanism outperforms majoritarian baselines both on welfare metrics and on popular support among human participants. The paper is careful about the limits; readers should be too. **The fact that an optimizer found a mechanism is not the same as the fact that the mechanism is fair, or legitimate, or robust to the behaviors that the simulation did not model.** This is the central open question.

The social-science reading: **this is computational Hurwicz**. It is continuous with the discipline's seventy-year investigation of institutional design, with a new instrument. It is not a disruption to the field; it is the field's tooling evolving.

---

## 4. Commons, public goods, and collective action

The second half of the week's institutional question concerns not designed markets and auctions but **shared resources**.

**Hardin (1968, *Science*)** wrote "The Tragedy of the Commons": a common pasture, individually rational grazing decisions, collective ruin. The article entered the public vocabulary and for decades was cited as proof that shared resources required either privatization or top-down regulation. No middle path, said Hardin.

**Elinor Ostrom** spent her career showing that Hardin was wrong about the empirics. In *Governing the Commons* (1990), Ostrom documented dozens of cases — alpine pastures, Japanese fisheries, Philippine irrigation systems — in which communities had managed common-pool resources sustainably for centuries, **without privatization and without central authority**. Ostrom received the Nobel Prize in Economics in 2009 (the first woman to do so) for this body of work.

Ostrom's **eight design principles** for durable commons governance — clear boundaries, rules matched to local conditions, participatory rule-change, effective monitoring, graduated sanctions, conflict-resolution mechanisms, recognized rights to organize, and nested enterprises — are not universal laws but empirical regularities distilled from the cases. They have stood up remarkably well under subsequent scrutiny (Cox, Arnold & Tomás 2010; Poteete, Janssen & Ostrom 2010).

**Olson (1965, *The Logic of Collective Action*)** is the canonical theoretical treatment of why large groups under-provide public goods — selective incentives and group size as the key parameters. **Samuelson (1954)** formalized the distinction between public and private goods in welfare economics. Together, Olson, Samuelson, Hardin, and Ostrom constitute the intellectual backbone of the field.

🟩 sits squarely in this territory. An iterated multiplayer trust game with a common pool is a canonical **CPR dilemma**. The RL-designed planner that allocates returns to sustain contributions is, in Ostrom's vocabulary, a **monitoring and sanctioning institution** — specifically, a redistributive one. That the paper's best-performing policy resembles a progressive tax-and-transfer scheme is itself a datum about what kinds of institutions sustain cooperation.

The paper's interpretability finding — that a simpler, explainable version of the RL policy is more popular with human players — connects to a separate but related literature. **Tyler (1990, *Why People Obey the Law*)** and the procedural-justice tradition argue that institutions are obeyed in part because they are seen as fair, and being seen as fair requires being legible. An algorithmic mechanism that cannot explain its reasoning may outperform a transparent one on welfare metrics and still lose on legitimacy — and the loss can eventually take the welfare with it. Students should take this as a **social-science constraint on mechanism design**, not as a nice-to-have.

---

## 5. Social dilemmas and altruistic punishment

The connecting tissue between mechanism design and commons work is the **social dilemma** family: situations in which individual rationality produces collective sub-optimality. The Prisoner's Dilemma is the 2-person case; the Public Goods Game is the n-person case; the Common Pool Resource game is the n-person case with a rival-but-non-excludable shared resource.

**Ledyard (1995)** surveyed the extensive experimental literature on public-goods games. The standard pattern: people contribute about half the efficient amount in one-shot PGGs, and contributions decay over repeated rounds without enforcement.

**Fehr & Gächter (2000, *Nature*)** established one of the most consequential results in experimental economics: the option to punish defectors at a personal cost — **altruistic punishment** — sustains cooperation at near-efficient levels, even though punishing is itself irrational from the punisher's narrow self-interest. The result reframes Hardin's dilemma: humans apparently come equipped with behavioral machinery that partially resolves it, though the machinery itself imposes costs.

🟩's mechanism is not a punishment scheme in the Fehr-Gächter sense — it redistributes rather than sanctions. But it is doing the same kind of work: an institutional correction to the individual incentive structure, imposed from outside the strategic interaction. Students should read it alongside Fehr-Gächter and ask in what respects the learned redistributive scheme is a computational discovery of a **better alternative** to punishment, and in what respects it is a **different kind** of institutional remedy.

---

## 6. Individual vs. social learning

🟪 pivots from institutional design to **how agents themselves learn**.

The central distinction is old. **Bandura (1977, *Social Learning Theory*)** argued that much human behavior is learned by observing others, not by direct reinforcement. The claim was radical in its moment because it cut against a strict behaviorist reading of learning. Three decades later, **Boyd & Richerson (1985, *Culture and the Evolutionary Process*)** and the subsequent cultural-evolution tradition (Henrich 2016, *The Secret of Our Success*; Mesoudi 2011) formalized social learning as an inheritance system: traits spread by imitation and teaching, with their own selection dynamics.

Why does this matter for collective decisions?

**Rogers (1988)** identified what is now called **Rogers' paradox**: if pure social learners free-ride on individual learners, and if social learning is cheaper, then at equilibrium social learning dominates — but in a changing environment, pure social learning produces average outcomes no better than pure individual learning, because no one is tracking the world. Subsequent work (Enquist, Eriksson & Ghirlanda 2007) showed that the paradox dissolves under frequency-dependent payoffs or strategic use of social information, but the phenomenon is robust enough to matter.

**Henrich & Boyd (1998)** and **Laland (2004)** distinguished **social-learning strategies**: copy-when-uncertain, copy-the-successful, copy-the-majority (conformist transmission), copy-kin. **Rendell et al. (2010, *Science*)** ran a tournament to see which strategies won; the robust finding was that conditional copying — especially **copy-when-uncertain** and **copy-the-successful** — dominated.

🟪 extends this lineage into a reinforcement-learning framework with environmental volatility as the key parameter. Their result — that **mixed populations of individual and social learners are adaptive across regimes** — is computationally consistent with the cultural-evolution literature's pattern. In stable environments, social learners dominate; in volatile environments, individual learners do; mixed populations can survive both because they bring complementary information. The paper's innovation is to show this as an explicit ESS-style result within a deep-RL modeling framework.

The social-science reading: **this is a PNAS-era restatement of the Rendell-et-al. tournament**, updated with the mathematics of reinforcement learning and with the additional variable of environmental non-stationarity. Students who've seen the cultural-evolution literature will see a direct descendant; students who haven't should treat this paper as their entry point to it.

---

## 7. Wisdom of crowds and its limits

The collective-decision question that 🟪 inherits also has a distinct lineage in **statistical** and **political** thought.

**Condorcet's jury theorem (1785)** is one of the oldest results in social-choice theory. If each juror is more likely than chance to vote correctly on a binary question, and votes are independent, then the majority vote converges to the correct answer as the jury grows. The theorem is the mathematical backbone of democratic epistemology; it is why we count votes.

**Galton (1907, *Nature*)** reported an even more vivid empirical result. At a country fair, the mean of 787 individual guesses at the weight of an ox was accurate to within 1%. **Surowiecki (2004, *The Wisdom of Crowds*)** popularized the category. Under conditions of independence, diversity, and appropriate aggregation, crowds can outperform individual experts.

The negative results are just as important.

**Bikhchandani, Hirshleifer & Welch (1992, *Journal of Political Economy*)** introduced **information cascades**: when agents act sequentially and observe one another, a small number of early signals can drive later agents to ignore their private information, producing **herd behavior** that may settle on the wrong answer with high confidence. The model explains fads, bubbles, and failures of deliberation.

**Lorenz et al. (2011, *PNAS*)** showed experimentally that even mild social influence reduces the accuracy of crowd estimates by eroding the independence that makes crowds wise in the first place.

🟪's paper is explicitly about this trade-off. Social learning enhances efficiency in stable contexts and undermines flexibility in volatile ones. The coexistence of individual and social learning preserves both. Readers should hold Condorcet, Galton, Bikhchandani, and Lorenz simultaneously in view; the paper is not a departure from any of them but a synthesis.

---

## 8. Simulation, legitimacy, and the governance question

Two closing threads that cut across the week's readings.

**Simulation as policy design.** The 🟦 and 🟩 papers are making a methodological wager: that reinforcement learning over simulated populations can produce institutions worth deploying in real ones. The wager is not new — it is the **computational social science** wager (Lazer et al. 2009, *Science*) — but it is being made with new confidence, and in new domains. The social-science question remains: **how much can a simulation tell us about institutions before the institutions must face humans?**

**Legitimacy and interpretability.** The 🟩 result that an interpretable mechanism outperforms an opaque one in human popularity is a clue about the deployment frontier. Institutions in real societies are evaluated not only on what they produce but on whether their production is legible. This connects to a broader literature on **algorithmic accountability** (Binns 2018; Rahwan 2018; Selbst et al. 2019) and to **deliberative democracy** (Habermas; Fishkin), which argues that governance requires a certain kind of justifiable reasoning. A mechanism that cannot explain itself is, in this tradition, not a full institution.

The governance question the week raises is therefore **whose welfare function the mechanism optimizes**. A designer who specifies the welfare target has made a political choice — utilitarian, Rawlsian maximin, or something in between — and no amount of optimization can dissolve that choice. **Arrow's impossibility** and **Sen's Paretian liberal** (1970) remind us that aggregating preferences is never mechanical. Students should see this as the ineliminable political kernel at the center of a highly technical week.

---

## Paper-to-concept reading map

- 🟦 **Koster, Tacchetti et al. — Deep Mechanism Design.** Bring §1 (the institution problem from Hobbes to Hurwicz), §2 (classical mechanism design with IC and impossibility results), §3 (learned vs. analytic mechanisms; sim-to-real question), §8 (legitimacy, welfare-function politics). The central debate is whether a learned mechanism is a better designer or a displacement of the design question onto the optimizer and its welfare target.
- 🟩 **Koster et al. — Sustainable CPR.** Bring §4 (Hardin, Ostrom, Olson; CPRs and commons governance), §5 (social dilemmas and Fehr-Gächter altruistic punishment as alternative mechanism), §8 (interpretability, procedural justice, Tyler on legitimacy). The central debate is whether the RL-designed redistributive policy is a computational discovery or a restatement of an Ostrom-style arrangement.
- 🟪 **Suganuma et al. — Social Learning.** Bring §6 (individual vs. social learning; Boyd-Richerson, Rogers' paradox, Rendell-et-al. tournament), §7 (wisdom of crowds; Condorcet, Galton, Bikhchandani cascades, Lorenz erosion of independence). The central debate is whether the mixed-population ESS is a novel computational finding or a confirmation — in new formalism — of patterns the cultural-evolution literature has been reporting for decades.

---

## Further reading from the social sciences

- Hurwicz, L. (1960). Optimality and informational efficiency in resource allocation processes. In *Mathematical Methods in the Social Sciences*.
- Myerson, R. B. (1979, 1981). Incentive compatibility and the bargaining problem; Optimal auction design.
- Maskin, E. (1999). Nash equilibrium and welfare optimality. *Review of Economic Studies*.
- Vickrey, W. (1961). Counterspeculation, auctions, and competitive sealed tenders. *Journal of Finance*.
- Arrow, K. J. (1951). *Social Choice and Individual Values*. Wiley.
- Gibbard, A. (1973). Manipulation of voting schemes. *Econometrica*. Satterthwaite, M. (1975). Strategy-proofness and Arrow's conditions. *JET*.
- Sen, A. K. (1970). The impossibility of a Paretian liberal. *Journal of Political Economy*.
- Hardin, G. (1968). The tragedy of the commons. *Science*.
- Ostrom, E. (1990). *Governing the Commons*. Cambridge UP.
- Ostrom, E. (2009). Beyond markets and states: Polycentric governance of complex economic systems. Nobel lecture.
- Olson, M. (1965). *The Logic of Collective Action*. Harvard UP.
- Samuelson, P. A. (1954). The pure theory of public expenditure. *Review of Economics and Statistics*.
- Ledyard, J. O. (1995). Public goods: A survey of experimental research. In *Handbook of Experimental Economics*.
- Fehr, E. & Gächter, S. (2000). Cooperation and punishment in public goods experiments. *AER*; also (2002) *Nature*.
- Berg, J., Dickhaut, J. & McCabe, K. (1995). Trust, reciprocity, and social history. *Games and Economic Behavior*.
- Bandura, A. (1977). *Social Learning Theory*.
- Boyd, R. & Richerson, P. J. (1985). *Culture and the Evolutionary Process*. Chicago UP.
- Henrich, J. (2016). *The Secret of Our Success*. Princeton UP.
- Rogers, A. R. (1988). Does biology constrain culture? *American Anthropologist*.
- Rendell, L. et al. (2010). Why copy others? Insights from the social learning strategies tournament. *Science*.
- Condorcet, M. de (1785). *Essai sur l'application de l'analyse à la probabilité des décisions rendues à la pluralité des voix*.
- Galton, F. (1907). Vox populi. *Nature*.
- Surowiecki, J. (2004). *The Wisdom of Crowds*.
- Bikhchandani, S., Hirshleifer, D. & Welch, I. (1992). A theory of fads, fashion, custom, and cultural change as informational cascades. *JPE*.
- Lorenz, J., Rauhut, H., Schweitzer, F. & Helbing, D. (2011). How social influence can undermine the wisdom of crowd effect. *PNAS*.
- Tyler, T. R. (1990). *Why People Obey the Law*. Yale UP.
- Lazer, D. et al. (2009). Computational social science. *Science*.
