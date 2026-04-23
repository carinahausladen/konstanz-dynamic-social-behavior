# Chapter 5 — Emergent Societies

*A companion to Week 5 of the Konstanz seminar on Dynamic Social Behavior. This chapter introduces the concepts in play when we move from simulating individuals to simulating **populations** — and studying what emerges among them that no single agent contains.*

---

## Reading Guide

- 🟦 **Altera Team (2024)** — *Project Sid: Many-Agent Simulations Toward AI Civilization.* 10 to 1,000+ LLM agents in Minecraft; specialization, cultural transmission, emergent governance.
- 🟩 **Ashery et al. (2025)** — *Emergent Social Conventions and Collective Bias in LLM Populations.* Published in *Science Advances*. LLM agents playing naming games; conventions, collective bias, committed-minority flips.
- 🟨 **Larooij & Törnberg (2025)** — *Can We Fix Social Media? Testing Prosocial Interventions Using Generative Social Simulation.* LLM-populated synthetic platform testing six prosocial interventions.

A paper-to-concept index closes the chapter.

---

## 1. Social facts and the problem of emergence

Durkheim (1895, *The Rules of Sociological Method*) insisted that social facts — the patterned regularities of collective life — were *sui generis*: not reducible to the individual, and constraining individual action even though no individual had authored them. A century of social theory has agreed and disagreed in detail, but the core puzzle has persisted: **how do the recurrent patterns of collective life arise, and why do they persist?**

The simplest computational demonstration of the puzzle remains **Schelling's segregation model** (1971). Agents with a mild preference for neighbors like themselves produce cities far more segregated than any agent wants. Nobody is biased; the outcome is biased. The model is the cleanest way to impress on a student the one idea that makes all of this week's reading legible: **macro patterns are not readouts of micro preferences.**

**Granovetter (1978)** added the thresholds view: collective behavior depends on the distribution of tolerance for deviance from the current state. A crowd might riot or go home depending on how its thresholds are stacked. **Axelrod (1986, 1997)** brought evolutionary and cultural logic into the frame — norms and cultural traits spread, compete, and occasionally tip. **Macy & Flache** and the broader ABM tradition codified these moves as research practice.

The Week 5 papers are direct descendants. What has changed is the agent: Schelling's tokens had a single numeric threshold; Axelrod's had a vector of cultural traits; the LLM agent has a language model inside it, and can in principle *say why it did what it did*. That is a real gain, and also — as we will see — a real source of interpretive trouble.

🟦 Project Sid is this week's purest emergence paper: watch what the civilization does. 🟩 Ashery is the convention-formation paper in the Schelling / Granovetter / Centola line. 🟨 Larooij & Törnberg use emergence in a more instrumental mode: simulate a platform and test interventions on it.

---

## 2. Convention and norm

Two words that are often used interchangeably, and should not be.

**Convention**, in the sense of David Lewis (1969, *Convention*), solves a **coordination problem**. Two parties each prefer to meet rather than miss each other; given the history of coordinating in the café rather than the park, each has reason to keep coordinating in the café. There is no deep value at stake. If everyone started meeting in the park instead, the convention would be just as good. Driving on the right in France, on the left in Britain — pure Lewis conventions.

**Norm**, in the sense of Cristina Bicchieri (2006, *The Grammar of Society*), has more structure. A social norm is a pattern of behavior that is **conditional on expectations**: I follow it because I believe (a) others follow it and (b) others believe I ought to follow it, and because my preferences reflect those beliefs. Norms carry evaluative content; they can be violated, and violations can be sanctioned. Fehr & Gächter's (2000) altruistic punishment experiments made the sanctioning step empirically vivid.

The distinction matters because the minimal model used in 🟩 Ashery — the **naming game** — is a pure Lewis-style convention. Agents meet in pairs, each picks a label for a thing; if the labels match, both are rewarded. Iterated across a population, a single name spreads. The paper shows that this classic model of convention formation (Baronchelli et al. 2006, *Journal of Statistical Mechanics*) still works when the agents are LLMs.

But the paper also shows something the naming-game literature spent years establishing: that **populations can become biased as a whole even when individuals are not**. This is the same shape as the Schelling result, now at the level of conventions rather than neighborhoods, and it is where the distinction to norms starts to matter. When a biased convention becomes backed by the belief that it *ought* to be followed, it has crossed from Lewis into Bicchieri, and it is much harder to change.

🟦 Project Sid's religious transmission and rule adoption are closer to norms than to pure conventions; 🟩 Ashery's naming games are pure conventions, with the suggestion that collective bias could be the first step toward norm formation.

---

## 3. Tipping points and committed minorities

One of the cleanest empirical results in modern social-dynamics research is **Centola et al. (2018, *Science*)**: in controlled online experiments, a committed minority of roughly **25 percent** suffices to flip a population's convention to a new one. The 25 percent is not a universal constant but it sits in the middle of a range of predictions from threshold-model theory (Granovetter 1978; Watts 2002; Centola & Macy 2007).

