# Chapter 6 — Strategic Games: Deception, Negotiation, Theory of Mind

*A companion to Week 6 of the Konstanz seminar on Dynamic Social Behavior. This chapter introduces the concepts behind machine play in games where strategy, deception, and natural-language negotiation are not decorations but the substance of the game.*

---

## Reading Guide

- 🟦 **Xu, Yu, Fang, Wang & Wu (2024)** — *Language Agents with Reinforcement Learning for Strategic Play in the Werewolf Game.* ICML 2024. LLM agents with RL for social-deduction play.
- 🟩 **FAIR Diplomacy Team, Meta (2022)** — *Human-level play in the game of Diplomacy by combining language models with strategic reasoning* (CICERO). *Science*. Top-10% play in anonymous online Diplomacy via planning + language-generation hybrid.

A paper-to-concept index closes the chapter.

---

## 1. Why Werewolf and Diplomacy

Games in which information is **complete** — chess, Go, checkers — have been defeated by machines for decades. The interesting remaining frontier is games in which (a) information is **incomplete**, (b) other players' **types** or roles are uncertain, and (c) some portion of the action is carried out in **natural language**. Werewolf and Diplomacy are the canonical testbeds for this frontier. They do not yield to pure search; they do not yield to pure language modeling; they yield — if at all — to hybrids that treat strategy and language as interacting systems.

The social-science interest is parallel. The field has studied both games as laboratories. Diplomacy has been used in political-science teaching for decades as a live experiment in alliance dynamics and commitment. Social-deduction games in the Werewolf family have been used in experimental economics to study deception, trust, and information revelation. What the computational papers do is add a new kind of player — a machine that talks — to long-running research programs.

---

## 2. The von Neumann inheritance and its limits

Modern game theory begins with **von Neumann & Morgenstern (1944, *Theory of Games and Economic Behavior*)**. Their framework — payoffs, strategies, equilibria — has structured the entire subsequent literature in economics, political science, and computer science. **Nash (1950)** proved that equilibria exist in a broad class of games; the concept has since done vast amounts of work across the disciplines.

The limitation, and the reason Werewolf and Diplomacy remain hard, is that the classical framework was developed primarily for **games of complete information**. When players do not know each other's types, and when the action includes **cheap talk**, the classical machinery needs extensions. Two of those extensions matter for this week.

**Harsanyi (1967–68)** introduced **Bayesian games**: each player has a type, drawn from a distribution common knowledge to all players, and conditions on their private type when choosing actions. Every Bayesian game has a Bayes-Nash equilibrium, at least in mixed strategies. Werewolf is structurally a Bayesian game — the type is your role (werewolf, seer, villager).

**Aumann (1976)** formalized **common knowledge**: something is common knowledge when everyone knows it, everyone knows everyone knows it, and so on up the hierarchy. Strategic reasoning in games of incomplete information depends on what is common knowledge and what is not. A werewolf player's ability to deceive depends on the common-knowledge structure: the werewolves know who they are; the villagers know only that they do not know.

Students do not need the formal mathematics. They need the **shape** of the machinery and the awareness that standard game-theoretic reasoning, without these extensions, does not apply to either of this week's games.

---

## 3. Cheap talk, signaling, and the limits of words

Why is it hard to communicate strategically? Because your listener has no guarantee that what you say is what you believe. This is the central question behind a cluster of foundational results.

**Crawford & Sobel (1982, *Econometrica*)** established the **cheap-talk** model. Sender has private information, receiver makes a decision; sender sends a message at no cost. When do the sender and receiver's interests overlap enough that the message is informative? The result is elegant: communication is informative only when preferences are sufficiently aligned. Pure adversaries cannot communicate informatively by cheap talk; pure allies always can.

**Spence (1973, *Quarterly Journal of Economics*)** introduced **signaling** with costly actions. An educational credential signals type because it is cheaper for a high-type agent to acquire than a low-type one. Signals are informative when their cost structure correlates with the underlying type.

**Akerlof (1970, *QJE*)**, the "lemons" paper, established the **asymmetric-information** framework: when one party knows more than another, markets can collapse. The paper won the 2001 Nobel; its insight applies to every strategic situation where one side knows more than the other, which is every situation in Werewolf and in Diplomacy.

