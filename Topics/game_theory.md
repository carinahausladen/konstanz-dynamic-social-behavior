# Game Theory

## Motivation: LLMs in Strategic Environments

LLMs are increasingly being deployed in **strategic, multi-agent environments**, including Financial markets (e.g., trading agents like [Taurig Research](https://github.com/taurig-research)) and Cybersecurity (e.g., adversarial simulations).  

This illustrates that LLMs are increasingly becoming active participants in strategic and economic systems.
To study such environments formally, we turn to **game theory**, which provides a mathematical framework for analyzing strategic interaction.

Game theory allows us to test whether LLM-based agents can:

- Reason strategically in multi-agent settings  
- Understand incentives and payoffs  
- Predict other agents’ actions  
- Choose between cooperation and competition in a rational way  

In this sense, game theory acts as a **diagnostic tool** for evaluating LLM capabilities beyond language.

---

## Human Behavior in Strategic Settings

Measuring how people behave in repeated interactions, for example, how they cooperate and coordinate, is the subject of behavioural game theory. While traditional game theory assumes that people’s strategic decisions are rational, selfish and focused on utility maximization, behavioural game theory has shown that human agents deviate from these principles and, therefore, examines how their decisions are shaped by social preferences, social utility and other psychological factors. 

Studies of behavioral game theory demonstrate that choices are not always rational and do not always represent the utility maximizing choice.


The core categories of games can be summarized as follows:

| **Category**                   | **Main Idea**                                              | **Example Games**                                    |
| ------------------------------ | ---------------------------------------------------------- | ---------------------------------------------------- |
| **Coordination Games**         | Players benefit from matching choices; multiple equilibria | Battle of the Sexes, Stag hunt, Coordination game    |
| **Social Dilemmas**            | Individual rationality leads to worse group outcomes       | Prisoner's Dilemma, Public goods, Traveler’s dilemma |
| **Zero-Sum Games**             | One player’s gain is another’s loss                        | Matching pennies, Rock-paper-scissors, Blotto games  |
| **Bargaining Games**           | Players negotiate how to divide resources                  | Ultimatum game, Dictator game, Nash bargaining game  |
| **Dynamic (Sequential) Games** | Order and timing of moves matter                           | Centipede game, Trust game, Pirate game              |

To understand these games better, we will play a public good game in the classroom.


There is a large literature of these games being played, and there are some canonical findings, and let's just look at the canonical findings of the social dilemma games.

The canonical findings:

- Initial cooperation is high (≈ 40–60% contributions in public goods)
- Decay over time without enforcement
- Strong heterogeneity of behavioral types (selfish types, conditional cooperators (largest group), altruists / free riders)
- Costly punishment increases cooperation
- Beliefs matter a lot (people respond to expectations)

The Leading Mechanisms to explain these behaviors are:

- Social preferences: inequity aversion dislike being worse off (envy) dislike being better off (guilt)
- Conditional cooperation: people are willing to contribute if others do.
- Reciprocity: Reward kindness, punish unkindness
- Norm enforcement: fairness norms, Strong cross-country variation
- Confusion / bounded reasoning: Some cooperation is mistakes or misunderstanding, especially early rounds.


Interesting Results on Cross-Country Comparisons  (Herrmann, Thöni, Gächter (2008)):

|                                                 | **High Cooperation** | **Medium Cooperation** | **Low Cooperation** |
| ----------------------------------------------- | -------------------- | ---------------------- | ------------------- |
| **Punish free riders (pro-social punishment)**  | Switzerland, Germany | United States          | —                   |
| **Low punishment (norms internalized)**         | Denmark              | Japan                  | —                   |
| **Anti-social punishment (punish cooperators)** | —                    | Saudi Arabia, Oman     | Greece, Russia      |


Another important concept to have heard about is the **Nash equilibrium**: A situation where no player can improve their outcome by changing their strategy, given what everyone else is doing.

In the Prisoner's Dilemma:

- Initial choice: P1: *C*ooperate P2: *D*efect;
- Rationale: If the other cooperates → you prefer to defect; If the other defects → you still prefer to defect
- No one wants to change → Nash equilibrium = (D, D)



## LLMs in Strategic Settings

Behavioural game theory lends itself well to studying the repeated interactions of diverse agents
Recently, this literature has been extended to LLMs:

LLMs are deployed in classic experimental setups. This allows for two goals: First, to test whether LLMs replicate, deviate from, or fail to match human behavior. And second it is a form of AI evaluation.

For example, a repeatedly posed critique in this literature is the following:

> “LLMs fail miserably at the Ultimatum Game once you strip away textbook phrasing…  
> They either play hyper-rationally ($1 offer) or rigid 50/50 because of RLHF ‘niceness.’  
> What they aren’t doing is simulating the opponent’s spite or fairness threshold...  
> They do not have Theory of Mind...  
> If we want AI agents to negotiate real-world contracts, they need to understand human spite and bluffing...”  
> — @docdrayai (Apr 2026)


Thus, a central concept in this discussion is **Theory of Mind (ToM)** — the ability to attribute beliefs, intentions, and preferences to others. 
Humans use ToM to anticipate behavior in strategic settings.
It remains unclear whether LLMs truly possess this capability or merely approximate it through pattern recognition.


An interesting recent initiative in this space is the **Mind Game Challenge**, a NeurIPS 2025 workshop.
Teams could deploy their LLMs in the [Mind Games Arena](https://www.mindgamesarena.com) in four different games (e.g. Secret Mafia, Iterated Prisoner's Dilemma).




## Resources 

- [Game Theory Meets Large Language Models: A Systematic Survey (2025)](https://arxiv.org/abs/2502.09053)

- [Can Large Language Models Serve as Rational Players in Game Theory? A Systematic Analysis (2024)](https://ojs.aaai.org)

- [GTBench: Uncovering the Strategic Reasoning Capabilities of LLMs via Game-Theoretic Evaluations (2024)](https://neurips.cc)

- [Strategic Behavior of Large Language Models and the Role of Game Structure Versus Contextual Framing (2024)](https://www.nature.com/articles/s41598-024-69032-z)

- [Playing Repeated Games with Large Language Models (2025)](https://www.nature.com/articles/s41562-025-02172-y)

- [A foundation model to predict and capture human cognition (2025)](https://www.nature.com/articles/s41586-025-09215-4)
- [Could machine learning help to build a unified theory of cognition? (2025)](https://www.nature.com/articles/d41586-025-02353-9)


- [ALYMPICS: LLM Agents Meet Game Theory (2025)](https://aclanthology.org/2025.coling-main.193/)

- [Will Systems of LLM Agents Cooperate: An Investigation into a Social Dilemma (2025)](https://arxiv.org/pdf/2501.16173)

- [The MindGames Challenge: Theory-of-Mind and Game Intelligence in LLM Agents (2025)](https://neurips.cc/virtual/2025/loc/san-diego/competition/127731); This is a series of videos+slides. The presenter should focus on the **first two talks only**.

- [LARGE LANGUAGE MODELS AS SIMULATED ECONOMIC AGENTS: WHAT CAN WE LEARN FROM HOMO SILICUS(2026)](https://www.nber.org/system/files/working_papers/w31122/w31122.pdf)


# Methods

Next, we will focus on methodological approaches related to this literature.
One important strand of methods concerns the analysis of behavioral data generated in human experiments. 

In particular, we will study techniques such as **dynamic time warping** and **clustering**, which allow us to identify patterns and similarities in how individuals behave over time in strategic interactions.

These methods help us move beyond aggregate outcomes and instead uncover structured behavioral types and trajectories within games.


### Optional Readings

- [Clustering: Science or art? (2012)](https://proceedings.mlr.press/v27/luxburg12a/luxburg12a.pdf)
- [What are the true clusters? (2015)](https://doi.org/10.1016/j.patrec.2015.04.009) 


### Datasets for Projects

These are public datasets with data from human participants
- [Dal Bó & Fréchette (2018)](https://www.jstor.org/stable/pdf/26417201) — 103 sessions, 1,734 subjects, 116,644 observations
- [Bigoni et al. (2024)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4809158) — 27 sessions, 598 subjects, 60,334 observations
- [Embrey et al. (2018)](https://academic.oup.com/qje/article/133/1/509/4095199) — 27 sessions, 552 subjects, 65,720 observations
- [Mazur et al. (2025)](https://github.com/lechmazur/pgg_bench) — public goods cooperation benchmark
