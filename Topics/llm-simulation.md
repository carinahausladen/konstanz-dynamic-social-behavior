# Lecture Notes: Human Behavior Simulation with LLMs

- Lecture notes
  - Human behavior simulation with LLM agents: what is feasible today vs. still speculative.
  - Technical design choices: prompts, memory/state, tools, and reward signals.
  - Data and modeling assumptions: how training data shapes behavior.
  - Ethics in practice: privacy, consent, bias, manipulation, and transparency.
  - Evaluation and reproducibility: benchmarks, failure modes, and reporting standards.
 
In 2023, Park et al. introduced a seminal paper in which a small society of LLM-based agents was simulated. A key innovation was the modeling of “brain-like” memory architectures—short-term memory, long-term memory, and reflection processes—implemented through LLMs. The resulting agents displayed coherent and temporally extended social behavior. Shortly thereafter, Altera AI extended this approach by simulating long-term societal evolution within the virtual environment Minecraft. These simulations included the emergence and transformation of shared structures such as religion, language, and cooperation patterns. More recently, Moltbook demonstrated how entire social media ecosystems can be modeled using interacting LLM-based agents.
At the same time, industry actors have entered this field at scale. Simile AI, for example, recently received $100 million in seed funding to develop a “foundation model capable of predicting human behavior across products and situations.” The magnitude of such investments illustrates the strategic importance increasingly attributed to behavioral simulation technologies.

## Readings

- [Simulating Human Behavior with Large Language Models (2023)](https://arxiv.org/abs/2304.03442)  
  🎧 ~1:10:00

- [Terra AI: LLM Agents in a Minecraft Environment (2024)](https://arxiv.org/abs/2411.00114)  
  🎧 ~1:00:00

- [HumanLM (Stanford) (2024)](https://humanlm.stanford.edu/index.html)  
  🎧 ~1:15:00

- [Simile AI platform (2025)](https://simile.ai)  
  🎧 ~0:30:00

- [LLM Agent Papers Tracker (ongoing)](https://github.com/zjunlp/LLMAgentPapers)  
  🎧 ~0:30:00

## Datasets for Projects

- **PersonaChat** (dialogue with user profiles):  
  [Hugging Face](https://huggingface.co/datasets/personachat)

- **EmpatheticDialogues** (emotion-rich conversations):  
  [Hugging Face](https://huggingface.co/datasets/empathetic_dialogues)

- **DailyDialog** (human daily conversation dataset):  
  [Hugging Face](https://huggingface.co/datasets/daily_dialog)

- **MELD** (emotion + dialogue + multimodal context):  
  [GitHub](https://github.com/declare-lab/MELD)

- **SWDA / Switchboard-derived dialogue acts** (classic conversation behavior baseline):  
  [Hugging Face](https://huggingface.co/datasets/swda)
