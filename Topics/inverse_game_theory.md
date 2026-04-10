# Beyond LLMs: Building World Models with Reinforcement Learning, Inverse Game Theory, and Applications to Social Dilemmas

**Fei-Fei Li** describes LLMs as “eloquent but ungrounded” — powerful at generating language, but lacking true spatial intelligence rooted in perception and action.  
  > “Language is purely generated signal. You don’t go out in nature & there’s words written in the sky for you. There is a 3D world that follows laws of physics.”

**Yann LeCun** repeatedly calls LLMs a potential “dead end” for human-level intelligence, emphasizing that children learn from ~10¹⁵ bytes of visual/sensory data, far exceeding the textual training of even the largest models.  
  > “Your house cat is way smarter than the biggest LLMs — we still lack domestic robots, fully autonomous cars, and systems with true physical understanding.”

Both researchers strongly advocate moving toward **world models** — rich, simulatable internal representations of reality that go far beyond text.



Reinforcement learning (RL) is one of the most promising technologies for building these grounded world models. RL agents learn by interacting with environments, optimizing long-term rewards through trial and error — exactly the kind of adaptive, embodied learning needed for robotics and real-world decision-making.
Boston Dynamics’ robots use RL as do autonomous driving systems (e.g., Waymo) .
While we do not work directly in robotics, the principles and tools of RL transfer powerfully to the social sciences.



Multi-agent reinforcement learning (MARL) has become a major tool for studying **social dilemmas**.
Agents learn policies in simulated environments that mirror real-world incentive structures, revealing emergent behaviors such as:
- When and how cooperation arises
- The impact of communication, punishment, reputation
- The effectiveness of policy interventions
This line of work has a long history (Camerer & Ho 1999, early iterated PD studies) but has exploded with deep RL since ~2017.



A closely related and rapidly growing field is **inverse game theory** (also connected to inverse reinforcement learning / IRL).
Instead of predicting behavior from known payoffs → inverse game theory **infers the hidden utilities / rewards / rationality parameters** that best explain observed actions or equilibria.
Applications include:
- Decoding strategic preferences in economic games
- Understanding human or AI agent behavior in social dilemmas
- Designing mechanisms by reverse-engineering incentives


### Resources

- [Learning to Resolve Social Dilemmas: A Survey (2024)](https://dl.acm.org/doi/abs/10.1613/jair.1.15167)
- [Multi-agent reinforcement learning in sequential social dilemmas (2017)](https://arxiv.org/abs/1702.03037)
- [Reinforcement learning in a prisoner’s dilemma (2024)](https://doi.org/10.1016/j.geb.2024.01.004)
- [Deep mechanism design: Learning social and economic policies for human benefit (2024)](https://www.pnas.org/doi/10.1073/pnas.2319949121)
- [Deep reinforcement learning can promote sustainable human behaviour in a common-pool resource problem (2025)](https://doi.org/10.1038/s41467-025-58043-7)
- [Collective artificial intelligence and evolutionary dynamics (2025)](https://www.pnas.org/doi/pdf/10.1073/pnas.2505860122)
- [How social learning enhances—or undermines—efficiency and flexibility in collective decision-making under uncertainty (2025)](https://www.pnas.org/doi/epub/10.1073/pnas.2516827122)
- [Scaffolding cooperation in human groups with deep reinforcement learning (2023)](https://www.nature.com/articles/s41562-023-01686-7)
-[Human-level play in the game of Diplomacy by combining language models with strategic reasoning (2022)](https://www.science.org/doi/10.1126/science.ade9097)
- [Language Agents with Reinforcement Learning for Strategic Play in the Werewolf Game](https://arxiv.org/pdf/2310.18940)

#### Optional Foundations
- [Experience-weighted attraction learning in normal form games (1999)](https://doi.org/10.1111/1468-0262.00054)
- [Prosocial learning agents solve generalized Stag Hunts better than selfish ones (2017)](https://arxiv.org/abs/1709.02865)
- [Learning with opponent-learning awareness (2018)](https://arxiv.org/abs/1709.04326)


Another interesting course on the topic can be found [here](https://docs.google.com/spreadsheets/d/1G0UNG6TewBS1PzNrW3JNs9h-1eLs-UqqcJ8wQYEE5JM/edit?gid=0#gid=0).