**Kamenica & Gentzkow (2011, *American Economic Review*)** developed **Bayesian persuasion**: the sender commits to an *information policy* and then sends messages under that policy. Unlike cheap talk, the commitment makes the sender's words credible. CICERO's architecture — generating messages from plans, filtered by consistency — is close to a mechanized analogue of Bayesian persuasion with designed commitment.

**Schelling (1960, *The Strategy of Conflict*)** is the under-sung ancestor of much of this. Schelling thought about **commitment** as the foundation of strategic advantage: burning ships, doomsday machines, making your options visibly and credibly smaller so that your opponent has no choice but to accept your preferred outcome. Every move CICERO makes has a Schelling precursor, and students who read a single chapter of *Strategy of Conflict* (chapter 2 or 5 will do) will understand Diplomacy in a way no amount of computer-science exposition can supply.

The social-science lineage — von Neumann → Nash → Harsanyi → Schelling → Crawford-Sobel → Spence → Akerlof → Kamenica-Gentzkow — is the backbone of this chapter. All seven scholars have Nobel or Nobel-adjacent standing. The computational papers are playing in a field these scholars laid out.

---

## 4. Theory of mind

Premack & Woodruff (1978, *Behavioral and Brain Sciences*) asked "Does the chimpanzee have a theory of mind?" The phrase stuck. **Theory of mind** is the cognitive capacity to attribute mental states — beliefs, desires, intentions — to others, and to act on the attribution.

**Wimmer & Perner (1983, *Cognition*)** operationalized the question with the **false-belief task**: Sally puts a marble in a basket and leaves; Anne moves it to a box; Sally comes back; where will Sally look? A child who answers "the basket" has represented Sally's false belief; a child who answers "the box" has not. Around age four, most children pass the task. The test became the workhorse of developmental cognitive science.

**Higher-order theory of mind** recurses: I think that you think that I think... Kinderman, Dunbar & Bentall (1998) found that ordinary adults manage four or five levels of recursion reliably, with considerable individual variation. The Werewolf and Diplomacy settings require at least two levels of recursion as a matter of routine — "the werewolves know the villagers think X about them."

The question the Week 6 papers raise is whether LLMs have theory of mind in any robust sense. There is a lively literature with disagreement (Kosinski 2023; Ullman 2023; Shapira et al. 2024). The conservative reading is that LLMs pass some false-belief-like tasks and fail others in ways that suggest representation rather than pattern completion is uneven. The liberal reading is that whatever LLMs do, it is functionally sufficient to support some level of strategic play in games that require ToM. Werewolf and Diplomacy are the natural stress tests.

🟦 Xu et al.'s paper is the closest thing to a sustained empirical study of LLM-agent ToM in a competitive setting. 🟩 CICERO's ability to maintain plausible intent-consistent dialogue is, whatever else it is, a demonstration of ToM-like behavior at scale.

---

## 5. Deception as a social-science object

Deception is not the absence of honesty; it is a **strategic action** with its own literature.

**Bok (1978, *Lying: Moral Choice in Public and Private Life*)** distinguishes categories of untruth: bald lies, evasions, half-truths, strategic silences. These categories have consequences for evaluation.

**Gneezy (2005, *American Economic Review*)** built the behavioral-economics bridge. In a simple sender-receiver experiment, senders face a choice between honest and dishonest messages with different payoff consequences; the experimenter varies who gains and who loses. The paper established stable preferences: people dislike lying, dislike more strongly lies that hurt others, and will forgo material payoff to tell the truth. This is **aversion to lying** as a measurable parameter of human behavior.

**Goffman (1959, *The Presentation of Self in Everyday Life*)** provides the broader frame: social life is staged, and the performance of self is constantly managed. A Werewolf player maintaining the role of innocent villager is doing Goffmanian dramaturgy under high stakes. Goffman is worth reading in the Werewolf context not because he formalizes anything but because he makes visible the texture of what the game is about.

**Simmel (1906, *"The Sociology of Secrecy and of Secret Societies"*)** identified the **social structure of concealment** — how groups maintain, communicate, and leverage secrets. Werewolf is a purified Simmelian setting: one subset of the group knows something the other does not, and the game structure forces the secret into repeated communicative pressure.

