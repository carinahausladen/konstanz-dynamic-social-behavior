# Chapter 4 — Simulating People

*A companion to Week 4 of the Konstanz seminar on Dynamic Social Behavior. This chapter introduces the ideas behind the week's readings from a social-science vantage point, so that the computational papers read as a continuation of a long tradition rather than a break from it.*

---

## Reading Guide

The week's four papers are tagged throughout this chapter. When a concept appears, its paper tags indicate where it does substantive work.

- 🟦 **Park et al. (2023)** — *Generative Agents: Interactive Simulacra of Human Behavior.* UIST '23. The 25-agent Smallville paper.
- 🟩 **Park et al. (2024)** — *Generative Agent Simulations of 1,000 People.* Interview-based simulation of real survey respondents.
- 🟨 **Hewitt et al. (2024)** — *Predicting Results of Social Science Experiments Using LLMs.* Forecasting treatment effects before (or instead of) running experiments.
- 🟥 **Anthis et al. (2025)** — *LLM Social Simulations: A Promising Research Agenda.* The cautionary counterweight; catalogues open validity problems.

A paper-to-concept reverse index appears at the end.

---

## 1. The simulation impulse in social science

Social science has always entertained the thought that a well-constructed model could stand in for a person. The thought has a pedigree.

**Schelling's segregation model** (1971) is the canonical example. Two kinds of tokens on a chessboard move if too few of their neighbors are like them. Nobody wants a segregated city; the city segregates anyway. The model was not meant to be accurate about real residential behavior; it was meant to demonstrate that **macro outcomes are not readouts of micro preferences**. The lesson — and the method — have shaped computational social science ever since.

**Epstein & Axtell's *Growing Artificial Societies*** (1996) took the idea further: put agents on a landscape, give them rules, watch societies emerge. This is the agent-based modeling (ABM) tradition that Macy & Willer (2002, *Annual Review of Sociology*) later surveyed and institutionalized. ABMs traded realism for control: the agents are simple, the rules are transparent, and the researcher learns by varying them.

The move the Week 4 papers make is to replace rule-based agents with **language-model agents**. An LLM does not follow a clean rule; it produces behavior by completing text. What it gains is plausibility — agents that can be interviewed, that produce open-ended interaction, that reason in natural language. What it risks is the opposite of ABM's classical virtue: you no longer know exactly why the agent did what it did.

🟦 Park's Smallville is the pure expression of this replacement. 🟩 Park's 1,000 People extends it to real survey respondents. 🟨 Hewitt uses LLMs not to simulate individuals but to predict aggregate experimental outcomes. 🟥 Anthis asks whether any of this can carry scientific weight.

---

## 2. Silicon sampling

A survey statistician asks: *who is in the sample, and does the sample represent the population we care about?* A **silicon sampling** paradigm (Argyle et al. 2023, *Political Analysis*; Horton 2023, *Homo Silicus*) asks the analogous question of LLMs: *can prompt-conditioned text from a language model stand in for responses from a person of a given type?*

Silicon sampling is not a claim that the LLM *is* a subject. It is a narrower claim: that conditional on the persona prompt, the model's outputs have **some measurable relationship** to what a human of that type would say. Argyle et al. (2023) found that GPT-3 conditioned on demographic profiles could reproduce the *associational structure* of the American National Election Study — party identification predicting vote choice, ideology predicting issue positions — without being trained to do so.

The two moves to keep separate:
- **Conditioning**: supplying the LLM with demographic or biographical context that is supposed to locate it in population space.
- **Evaluation**: comparing LLM outputs to human outputs on a shared instrument (survey, game, task).

The move 🟩 Park 2024 makes is to push both steps further: conditioning on a **two-hour qualitative interview** rather than a demographic label, and evaluating against the *same individual's* answers on the General Social Survey, the Big Five, and canonical economic games. The pretension is no longer to simulate a type but to simulate a **specific person**.

This is the closest social science has come to Zaller's (1992) "receive-accept-sample" model of the citizen implemented as code — though Zaller's model was causal and parsimonious, and this one is neither.

---

## 3. Agent architecture: memory, reflection, planning

Rule-based agents kept their internals transparent. LLM agents do not. But the Park 2023 🟦 paper made a methodological contribution that social scientists should recognize: it **modularized cognition**.

The three modules:

- **Memory stream**. Every observation, conversation, and internal thought is appended to a log. Retrieval is scored by three components — recency, importance (assigned by the LLM itself), and relevance to the current situation. This is Retrieval-Augmented Generation (RAG), but conceptually it is closest to what cognitive psychologists call a **long-term memory with cue-dependent retrieval** (Tulving 1972).
- **Reflection**. Periodically, the agent summarizes its recent memories into higher-order beliefs: "I am lonely." "Klaus cares about me." These summaries go back into the memory stream and themselves become retrievable. The analogue in cognitive psychology is Bartlett's (1932) schemas; the analogue in sociology is Goffman's (1959) construction of self through ongoing narrative.
- **Planning**. The agent drafts a day's schedule, refines it, revises under contingency. The analogue is Tolman's (1948) cognitive maps and the broader planning tradition in decision theory.

This architecture is not uniquely the Park design — variations appear across the multi-agent literature — but it is the clearest statement of the move. The implication for social science is that an LLM agent is **not a monolith**; its behavior is produced by the interaction of these modules, each of which can be perturbed independently. A sociologist interested in the role of *reflection* in identity formation can, in principle, ablate it.

---

## 4. Validity — the old vocabulary applied to new subjects

The single most useful inheritance social science brings to this literature is the **typology of validity** (Campbell & Stanley 1963; Cronbach & Meehl 1955; Shadish, Cook & Campbell 2002). Every LLM simulation study hangs on this vocabulary, whether it uses it or not.

- **Internal validity** — within the study, does the treatment cause the outcome? For LLM studies, this is the question of *whether the prompt caused the response*, which is trivially yes, and therefore uninteresting.
- **External validity** — does the finding generalize beyond the study's population, setting, and instrument? For LLM studies, this is the *central* question. Smallville's 25 agents organized a Valentine's Day party; would a different seed produce the same emergence? Would agents conditioned on German names do something different? 🟦🟩🟨 all face this question.
- **Construct validity** — do the measurements tap the concept they claim to measure? When 🟩 Park 2024 elicits Big Five responses from a simulated agent and compares them to the real respondent's Big Five, the question is not only *are the numbers similar* but *do they mean the same thing*. A human's "agreeableness" score is an index of a lifetime of social interaction; an LLM's is the next-token distribution conditioned on a persona prompt.
- **Ecological validity** — does the task environment resemble the real one? This is Brunswik's (1956) lens-model criterion, and it bites hard. A survey simulated in a chat window with no incentive for accuracy is not the same as a face-to-face interview with an hour of rapport.

🟥 Anthis et al. are the clearest voice on this. Their catalogue of open problems maps almost one-to-one onto the classical validity typology, and every social-science student should read them holding that dictionary open.

---

## 5. Prompt framing is question-wording

Social-science methodologists have known for at least sixty years that how you ask a question shapes the answer you get. **Schuman & Presser (1981)** demonstrated that response distributions to apparently equivalent survey items can differ by double-digit percentage points. **Tversky & Kahneman (1981, *Science*)** showed the same for decision framing in experimental economics. The discovery that **LLM outputs change dramatically with small prompt rewordings** is in every respect the same phenomenon, applied to a new class of subject.

This matters for two reasons:

1. It is a reason not to panic. "LLMs are unstable under rewording" is shocking only if one did not know that humans are too. The methodological problem is old.
2. It is a reason not to relax. The social-science response to question-wording effects was the entire discipline of **survey methodology**: pretesting, cognitive interviewing, split-ballot experiments. The LLM-simulation literature has not yet built its equivalent. 🟥 Anthis' call for benchmarks and validation protocols is, in effect, a call to build that discipline.

The analogy also suggests where **alignment tax** comes in. RLHF-trained models are tuned to produce answers humans rate well, which tends to mean polite, moderate, non-threatening answers. This is **social-desirability bias** (Edwards 1957; Paulhus 1984) baked into the instrument. When the literature worries that LLM subjects are too agreeable, it is rediscovering a problem survey methodologists have managed, imperfectly, for decades.

---

## 6. Forecasting social-science experiments

Philip Tetlock's *Expert Political Judgment* (2005) is the reference point for anyone asking *how well can smart people predict what will happen in a social-science setting?* The answer, for political and geopolitical forecasting, was: not well, and with wide variance across forecasters. The Good Judgment Project (Mellers et al. 2014) showed the variance was structured — some people, and some aggregation methods, did reliably better. This is **forecasting tournaments** as a research method.

🟨 Hewitt et al. (2024) run the equivalent tournament for **social-science experiments**. Given an experiment's description, can GPT predict its effect size and direction? The benchmark is human expert predictions on the same experiments (the Replication Markets tradition; DellaVigna & Pope 2018).

Two features of this setup deserve emphasis:

- **The replication crisis** (Open Science Collaboration 2015, *Science*) is what makes the question worth asking. If published experimental results were broadly reliable, predicting them would be a parlor trick. Because they are not, predicting them is a methodological intervention — potentially a cheaper substitute for some experiments, potentially a way to triage which experiments to invest in running.
- **Data contamination** is the elephant in the room. If the experiment was published before the LLM's training cutoff, the model may recall the result rather than reasoning to it. This is the hardest threat to rule out and the most important thing for readers to hold in mind.

Social-science students should see this paper as continuous with Tetlock and with the broader *predictive* turn in social science (Hofman, Sharma & Watts 2017, *Science*), not as a departure from it.

---

## 7. Simulating individuals vs. simulating populations

A useful distinction that the week's papers tacitly navigate:

- **Individual-level simulation** (🟦🟩) — produce behavior that tracks a specific person or a specific type. Success is measured by correspondence between simulated and real individual responses.
- **Population-level simulation** (🟨) — produce distributional predictions about aggregate outcomes. Success is measured by the accuracy of effect-size or direction forecasts.

The distinction matters because the failure modes are different. An individual-level simulator can be locally accurate but globally biased; a population-level simulator can match aggregates while getting every individual wrong (the **ecological fallacy**, Robinson 1950). Social-science students are already trained to keep this distinction sharp; they should deploy it when reading the LLM literature.

---

## 8. WEIRD training, WEIRD outputs

Henrich, Heine & Norenzayan's (2010, *Behavioral and Brain Sciences*) "The weirdest people in the world" showed that the subjects of published psychology experiments are drawn overwhelmingly from **Western, Educated, Industrialized, Rich, Democratic** populations — and that many findings do not replicate outside them. LLMs, trained on English-dominant web text, are WEIRD subjects at an industrial scale. When 🟦🟩🟨 simulate "humans," they are in the first instance simulating a WEIRD slice of humanity, and when the simulation fails to match real-world aggregates drawn from broader populations, this is the reason to suspect first.

This is not a reason to abandon LLM simulation. It is a reason to treat LLMs the way social scientists learned to treat psychology undergraduates: useful for some questions, misleading for others, and never to be confused with the full population of interest.

---

## Paper-to-concept reading map

If you are preparing to discuss a specific paper, these are the concepts from this chapter to bring with you.

- 🟦 **Park 2023 Generative Agents.** Bring §1 (ABM tradition and its replacement), §3 (memory / reflection / planning), §4 (believability vs. external validity), §7 (individual-level simulation).
- 🟩 **Park 2024 1,000 People.** Bring §2 (silicon sampling), §4 (construct validity of psychometric instruments), §7 (within-person vs. between-person accuracy), §8 (WEIRD boundaries). Zaller's RAS model is the natural social-science analogue for what the pipeline attempts.
- 🟨 **Hewitt 2024 Predicting Results.** Bring §4 (external validity under distribution shift), §6 (forecasting tournaments; replication crisis; data contamination), §7 (population-level simulation).
- 🟥 **Anthis 2025 LLM Social Simulations.** Bring §4 (full validity typology), §5 (prompt framing as question-wording, alignment tax as social-desirability bias), §8 (WEIRD). This paper is the chapter's critical index.

---

## Further reading from the social sciences

- Schelling, T. C. (1971). Dynamic models of segregation. *Journal of Mathematical Sociology*.
- Epstein, J. M. & Axtell, R. (1996). *Growing Artificial Societies*. MIT Press.
- Macy, M. W. & Willer, R. (2002). From factors to actors: Computational sociology and agent-based modeling. *Annual Review of Sociology*.
- Argyle, L. P., et al. (2023). Out of one, many: Using language models to simulate human samples. *Political Analysis*.
- Horton, J. J. (2023). Large language models as simulated economic agents: What can we learn from *Homo Silicus*? NBER w31122.
- Open Science Collaboration (2015). Estimating the reproducibility of psychological science. *Science*.
- Henrich, J., Heine, S. J. & Norenzayan, A. (2010). The weirdest people in the world? *Behavioral and Brain Sciences*.
- Tetlock, P. E. (2005). *Expert Political Judgment*. Princeton UP.
- Campbell, D. T. & Stanley, J. C. (1963). *Experimental and Quasi-Experimental Designs for Research*.
- Cronbach, L. J. & Meehl, P. E. (1955). Construct validity in psychological tests. *Psychological Bulletin*.
- Schuman, H. & Presser, S. (1981). *Questions and Answers in Attitude Surveys*.
- Zaller, J. (1992). *The Nature and Origins of Mass Opinion*. Cambridge UP.