What the Centola experiments established is that **convention change is not a smooth process**. Nothing happens — nothing happens — and then the tipping point is crossed and the new convention sweeps the population. This is the signature of a **phase transition**, a concept imported into sociology from statistical physics.

🟩 Ashery et al. replicate this experimental shape in silico. A small group of LLM agents committed to a non-majority label can, under the right conditions, flip the whole population. The replication is interesting for two reasons. First, it is a small act of **consilience**: the same qualitative dynamics appear whether the agents are humans in a chat experiment or language models in a simulation. Second, it is a **test of the mechanism**: if the dynamics depend on humans' capacity for conformity in Bicchieri's sense, LLMs should not produce them — and yet something that looks like them appears anyway. This is either a discovery about LLMs or a discovery that conformity as a mechanism is more representational than we thought.

Students should hold both interpretations in their heads at once.

---

## 4. Homophily, echo chambers, and the honest state of the evidence

**McPherson, Smith-Lovin & Cook (2001, *Annual Review of Sociology*)** is the canonical reference for **homophily** — the tendency of similar people to associate. Homophily is empirically ubiquitous: it shows up in friendship, marriage, organizational ties, and online networks. Nothing about it is controversial, in its raw form.

What *is* controversial is the leap from homophily to **filter bubbles** and **echo chambers**, a leap most associated with Pariser (2011, *The Filter Bubble*) and Sunstein (2001, *Republic.com*). The argument: algorithmic personalization amplifies homophily to the point that users inhabit informational worlds sealed off from one another. The concern drove a decade of platform-reform debate.

The empirical record is more complicated than the popular argument suggests.

- **Bakshy, Messing & Adamic (2015, *Science*)** studied cross-cutting exposure on Facebook and concluded that individual choice (who users friended and what they clicked) did more to narrow exposure than the algorithm did. The study is contested for access reasons, but its result is hard to ignore.
- **Guess et al. (2023, *Nature / Science*)**, the massive 2020-election collaboration, found that substantial changes to the Facebook and Instagram algorithms produced only modest shifts in polarization, belief, and time-on-platform.
- **Bail (2022, *Breaking the Social Media Prism*)** reframes the problem: the threat is not the bubble, it is the performance of identity under visible cross-partisan observation. The feed makes us more tribal by showing us the other side, not by hiding it.

Any competent reading of 🟨 Larooij & Törnberg requires holding this evidence alongside the paper's synthetic-platform findings. The paper's intervention tests — chronological feeds, bridging-based ranking, etc. — correspond one-to-one with proposals in the ongoing policy debate. Its conclusion that many interventions produce only modest gains is, in effect, a computational echo of the Guess et al. empirical result. Students should read it with that result in mind.

---

## 5. Algorithmic amplification and bridging ranking

Two technical pieces of vocabulary are worth owning before engaging 🟨.

**Algorithmic amplification** is the claim that a platform's ranking system does not merely select from what users produce; it **shapes what users produce** by making some kinds of content visible and others not. This is a causal claim about feedback, and like all causal claims about feedback it is hard to establish empirically. The literature is unsettled; read it as contested, not decided.

**Bridging-based ranking** (Ovadya & Thorburn; Stray et al.) is a design proposal: rank content by whether it attracts engagement from *across* existing partisan or demographic divides, not merely by total engagement. **Community Notes** on X is the largest deployment of something in the spirit of a bridging algorithm; its published evaluations are mixed. Bridging ranking is in the direct lineage of **deliberative democracy** (Habermas 1984, 1996; Fishkin 1991), which has long argued that good public deliberation requires structured exposure across difference.

🟨 Larooij & Törnberg test both chronological and bridging interventions. Their finding that prosocial interventions in the synthetic platform yield modest gains, and sometimes make things worse, should be read as a **computational complement** to a policy debate that has been argued mostly essayistically until now.

---

## 6. Scale and the Durkheimian move

One of the subtler theoretical claims in 🟦 Project Sid is that **scale matters in kind, not only in degree**. Ten agents and a thousand agents are not the same simulation. Durkheim (1893, *The Division of Labor in Society*) argued that the transition from **mechanical solidarity** (homogeneous, close-knit communities) to **organic solidarity** (differentiated, interdependent societies) was driven in part by population density. The larger the population, the more specialization becomes viable; the more specialization, the more interdependence; the more interdependence, the more elaborated the institutions.

Project Sid reports specialization and role-taking emerging as agent populations scale. This is not just an engineering detail. It is a claim, at least implicitly, that the same threshold effect shows up in artificial populations. Whether this is a discovery about LLM agents or an artifact of the cognitive architecture the authors built (the PIANO scheme) is a legitimate open question. Social-science students should be alert to the ambiguity.

---

## 7. Cultural transmission

**Boyd & Richerson (1985, *Culture and the Evolutionary Process*)** and the subsequent cultural-evolution literature (Henrich 2016, *The Secret of Our Success*; Mesoudi 2011) treat culture as a system of inheritance distinct from but interacting with genetic inheritance. Traits spread through populations by imitation and teaching; some traits spread faster than others; the ecology of traits evolves.

