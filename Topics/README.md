# Dynamic Social Behavior — A Companion Book

*Companion reading for the Konstanz seminar on **Dynamic Social Behavior** (Spring 2026). These chapters introduce the ideas behind the seminar's papers from a social-science vantage point, so that the computational literature reads as a continuation of a long tradition rather than a break from it.*

---

## About this book

Each chapter corresponds to one week of the seminar. It introduces, in book-chapter form, the concepts needed to read that week's papers with comprehension — starting from the social-science tradition (Schelling, Durkheim, Lewis, Bicchieri, Ostrom, Hurwicz, Schelling again, Gneezy, Boyd & Richerson, Condorcet, Galton, Bikhchandani, and many more) and bridging to the computational work at the edge of the field.

The chapters are written for a reader who already carries a reasonable load of social-science knowledge, and who would like an honest map of how the recent wave of LLM- and RL-based research on social behavior connects to what social science has long known.

---

## Chapters

- **[Chapter 2 — Game Theory as a Diagnostic Language](week2_fundamentals.md)** — The vocabulary for studying strategic behavior: normal-form games, Nash equilibrium, the 2×2 social-dilemma taxonomy, repeated games, social preferences, and the behavioral-GT tradition. *Papers: Horton; Lorè & Heydari; Akata; Sun.*
- **[Chapter 3 — Rationality, Cognition, and the Validity Question](week3_fundamentals.md)** — Decomposing rationality into desire, belief, and refinement; the cognitive-science tradition (Newell & Simon, ACT-R, Marr); evolutionary game theory; and the methodological critique of LLMs as stand-ins for human subjects. *Papers: Fan; Binz (Centaur); Willis; Kozlowski & Evans.*
- **[Chapter 4 — Simulating People](week4_fundamentals.md)** — Silicon sampling, agent architectures (memory, reflection, planning), the validity typology (Campbell & Stanley; Cronbach & Meehl), WEIRD-sample critique, prompt framing as question-wording, and forecasting social-science experiments. *Papers: Park 2023 (Smallville); Park 2024 (1,000 People); Hewitt; Anthis.*
- **[Chapter 5 — Emergent Societies](week5_fundamentals.md)** — Durkheim on social facts, Schelling on emergence, Lewis conventions vs. Bicchieri norms, tipping points and committed minorities (Centola), homophily and echo chambers (McPherson; Bakshy; Guess; Bail), and simulation as a policy sandbox. *Papers: Altera (Project Sid); Ashery; Larooij & Törnberg.*
- **[Chapter 6 — Strategic Games: Deception, Negotiation, Theory of Mind](week6_fundamentals.md)** — Bayesian games (Harsanyi), cheap talk (Crawford & Sobel), signaling (Spence), Bayesian persuasion (Kamenica & Gentzkow), Schelling commitment, theory of mind (Premack & Woodruff; Wimmer & Perner), deception (Gneezy; Bok; Goffman; Simmel), and hybrid LLM+RL architectures. *Papers: Xu (Werewolf); FAIR (CICERO).*
- **[Chapter 7 — Designing Institutions, Governing Commons, Learning Together](week7_fundamentals.md)** — Mechanism design from Hurwicz to deep RL; incentive compatibility; Arrow and Gibbard-Satterthwaite impossibility results; Hardin and Ostrom on commons; Fehr-Gächter altruistic punishment; social learning (Boyd & Richerson; Rogers' paradox; Rendell et al.); wisdom of crowds and its limits (Condorcet; Galton; Bikhchandani; Lorenz); legitimacy and procedural justice (Tyler). *Papers: Koster, Tacchetti et al. (Deep Mechanism Design); Koster et al. (Sustainable CPR); Suganuma et al. (Social Learning).*

---

## How to read

The chapters are organized **by concept, not by paper**. Inside each chapter, concepts appear in a pedagogical order that follows the social-science argumentative structure, and each concept names the papers that engage it. A **color-tagged reading guide** opens every chapter, and a **paper-to-concept reverse index** closes it, so that a student preparing to discuss a specific paper can pull the exactly-right sections.

The color tags are consistent across the book:
- 🟦 first-listed paper of the week
- 🟩 second
- 🟨 third
- 🟥 / 🟪 fourth (or an additional paper)
- 🧭 bridge / context paper (not a presenter's paper)

The tags are a navigation aid. Reading linearly — from §1 to the end of a chapter — is the recommended first pass; the reverse index is there for the second.

---

## What this book is not

It is not a replacement for the papers. It is an on-ramp. The papers themselves reward close reading, and the argument between them — what counts as a valid LLM subject, what emergence in an artificial population means, whether a learned institution is discovered or designed — cannot be resolved from a companion text.

It is also not a computer-science textbook. Engineering detail (transformer architecture, PPO implementation, retrieval-augmented generation internals) is elided where it is not load-bearing for the conceptual argument. Readers who want depth there will find excellent treatments elsewhere. This book takes the opposite commitment: **whenever a choice arose between depth in social science and depth in computer science, the social-science side was preferred.**

---

## Seminar context

The seminar, taught at the University of Konstanz in Spring 2026, brings together students from political science, sociology, economics, and cognitive science to study what recent advances in LLM- and RL-based modeling tell us about human social behavior — and what they do not.

Chapters cover Weeks 2 through 7 of the seminar. Week 1 is a course introduction; Week 8 is student synthesis; those weeks do not have a chapter here.

---

## A note on the author, the authors, and the conversation

These chapters were drafted in conversation between the instructor and an AI assistant. Where an AI assistant can be useful in pedagogy is by keeping a large corpus of social-science classics in working memory and drafting coherent connective tissue; where it cannot be useful is in *knowing* what a given cohort of students needs, which only the instructor does. Any place where this book reads well is the result of the instructor's editorial direction; any place it reads badly is a failure of that editorial loop and welcomes correction.

Corrections, pull requests, and discussions are welcome via the repository's issue tracker.