Students should read the Werewolf LLM literature with this library at hand. The question of whether an LLM can "lie" dissolves into several more specific questions: can it pass as a role it is not? can it calibrate the cost and payoff of untruth? can it detect deception in others? These are measurable and distinct, and the Xu paper engages some of them explicitly.

---

## 6. Reinforcement learning, at the minimum

The Week 6 papers use reinforcement learning. A compact vocabulary suffices.

- **State** — the current configuration of the world relevant to the agent's decision.
- **Action** — a choice the agent can make.
- **Reward** — a scalar signal the environment returns to the agent, to be maximized over time.
- **Policy** — a rule mapping states to actions (or distributions over actions).
- **Value** — expected cumulative future reward from a state under a policy.

**Sutton & Barto (2018, *Reinforcement Learning: An Introduction*)** is the standard reference. The conceptual lineage in the social sciences is **Thorndike's law of effect** (1911) via **operant conditioning** (Skinner) and **Bush-Mosteller** (1955) stochastic learning theory; economists have used essentially equivalent formalisms under the name **reinforcement-based learning** in games (Roth & Erev 1995; Camerer & Ho 1999). The same mathematical shape has been in behavioral science for a century.

**Self-play** is the regime in which a reinforcement-learning agent trains by playing against prior versions of itself. It is how AlphaGo became better than any human (Silver et al. 2016, *Nature*) and how the Xu and CICERO agents are trained. The social-science analogue is **evolutionary game theory** (Maynard Smith 1982; Weibull 1995): strategies play against a population of strategies, and the population changes by selection.

**Policy gradient methods** — of which **PPO** (Proximal Policy Optimization; Schulman et al. 2017) is the workhorse used in Xu et al. — adjust the policy to increase the probability of actions that produced reward. Students do not need the gradient calculation; they need to know the agent improves by *rewriting its own tendencies*, not by searching a tree.

The conceptual bridge students should carry is: **reinforcement learning is a computational version of a behavioral-science idea that predates it by a century**. The novelty is the scale, not the principle.

---

## 7. Hybrid architectures: language meets strategy

Pure LLMs have a characteristic failure mode in strategic settings: they inherit **action biases** from training data. An LLM asked to play Rock-Paper-Scissors picks Rock far more than one-third of the time, because the word "rock" is more common in training text. The Xu paper's motivating diagnostic is exactly this kind of distributional leakage. Their architectural response is to use the LLM to *generate candidate reasoning and candidate actions*, and train an RL policy to *choose among candidates*.

This is a general pattern. CICERO does an analogous thing: a strategic-reasoning module produces **intents** (joint-action plans consistent with what the agent thinks will happen); a language model generates dialogue **conditioned on those intents**; a filter prunes utterances that are inconsistent with the plan. The language model does the talking; the planner does the strategizing; a constraint enforces that the talk does not contradict the plan. The result is the first system to reach top-10% performance in online Diplomacy against humans without being detected as a bot.

The methodological move — **use LLM for generation, use an explicit optimizer for selection** — is the single most generalizable lesson this week carries. It will recur in Week 7 (where an RL planner designs mechanisms over an LLM-shaped behavior space) and in the broader literature on agentic AI.

---

## 8. Turing-style evaluation in strategic settings

CICERO's survival in anonymous Diplomacy play, across a league of human competitors, is closer to a **Turing test** than most AI-evaluation results in recent years. The classical Turing test (Turing 1950, *Mind*) asked whether a machine could pass for human in natural-language conversation. A Diplomacy Turing test asks something harder: can a machine pass for human when the stakes include trust, betrayal, and sustained strategic relationship-building under pressure?

Social-science students should notice that this inherits from the **human-computer interaction** literature (Bainbridge; Nass & Moon's 2000 "ethopoeia" work) and from **behavioral Turing tests** in economics (e.g., Aher, Arriaga & Kalai 2023's use of LLMs to reproduce classic experiments). The common thread: **what does it mean to pass for human** depends on what channel you are being tested on.

🟩 CICERO's result is provocative because the channel is negotiation, and negotiation was supposed to be a protected human domain. The paper's more subtle contribution is methodological: it shows what a behavioral Turing test at scale can look like.