🟦 Project Sid's observation of religious transmission — agents adopting ritual practices and propagating them through the population — sits squarely in this tradition. The finding is less that LLMs can transmit memes (of course they can, they are language models) than that the *structure* of transmission through an artificial population echoes empirical cultural-transmission dynamics: prestige biases, conformist copying, successive variation. The analogue experiment in humans is the Rendell et al. (2010, *Science*) social-learning-strategies tournament, which established that **copy-when-uncertain** and **copy-the-successful** dominate more elaborate strategies across problem structures.

Reading 🟦 through Boyd-Richerson-Henrich rather than through engineering-first framings is the move that makes the paper legible as social science.

---

## 8. Simulation as a policy sandbox

The methodological claim common to all three papers — most explicit in 🟨 — is that an LLM-populated simulation can serve as a **counterfactual laboratory** for social interventions that are either too costly, too ethically fraught, or too coarse to run on real populations. This is a claim with heritage: **computational social science** (Lazer et al. 2009, *Science*) is in part a claim that richer computational models allow counterfactual reasoning that observational data do not support.

But simulation-as-sandbox has a characteristic weakness. The simulation's answer is only as good as the fidelity of the simulated agents. If the agents over-react to partisan cues, the simulation will over-predict polarization; if they under-react, it will under-predict. The simulation's output is **conditional** on the simulated agent being a good model of the human, which is the unresolved question the Week 4 chapter surveyed.

Students reading 🟨 should therefore ask two questions simultaneously. First: do the interventions produce the predicted effects **inside the simulation**? Second: is the simulation itself a credible model of the system the interventions would be applied to? Papers in this tradition are persuasive only when both questions have defensible answers.

---

## 9. Collective bias from unbiased agents

A closing conceptual point, running through the chapter. The Schelling segregation result, the Ashery collective-bias result, and several emergent phenomena in Project Sid share a **structural family resemblance**: the macro outcome is more extreme than any individual-level preference would suggest.

This is not an LLM-specific phenomenon. It is the canonical insight of computational social theory. **Jackson (2019, *The Human Network*)** surveys how it plays out in contemporary networks. **Centola (2018, *How Behavior Spreads*)** catalogues the empirical cases. The Week 5 papers extend the observation into artificial populations; the observation itself is older than any of them.

A student who leaves Week 5 with one sentence should have this one: *You cannot understand the behavior of a population by aggregating the behavior of its members, whether those members are humans or language models.*

---

## Paper-to-concept reading map

- 🟦 **Altera — Project Sid.** Bring §1 (Durkheim / Schelling on emergence), §6 (population density and specialization), §7 (cultural transmission; Boyd-Richerson). The natural debate is whether the emergent civilization is **discovery or design** — cognitive architecture as theoretical choice.
- 🟩 **Ashery — Emergent Conventions.** Bring §1 (emergence), §2 (Lewis conventions vs. Bicchieri norms), §3 (Centola 2018 tipping points), §9 (collective bias). The natural debate is whether LLM convention dynamics replicate human ones because of shared mechanism or by pattern completion.
- 🟨 **Larooij & Törnberg — Fix Social Media.** Bring §4 (homophily, echo chambers, Bakshy / Guess evidence), §5 (algorithmic amplification, bridging), §8 (simulation as policy sandbox). The natural debate is whether the synthetic platform is a credible model of real platforms — the sandbox-validity question.

---

## Further reading from the social sciences

- Schelling, T. C. (1971). Dynamic models of segregation. *Journal of Mathematical Sociology*.
- Durkheim, É. (1893 [1984]). *The Division of Labor in Society*.
- Durkheim, É. (1895 [1982]). *The Rules of Sociological Method*.
- Granovetter, M. (1978). Threshold models of collective behavior. *American Journal of Sociology*.
- Lewis, D. (1969). *Convention*. Harvard UP.
- Bicchieri, C. (2006). *The Grammar of Society*. Cambridge UP.
- Centola, D. et al. (2018). Experimental evidence for tipping points in social convention. *Science*.
- Centola, D. (2018). *How Behavior Spreads*. Princeton UP.
- Baronchelli, A. et al. (2006). Sharp transition towards shared vocabularies in multi-agent systems. *JSTAT*.
- McPherson, M., Smith-Lovin, L. & Cook, J. M. (2001). Birds of a feather: Homophily in social networks. *Annual Review of Sociology*.
- Bakshy, E., Messing, S. & Adamic, L. (2015). Exposure to ideologically diverse news on Facebook. *Science*.
- Bail, C. A. (2022). *Breaking the Social Media Prism*. Princeton UP.
- Pariser, E. (2011). *The Filter Bubble*.
- Habermas, J. (1996). *Between Facts and Norms*.
- Boyd, R. & Richerson, P. J. (1985). *Culture and the Evolutionary Process*. Chicago UP.
- Henrich, J. (2016). *The Secret of Our Success*. Princeton UP.
- Rendell, L. et al. (2010). Why copy others? Insights from the social learning strategies tournament. *Science*.
- Lazer, D. et al. (2009). Computational social science. *Science*.
