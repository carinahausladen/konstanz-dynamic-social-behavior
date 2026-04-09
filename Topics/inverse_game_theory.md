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


### 📖 Key Readings 

- Köster, R., et al. (2025). *Deep reinforcement learning can promote sustainable human behaviour in a common-pool resource problem.* Nature Communications.  
  [DOI: 10.1038/s41467-025-58043-7](https://doi.org/10.1038/s41467-025-58043-7) (~19 min audio @ 1.5×)

- Tacchetti, A., et al. (2024). *Deep mechanism design: Learning social and economic policies for human benefit.* PNAS.  
  [DOI: 10.1073/pnas.2319949121](https://www.pnas.org/doi/10.1073/pnas.2319949121) (~26 min)

- Dolgopolov, A. (2024). *Reinforcement learning in a prisoner’s dilemma.* Games and Economic Behavior.  
  [DOI: 10.1016/j.geb.2024.01.004](https://doi.org/10.1016/j.geb.2024.01.004) (~32 min)

- Leibo, J. Z., et al. (2017). *Multi-agent reinforcement learning in sequential social dilemmas.* arXiv.  
  [arXiv:1702.03037](https://arxiv.org/abs/1702.03037) (~17 min)

- Virk, H., et al. (2025). *Blind Inverse Game Theory: Jointly Decoding Rewards and Rationality in Entropy-Regularized Competitive Games.* arXiv.  
  [arXiv:2511.05640](https://arxiv.org/abs/2511.05640) (~20 min estimated)

- IRL for AI Ethics. https://dkasenberg.github.io/inverse-reinforcement-learning-rescue/

Classic & foundational:
- Camerer & Ho (1999) → [DOI](https://doi.org/10.1111/1468-0262.00054)
- Peysakhovich & Lerer (2017) → [arXiv:1709.02865](https://arxiv.org/abs/1709.02865)
- Foerster et al. (2018) → [arXiv:1709.04326](https://arxiv.org/abs/1709.04326)

### Datasets & Environments for Hands-on Projects

These environments are excellent starting points for projects: train simple MARL agents, observe emergent cooperation/defection, perturb reward structures, or apply inverse methods to infer hidden preferences.

| Environment          | Description                                                                 | Source / Link                                                                 |
|----------------------|-----------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| Gathering Game       | Collect apples, but you can “zap” others — classic cooperation test         | [DeepMind / Leibo et al. 2017](https://arxiv.org/abs/1702.03037)              |
| Wolfpack             | Cooperative hunting — reward depends on surrounding prey together           | Same as above                                                                 |
| Melting Pot          | 50+ curated multi-agent social dilemma scenarios                            | [GitHub: google-deepmind/meltingpot](https://github.com/google-deepmind/meltingpot) |
| SocialJax            | Fast JAX-based sequential social dilemmas with strong baselines             | [OpenReview](https://openreview.net/forum?id=Qg6kHVN91t)                      |
| Iterated PD Variants | Moral agents, Stag Hunt, Volunteer’s Dilemma, etc.                          | [IJCAI 2023 paper & code](https://www.ijcai.org/proceedings/2023/0036.pdf)    |