---

## 9. Alliances, reputation, and the shadow of the future

Two threads from social science especially structure Diplomacy play.

**Axelrod (1984, *The Evolution of Cooperation*)** established, through computer tournaments of the iterated Prisoner's Dilemma, that cooperation can emerge among self-interested agents under the **shadow of the future** — when interactions are sufficiently likely to recur that defection today costs cooperation tomorrow. Diplomacy is an extended form of this logic, with additional structure: alliances are multilateral, betrayal is asymmetric in cost, and the game ends.

**Kreps, Milgrom, Roberts & Wilson (1982, *Journal of Economic Theory*)** — the "Gang of Four" paper — showed how **reputation** supports cooperation even in finite repeated games. If you might be the kind of player who always cooperates, a rational opponent can cooperate with you longer than backward induction would suggest. Reputation is what CICERO must manage across the arc of a game.

**Snyder (1984, 1997)** and **Walt (1987)** developed alliance theory in international relations. Their distinctions — bandwagoning vs. balancing, alliance dilemmas, the risk of abandonment vs. entrapment — give a political-science vocabulary for what Diplomacy players (human and machine) are doing. For students with IR backgrounds, this is the natural bridge into the computational work.

---

## Paper-to-concept reading map

- 🟦 **Xu et al. — Werewolf.** Bring §2 (Bayesian games, common knowledge), §4 (theory of mind and false belief), §5 (deception as Gneezy-measurable behavior, Simmelian secrecy, Goffmanian performance), §6 (RL vocabulary and self-play), §7 (hybrid LLM + RL architecture). The central debate is whether the agent's behavior reflects representational theory of mind or pattern completion — and whether the distinction matters for competitive outcomes.
- 🟩 **FAIR — Diplomacy / CICERO.** Bring §3 (Crawford-Sobel cheap talk, Spence signaling, Kamenica-Gentzkow persuasion, Schelling commitment), §4 (theory of mind at scale), §7 (hybrid planner + language-model architecture), §8 (Turing-style evaluation in strategic settings), §9 (alliances, reputation, shadow of the future). The central debate is whether CICERO's success is a demonstration of general strategic-communicative competence or a demonstration of what is achievable with a carefully engineered constraint between plan and speech.

---

## Further reading from the social sciences

- von Neumann, J. & Morgenstern, O. (1944). *Theory of Games and Economic Behavior*. Princeton UP.
- Nash, J. (1950). Equilibrium points in n-person games. *PNAS*.
- Harsanyi, J. C. (1967–68). Games with incomplete information played by "Bayesian" players, I–III. *Management Science*.
- Aumann, R. J. (1976). Agreeing to disagree. *Annals of Statistics*.
- Schelling, T. C. (1960). *The Strategy of Conflict*. Harvard UP.
- Crawford, V. & Sobel, J. (1982). Strategic information transmission. *Econometrica*.
- Spence, M. (1973). Job market signaling. *QJE*.
- Akerlof, G. (1970). The market for "lemons". *QJE*.
- Kamenica, E. & Gentzkow, M. (2011). Bayesian persuasion. *AER*.
- Premack, D. & Woodruff, G. (1978). Does the chimpanzee have a theory of mind? *BBS*.
- Wimmer, H. & Perner, J. (1983). Beliefs about beliefs. *Cognition*.
- Goffman, E. (1959). *The Presentation of Self in Everyday Life*.
- Simmel, G. (1906). The sociology of secrecy and of secret societies. *AJS*.
- Bok, S. (1978). *Lying: Moral Choice in Public and Private Life*.
- Gneezy, U. (2005). Deception: The role of consequences. *AER*.
- Axelrod, R. (1984). *The Evolution of Cooperation*. Basic Books.
- Kreps, D. M., Milgrom, P., Roberts, J. & Wilson, R. (1982). Rational cooperation in the finitely repeated prisoners' dilemma. *JET*.
- Snyder, G. H. (1997). *Alliance Politics*. Cornell UP.
- Turing, A. M. (1950). Computing machinery and intelligence. *Mind*.
- Sutton, R. S. & Barto, A. G. (2018). *Reinforcement Learning: An Introduction*. MIT Press.
