# General Skill for Academic Paper Writing, Editing and Consistency

> **OPERATIVE VERSION.** This English file is the one that BINDS manuscript work.
> `academic-writing-skill.tr.md` beside it is the owner's Turkish source, kept for reading
> and authoring — it is not the version an agent obeys. When the two disagree, this file
> wins. Editing the Turkish file does NOT update this one: the translation is a deliberate,
> audited pass, so a Turkish edit leaves this file stale until that pass is re-run. Both are
> stack-managed — edit them in `claude-agent-stack/templates/ownerDocs/`, never in a repo copy.

This document is a general ruleset that can be used for writing or restructuring empirical, theoretical, computational and methodological studies across different disciplines. The aim is not merely to make the text look more academic; it is to construct an auditable scientific argument among the research question, method, finding, interpretation and contribution.

These rules can be given directly as instructions to an author, an editor or an LLM-based writing tool.

---

## 0. Priority order and binding principles

The following priority order must be followed when a paper is edited:

1. **The target journal's current author guidelines**
2. **The reporting guideline specific to the study type**
3. **Scientific and numerical accuracy**
4. **Alignment between claim and evidence**
5. **Semantic and numerical consistency across sections**
6. **The author's deliberate terminology and format preferences**
7. **Academic tone, fluency and brevity**

If the target journal explicitly defines a rule differently, the journal's rule must be applied, not this general document. For randomized trials, observational studies, systematic reviews, prediction models, qualitative studies, animal experiments and similar designs, the appropriate reporting checklist must additionally be used.

### What must be preserved absolutely

- Data, numbers, equations, results, citations, tables and figure information must not be fabricated.
- Scientific meaning must not be altered in order to make the text more fluent.
- Technical terms the author has deliberately left in English must not be translated without permission.
- LaTeX commands, labels, refs, citations, macros, equations, tables and figures must not be corrupted.
- A scientific claim must not be made stronger than the design and the data permit.
- Missing or contradictory information must not be silently completed; it must be marked with `[DOĞRULANMALI]` ("to be verified" — the marker token is kept verbatim so it matches the Turkish source ruleset) or an editorial note.

---

## 1. Reconciled fundamental decisions

In this ruleset, certain common but overly rigid approaches have been balanced as follows.

### 1.1 The passive voice is the default; but it is not a mechanical obligation

Academic text must be written impersonally, in a measured way, and focused on the object/procedure. The passive construction is frequently appropriate, particularly in the Methods section. That said, if it is important that the agent be known, or if the passive construction makes the sentence artificial, an active sentence must be used.

**Appropriate:**

> The data were analysed with a bootstrap procedure.

**Appropriate:**

> \citet{ornek2025} reported that the same effect diminished on larger models.

**Inappropriate mechanical passivity:**

> It is observed by us that the literature has been shown.

Academic tone means not hiding the agent, but presenting the claim in a measured and auditable manner.

### 1.2 Tense must be chosen according to rhetorical function, not according to the section name

The whole paper must not be written in the present simple. General knowledge, prior work, the method carried out, the observed result and the current interpretation require different tenses.

### 1.3 A large number of subheadings must not be used; but a necessary structural distinction must not be prevented

Abstract, Introduction, Methods, Results, Discussion and Conclusion are the fundamental backbone. Methods and Results may be divided into subheadings if the structure of the study requires it. In general, more than three heading levels must not be used. A new subheading must not be opened for every two or three paragraphs.

### 1.4 Studies in the literature must not be recounted one by one

The aim is not to enumerate every paper or every method found in the literature, but to synthesise the **materially relevant method families, findings and limitations** that establish the research question. Comprehensiveness must not be confused with cataloguing.

### 1.5 A comparison table is not mandatory in every Discussion section

If the comparison with prior work is multidimensional and becomes difficult to follow within prose, a comparison table must be used. A table must not be added merely decoratively or as though it were mandatory.

### 1.6 Redefining acronyms in every section is not the general standard

The minimum rule is this: an abbreviation must be defined at first use within the abstract, and again at first use within the main text. Within long and independently readable major sections, supplementary files, figures and tables, it must be expanded again if necessary. If the author's stricter house style is to be applied, redefinition may be done at first use within every **major section**; mechanical repetition must not be done in every subsection.

### 1.7 “Proposed method” must be used only if there genuinely is a new method

If the study does not propose a new algorithm but presents an evaluation, ablation, measurement instrument or empirical analysis, these must be identified by their correct names. No research artefact must automatically be called a “proposed framework”.

---

## 2. The scientific backbone of the paper

The paper must be constructed along the following chain:

> **General problem → existing knowledge → tension or gap in the literature → research question → design/method → finding → interpretation → contribution → limit**

Each section must carry its own part of this chain.

### Must be done

- The research question must be expressible in a single sentence.
- Every headline claim must be matched directly to a test, table, figure or analysis.
- The originality of the study must be demonstrated through which confound it isolates, which baseline it establishes, or which problem it solves.
- The contribution must be established not merely with the word “novel”, but **with a chain of evidence**.
- For every major claim, the population, setting, endpoint and design boundary must be stated.

### Must not be done

- The research question must not be changed from section to section.
- A new main contribution not promised in the Introduction must not be added in the Conclusion.
- A finding not present in the Results must not be brought forth in the Discussion.
- A correlation must not be presented as a causal effect or a mechanism.
- A result must not be shown as more uniform, robust or general than it is in order to strengthen the story.

---

## 3. Academic language, voice and tense rules

### 3.1 Academic tone

The text must be:

- impersonal,
- measured,
- clear,
- evidence-based,
- explicit as regards the agent (the doer of the action) where required,
- appropriate to the discipline as regards jargon,
- free of exaggeration.

#### Preferred patterns

- "In this study, the problem of X is addressed."
- "Whether the effect of X originates from component Y was tested."
- "The data were analysed using the Z procedure."
- "A statistically detectable difference was observed."
- "This pattern is consistent with the X explanation."
- "The result is limited to the Y population and the Z setting."

#### Patterns to be avoided

- "We have conclusively proven that…"
- "We obtained a very striking and surprising result."
- "As everyone knows…"
- "As can easily be seen…"
- "This method is undoubtedly the best."
- "The results are revolutionary."

Expressions such as "prove", "demonstrate conclusively", "always", "never", "safe", "guaranteed" and the like must be used only when the required evidential standard is genuinely met.

### 3.2 Tense matrix

| Rhetorical function | Preferred tense | Example function |
|---|---|---|
| Generally accepted knowledge | Present simple | "LLMs generate code from natural-language prompts." |
| A literature state still in force | Present perfect or present simple | "Several studies have examined…" |
| A specific past study | Past simple | "Smith et al. reported…" |
| An operation performed in this study | Past simple; mostly passive | "The models were evaluated…" |
| The present function of a definition, equation or figure | Present simple | "Equation~(1) defines…"; "Figure~1 shows…" |
| An observed result | Past simple | "The treatment produced…" |
| The present meaning of a result | Present simple | "These findings indicate…" |
| Uncertain interpretation | Modal + present | "This pattern may reflect…" |
| Future work | Future or modal | "Future studies should examine…" |

#### Default usage by section

- **Abstract:** background present; method and findings past; take-home implication present.
- **Introduction:** established knowledge present; specific prior studies past; literature evolution present perfect; gap and current objective present.
- **Methods:** the operations performed past; definitions, equations and general procedures present.
- **Results:** observed outcomes past; figures/tables present; very limited statistical interpretation present.
- **Discussion:** past when referring to one's own findings; present for meaning and implication; modal for uncertainty of mechanism.
- **Conclusion:** what was done in the study past; the supported final inference present; future work future/modal.

#### Must not be done

- Unjustified tense drift must not occur within the same paragraph.
- A previous study must not be narrated in the present tense as if it were still being conducted.
- One's own observed results must not be fixed in the present simple as though they were general laws.
- The entire Methods section must not be written in the present tense.
- The whole article must not be forced into the passive voice merely so that it looks "academic".

### 3.3 Sentence and paragraph structure

Each sentence must preferably contain a single main claim. Each paragraph must be a single unit of argument.

A good paragraph mostly follows this order:

1. Topic sentence
2. Evidence or explanation
3. Limited interpretation
4. Transition to the next paragraph

#### Must be done

- The main idea must be given in the early part of the sentence.
- Long sentences must be split if they contain method, result, interpretation and limitation.
- Paragraphs must generally be units of meaning of 3--6 sentences.
- References such as "this", "these", "the situation in question" must be explicit.

#### Must not be done

- Four different claims must not be combined in one sentence.
- Literature review, method detail, result and recommendation must not be mixed within the same paragraph.
- Metadiscourse must not take precedence over the actual argument.
- The same result must not be told over and over in different words.

---

## 4. Section structure and use of headings

The backbone of a general research article is as follows:

1. Title
2. Abstract
3. Keywords
4. Introduction
5. Methods / Materials and Methods
6. Results
7. Discussion
8. Conclusion, or a conclusion integrated into the Discussion
9. Acknowledgements
10. Funding
11. Author Contributions
12. Competing Interests / Conflict of Interest
13. Ethics / Consent statements, if required
14. Data Availability
15. Code Availability, if required
16. References
17. Supplementary Information or Appendix

This ordering may vary according to the venue.

### Heading rules

- The core story must not be split into unnecessary subheadings.
- The Introduction must in most cases remain under a single heading.
- "Related Work" and "Present Work" must be made separate headings only if the discipline or the venue requires it.
- Methods subheadings must be derived from the actual workflow.
- Results subheadings must be aligned with the preregistered analysis hierarchy or with the research questions.
- Discussion subheadings may be used in very long texts; in short discussions a heading must not be opened for every paragraph.
- At most three heading levels must be used, unless the venue requires otherwise.

### Must not be done

- Two-sentence subsections must not be created.
- Headings must not be written like concluding sentences or marketing slogans.
- The same content must not be repeated in both the main text and the appendix.
- The article type structure of the target journal must not be ignored.

---

## 5. Terminology, abbreviations and notation

### 5.1 Terminology

A single canonical term must be chosen for each core concept.

#### Must be done

- `task`, `unit`, `item`, `sample`, `case`, `arm`, `condition`, `endpoint`, `metric` and `baseline` must be kept distinct from one another.
- The same concept must be referred to by the same name in all sections.
- Metrics that look similar but differ must be defined explicitly.
- Whether technical terms are to be left in Turkish or in English must be decided from the outset.
- Words the author has deliberately left in English must be preserved.

#### Must not be done

- Different synonyms must not be used continually for the same thing.
- "Validation", "verification", "confirmation", "certification" and "replication" must not be mixed at random.
- A control must not later be renamed as a baseline or a treatment.

### 5.2 Abbreviations

- The Abstract must be treated as an independent text, and an abbreviation must be defined there at first use.
- Within the main text an abbreviation must be expanded again at its first use.
- First use may be expanded again within long or independently readable major sections.
- Tables, figures and supplementary files must be as self-contained as possible.
- Non-standard abbreviations must be kept to a minimum and created only when repeated use is meaningful.
- Only abbreviations established across the field must be used in the Title.

#### House-style strict mode

If the author wants each major section to be read independently, an abbreviation may be redefined at its first use within the Abstract, Introduction, Methods, Results, Discussion and Conclusion. The same abbreviation must not be redefined in every subsection.

### 5.3 Symbols and units

- Every symbol must be defined at first use.
- The unit must be stated where one exists.
- SI units must be preferred, unless the field standard differs.
- The same symbol must not be used with different meanings.
- Scalar, vector, matrix and set notation must be consistent.

---

## 6. Title and Keywords

### 6.1 Title

The Title must state clearly the study's core object, its intervention or method, and, if necessary, the study design.

#### Must be done

- It must be specific and informative.
- The main endpoint or phenomenon must be visible where required.
- The study type must be added to the title if it prevents misunderstanding.
- The claim strength must not be stronger than the main finding.

#### Must not be done

- Promotional adjectives such as "novel", "revolutionary", "unprecedented" must not be used.
- A causal title must not be written if the result does not show causality.
- An excessively long title with a colon and three claims must not be created.
- Non-standard abbreviations must not be used.

### 6.2 Keywords

- Generally 4--8 keywords must be selected, according to the venue.
- The words in the Title must not all be repeated.
- Method, domain, task and the main phenomenon must be represented in a balanced way.
- The indexing terminology of the field must be used.

---

## 7. Abstract rules

Unless the venue requires otherwise, the abstract must be a single paragraph and must be understandable on its own. The general movement must proceed from the general to the specific.

### Recommended semantic order

1. **General problem:** What problem exists within the field or the deployment context?
2. **Literature gap:** What do previous studies address jointly, or which comparison do they leave missing?
3. **This study's answer:** Which method, design, framework or analysis is presented?
4. **Experimental setting:** Where, with which sample/population and with which basic protocol was it tested?
5. **Main results:** What are the two or three headline results that prove the contribution?
6. **Take-home conclusion:** What does the result mean and by which scope is it bounded?

### Must be done

- The problem and the gap must be given in the first 1--2 sentences.
- Patterns of the type "To address this problem, … is proposed/presented/evaluated" must be used only when they are genuinely appropriate.
- The methods must state the sample, dataset, model/population, design and endpoint without drowning in detail.
- The most important quantitative results must be given.
- Effect size, uncertainty or an exact comparison must be used if it is required for the contribution to be understood.
- The final sentence must carry the contribution together with the boundary.
- Background must be written in the present tense, procedures/results in the past tense, and implications in the present tense.

### Must not be done

- A long literature review must not be conducted.
- The abstract must not be filled with hardware brands, file counts, minor hyperparameters or secondary tests.
- All p-values and all subgroup results must not be given in the abstract.
- Citations must not be used, unless the venue explicitly permits them.
- The abstract must not be a copy of the first paragraph of the Introduction.
- Limitations must not be concealed entirely.
- A deployment or generalization claim stronger than the result must not be constructed.

### Short check for the abstract

- Is the problem clear?
- Is the gap testable?
- Is the solution understandable in a single sentence?
- Is it clear where and how it was tested?
- Are the main results supported with numbers?
- Does the final sentence contain the contribution and the scope?

---

## 8. Introduction rules

The Introduction must establish the cone-shaped story of the entire paper. Its purpose is not merely to give background, but to bring the reader necessarily to the research question.

### 8.1 Recommended paragraph functions

#### Paragraph 1 — The most general problem and the practical context

- The broad problem of the field must be defined.
- Why the problem matters must be shown.
- Factual claims must be supported with current and appropriate references.
- At the end of the paragraph, the transition to the next problem area must be prepared.

#### Paragraph 2 — The established approach and positive evidence

- The principal method families developed to solve the problem must be synthesized.
- The conditions under which they succeed must be stated.
- Studies must not be catalogued one by one.

#### Paragraph 3 — Conflicting or negative evidence

- The regimes in which the established approach does not work must be shown.
- Moderating factors such as model scale, dataset, training condition, budget or evaluation weakness must be explained.
- The paragraph must end with the unresolved problem.

#### Paragraph 4 — The correct baseline and the identification gap

- The real practitioner or scientific decision problem must be defined.
- Which ingredients, controls or explanations previous studies could not separate must be stated explicitly.
- The gap must be testable, not vague like "few studies exist".

#### Paragraph 5 — The approach presented in this study

- The current study must be introduced with a "For these reasons…" transition.
- What is tested, which comparison is established and which gap is targeted must be given.
- The main idea of the method must be described here; operation-level detail must not be entered into.
- Sentences may mostly be impersonal and passive.

#### Paragraph 6 — Contributions and headline findings

- Empirical, methodological, theoretical and practical contributions must be separated from one another.
- Contributions must preferably not exceed 3--5 items.
- Each item must contain a **problem → solution/test → evidence → boundary** mini-chain.
- A contribution list must be used if it suits the venue's style; otherwise it must be given within the prose.

#### Final paragraph — Scope and roadmap

- The boundary of the claim must be stated explicitly.
- The paper organization must be given briefly only if it provides the reader with genuine navigation.

### 8.2 Must be done within the Introduction

- Each paragraph must prepare the logical need for the next one.
- The literature must be used as a problem-solving narrative rather than a chronological list.
- Relevant method families and unresolved problems must be presented in a balanced way.
- Positive and negative literature must be evaluated together.
- The study aim, research questions or hypotheses must be stated explicitly.
- Novelty must be shown through the control or design that provides it.

### 8.3 Must not be done within the Introduction

- All Methods details must not be given.
- The Results section must not be rewritten from the start.
- Prior work must not be caricatured in order to enlarge the contribution.
- The expression "to the author's knowledge, the first" must not be used without a current and systematic search.
- The same gap must not be repeated again and again in different paragraphs.
- "Related Work" and "Present Work" headings must not be added unless the discipline requires them.
- Each citation must not be summarized in a separate sentence.
- The main story must not be lost while trying to present "all methods".

---

## 9. Methods rules

The fundamental task of the Methods section is to enable the reader to understand the study, to evaluate it, and to reproduce it as far as possible.

### 9.1 Opening paragraph

In the first paragraph:

- the general study design,
- the main method/framework/instrument,
- the input-output flow,
- the primary endpoint,
- the main subsections

must be given briefly.

If the study involves a complex pipeline, an overall framework figure must be presented in the opening subsection. The figure must show the order of the parts and their connections; the text must not merely repeat the figure, but must explain its logic.

### 9.2 Subsection structure

Subsections must be determined according to the study's real workflow. Not all of the headings below are mandatory in every paper:

- Study design and research questions
- Population, dataset or sample construction
- Inclusion/exclusion criteria
- Preprocessing
- Proposed method / measurement instrument / model architecture
- Mathematical formulation
- Training or inference protocol
- Baselines, controls and ablations
- Evaluation protocol and endpoints
- Statistical analysis
- Reproducibility, software and hardware
- Ethics, consent and governance
- Preregistration and deviations

### 9.3 Mathematical formulation

For each equation:

1. The purpose of the equation must be explained within the prose.
2. The equation must be numbered and referenced where necessary.
3. All symbols must be defined.
4. Units or dimensions, if any, must be stated.
5. Assumptions must be written explicitly.
6. A relation to the preceding or the following equation must be established.

Definitions, propositions, lemmas and theorems must be used only when they are formally necessary. A simple concept must not be placed inside a `definition` environment merely to make it look technical.

### 9.4 Algorithms and pseudocode

**MANDATORY (owner directive 2026-08-05).** Every manuscript is required to give its procedure
as **numbered algorithm blocks**. This is not a conditional rule: the justification "no new
algorithm is presented" does not drop the block, because the block documents not the novelty
but the **order of execution**. A reader cannot derive from a list of equations which of 16
equations runs first and which runs afterwards.

At least **two blocks** are given, and the two are numbered separately:

1. **Production / measurement procedure** — what is done from the input up to the raw output.
   This is the execution that produces the evidence.
2. **Evaluation and inference procedure** — from the raw output up to the reported quantities
   and the decision. This block exists even in the case where a study *does not learn*:
   estimators, intervals and decision rules are the steps of this block.

If a study genuinely carries a single procedure, why the absence of the second block is a
feature rather than a deficiency **is written explicitly**; it cannot be skipped silently.

Every block is required to carry the following:

- `Input:` and `Output:` lines, consistent with their symbols and with the notation table,
- initialization,
- numbered steps,
- stopping condition (if there is a loop),
- computational complexity if required,
- **a reference to the equation each step uses**. The step is required to show the equation it
  uses by name; "see Section 3" is not sufficient.

**Naming honesty is read together with §0.** The block is numbered as "Algorithm N" and
"proposed" may be used in the heading — this is the name of the LaTeX environment, not of the
claim. However, **the caption is required to say what the artifact actually is**: an evaluation
instrument, a measurement procedure or an ablation cannot be presented as a "repair algorithm"
or a "proposed framework". Example form: *"The proposed measurement procedure. It is not a repair
algorithm; it is a content-attribution measurement instrument."* A numbered environment and an
honest caption do not conflict; what §0 forbids is naming the artifact in the **wrong class**.

**A mechanical audit is mandatory.** The step–equation mapping cannot be maintained by hand:
when an equation is renamed the step points to nothing, when an equation is added it enters no
step, and both rot silently. The repository is required to carry a gate, and the gate must
catch all three of the following: (a) a step referencing a label that does not exist, (b) an
equation that enters no step, (c) an exemption left in place for an equation that is no longer
defined. It is legitimate for an equation to enter no step because it is a *property* rather
than an *operation*, but this is written in an exemption list **with its justification**; it is
not tolerated silently.

Pseudocode must not unnecessarily repeat a simple workflow that is already clear within the
prose; however, this cannot be used as a justification for dropping the two blocks above. The
constraint applies to unnecessary detail **inside** the block, not to the existence of the
blocks.

### 9.5 Tables and figures

- An overview figure may be used for the main framework.
- If the original module developed is complex, a second detailed figure may be added.
- A table may be used for the dataset, sample, model, hyperparameters, symbols or constants.
- Every table and figure must be called out in the text before its first use.
- Captions must be self-contained; the sample, units and symbols must be explained where necessary.

### 9.6 Must be done within the Methods

- The population and the unit of analysis must be defined explicitly.
- Sampling, randomization, seed and split procedures must be stated.
- Baselines and controls must be defined operationally.
- What adjectives such as "matched", "held-out", "independent", "frozen", "random" mean must be explained.
- Primary and secondary endpoints must be separated.
- Missing data, exclusions and failure handling must be given.
- Statistical tests, one/two-sided status, correction procedure and thresholds must be written.
- The data/code/material availability plan must be stated.
- Deviations and amendments must not be concealed.

### 9.7 Must not be done within the Methods

- It must not be asserted that the method was successful.
- An analysis chosen after the result was seen must not be presented as preregistered.
- Critical implementation details must not be skipped by calling them "standard procedure".
- If there is no strict total compute equality, "matched compute" must not be used on its own; what was equalized must be explained.
- If held-out data was used for selection, it must not be presented as a fully untouched test set.
- Result or discussion language must not be used in the Methods.
- Figures and tables must not be left unexplained in the text.

---

## 10. Results rules

The task of the Results section is to recall briefly where and how the testing was carried out and to report what was obtained together with its evidence. The question "Why did it happen?" must be left to the Discussion.

### 10.1 Opening paragraph

The first paragraph must briefly give the following information:

- the model/method/population that was tested,
- the platform or execution environment, if it affects the results,
- the datasets or test sets,
- the sample size,
- the comparison arms/groups,
- the number of rounds/trials,
- the primary endpoint,
- the scoring procedure.

This paragraph must not be a full repetition of the Methods. The aim is to enable the reader to follow the results independently.

### 10.2 Presentation of the experimental flow

If the test protocol is complex, an evaluation schematic may be given. If the framework figure in the Methods already shows the same flow explicitly, a duplicate diagram must not be added in the Results. A Results figure must show the result pattern, not the workflow.

### 10.3 Order of analysis

The Results must follow, as far as possible, the following order:

1. Run completeness and data integrity
2. Primary outcomes
3. Secondary outcomes
4. Ablations or component analyses
5. Robustness/sensitivity analyses
6. Error/failure analyses
7. Audit events or protocol deviations

This order must be aligned with the preregistration, the research questions or the hypotheses.

### 10.4 Reporting template for each main result

For each comparison, the following information must be given as far as possible:

1. The direction of the comparison
2. Effect size or net difference
3. Exact sample size or counts
4. Confidence interval or uncertainty
5. Raw and adjusted $p$-value, if required
6. Heterogeneity or subgroup direction
7. A single-sentence, non-mechanistic conclusion

#### Example structure

> Condition A produced higher accuracy than Condition B (difference = X, 95\% CI [L, U], adjusted $p=...$). The same direction was preserved in Z of subgroup Y.

### 10.5 Narration of tables and figures

For each display item, the text must briefly explain:

- what is shown,
- the main numerical pattern,
- the difference relative to the baseline,
- the uncertainty or variability,
- whether the pre-specified threshold was met.

The text must not repeat every cell of the table.

### 10.6 Must be done in the Results

- Exact $n$ values must be given.
- If the dataset or benchmark is external, it must be referenced.
- Primary, secondary and descriptive analyses must be labelled.
- Null and adverse results must also be reported.
- Effect size and uncertainty must be presented together.
- Figure/table ordering must be consistent with the text.
- Public and held-out endpoints must be kept separate from each other.

### 10.7 Must not be done in the Results

- A causal mechanism must not be explained.
- A lengthy comparison with the literature must not be made.
- A practical recommendation must not be produced.
- A non-significant result must not be written up as "there is no effect".
- A pooled tie must not be called "equivalence".
- It must not be the case that only the significant results are selected and the null results concealed.
- The same result must not be repeated three times unnecessarily in prose, table and figure.
- Interpretive adjectives such as "surprising", "striking", "remarkable" must not be used.

---

## 11. Discussion rules

The Discussion must discuss why the results matter, what they may mean, which explanations they are consistent with, and within which boundaries they are valid.

### 11.1 Recommended semantic order

#### 1. Brief synthesis of the main findings

- The method/design must be recalled in one or two sentences.
- The two or three most important results must be summarised briefly.
- The Results section must not be rewritten.

#### 2. Interpretation and possible mechanism

- Result and interpretation must be kept separate.
- If the mechanism was not directly tested, formulations such as "may reflect", "is consistent with", "one explanation is" must be used.
- Alternative explanations must be given.

#### 3. Relation to prior work

- It must be explained which literature line the findings support, extend or constrain.
- The respects in which prior work is strong and in which this study is strong must be separated honestly.
- If a multidimensional comparison is central, a reference-supported table may be used.

#### 4. Advantages and disadvantages of the method

- Internal isolation, controls, sample, endpoint and reproducibility must be assessed.
- Model/data quality, assumptions and protocol choices must be discussed.
- The internal consistency of the method and the residual confounds must be explained.

#### 5. Practical implications

- Benefit and harm must be assessed together.
- The recommendation must be limited to the studied population and setting.
- An average gain must not be turned into a universal rule.

#### 6. Validity boundaries

- Internal validity
- Construct validity
- Conclusion validity
- External validity
- Statistical power
- Measurement limitations
- Generalization status

may be assessed separately.

#### 7. Future work

- The focus must be on the most important open questions remaining in the present study.
- The future-work list must be derived directly from the limitations.

### 11.2 Must be done in the Discussion

- The main numbers in the Results must be cited selectively.
- The result on which each interpretation rests must be explicit.
- Alternative explanations must be given honestly.
- Advantages and limitations must be discussed with the same evidential standard.
- Claims must be assessed separately with respect to internal isolation and external generalization.
- Practical implications must be presented together with harms or failure cases.
- Sentences may mostly be impersonal; prior studies may be written with active attribution.

### 11.3 Must not be done in the Discussion

- New results must not be added.
- The Results section must not be repeated number by number.
- A plausible mechanism must not be presented as if it were proven.
- Limitations must not be brushed aside as a formality in a single paragraph.
- A sensitivity analysis must not be presented as an independent replication.
- A comparison table must not be added merely because it "ought to be there".
- Hypothetical claims must not be written with the same status as evidence.
- A practical recommendation must not be given without stating its scope.

---

## 12. Conclusion rules

The Conclusion must be a short, final synthesis containing no new information. For most studies 3--5 paragraphs are sufficient; the venue may require it to be shorter.

### 12.1 Recommended structure

#### Paragraph 1 — What was done?

- The problem and the study design must be given briefly.
- It must be explained what was tested with which comparison or method.

#### Paragraph 2 — What was shown?

- The main findings must be synthesised in the form of a story.
- The contribution must be related directly to the result.
- Not every headline number has to be repeated.

#### Paragraph 3 — Scope and practical meaning

- It must be stated to which population and setting the conclusion is limited.
- The most defensible practical or theoretical implication must be given.

#### Paragraph 4 — Future work

- The 2--4 next steps with the highest value must be given.
- The future work must not conceal the missing controls of the present study.

### 12.2 Must be done in the Conclusion

- The research question must be answered directly.
- The main contribution must be expressed clearly but in measured terms.
- Scope and limitations must be visible.
- Future directions must be derived from evidence gaps.
- The take-home statement may be given in the present tense.

### 12.3 Must not be done in the Conclusion

- New citations must not be added, unless the venue specifically requires it.
- New analyses, numbers, datasets or claims must not be added.
- A conclusion stronger than the abstract must not be constructed.
- The whole Discussion must not be repeated.
- Speculative sentences such as "this study will change the field" must not be used.
- A general law must not be inferred from a single sample or a limited benchmark.

---

## 13. Constructing contribution and originality

A contribution is not constructed merely with the expressions "new", "novel" or "first". Every contribution must be tied to the following matrix:

| Element | Question |
|---|---|
| Problem | Which scientific or operational problem has not been solved in previous studies? |
| Gap | Which ingredient, confound, population or baseline is missing? |
| Response | Which method, control or analysis is presented in this study? |
| Evidence | Which result supports this contribution? |
| Boundary | With which scope is this contribution limited? |

### Contribution types must be separated

- **Methodological contribution:** A new method, instrument, framework or protocol
- **Empirical contribution:** A new result or regularity
- **Theoretical contribution:** A new explanation, formalization or conceptual distinction
- **Evaluation contribution:** A new benchmark, control, baseline or audit design
- **Practical contribution:** An applicable procedure or decision rule
- **Reproducibility contribution:** Code, data, preregistration, audit or artifact

### Must be done

- The contribution list must contain items that are independent of one another.
- Every contribution must be verified with a result or an artifact.
- If a "first" claim is to be used, it must be supported by a systematic, current search.
- The strongest claim must rest on the strongest controlled comparison.

### Must not be done

- The same contribution must not be counted three times in different words.
- Merely using a different dataset must not be presented as the core novelty.
- An ablation or replication that was not carried out must not be written up as a contribution.
- A methodological contribution must not be confused with an empirical finding.
- A disjoint sensitivity result must not be presented as a proof of generalization.

---

## 14. Literature and citation rules

### 14.1 Literature synthesis

The literature must be grouped along the following axes:

- method family,
- task/domain,
- model/population,
- positive vs negative evidence,
- compute regime,
- evaluation design,
- known confounds,
- remaining gap.

#### Must be done

- Primary evidence must be preferred as the direct basis of a claim.
- Reviews and systematic reviews must be used for the synthesis of the field.
- Contradictory findings must be presented in a balanced manner.
- A citation must be placed as close as possible to the sentence it supports.
- Current and authoritative sources must be checked.
- Study-type reporting guidelines must be used.

#### Must not be done

- Citation dumping must not be done.
- A review must not be presented as if it were the direct result of a primary experiment.
- A number or conclusion not present in the source must not be attributed to that source.
- Predatory or unreliable journals must not be used.
- An old and irrelevant source must not be selected merely because its citation count is high.
- The phrase "No prior study" must not be used without a sufficient search.

### 14.2 Citation tense

- An operation performed by a specific study: past simple.
- An ongoing trend across the field: present perfect.
- A theory or definition that is still accepted: present simple.

---

## 15. Statistical and evidential reporting

### 15.1 Fundamental distinctions

- Non-significance **is not absence of effect**.
- No observed difference **is not equivalence**.
- A pooled tie **is not unit-level equality**.
- Direction consistency **is not magnitude replication**.
- Fresh seeds **are not independent population replication**.
- Statistical significance **is not practical importance**.
- Association **is not causation**.
- Strong prediction **is not mechanism proof**.

### 15.2 What must be reported

- Exact $n$
- Unit of analysis
- Effect size
- Confidence interval or uncertainty
- Exact $p$-value, where appropriate
- Multiple-testing correction
- One-sided/two-sided status
- Primary/secondary/descriptive classification
- Missing data and exclusions
- Randomization/seeds
- Heterogeneity and subgroup rules
- Preregistration status
- Deviations and amendments

### 15.3 Claim calibration

| Evidence level | Appropriate wording |
|---|---|
| Descriptive | "X was observed." |
| Association | "X is associated with Y." |
| Controlled attribution | "When A and B were held constant, a difference attributable to component C was observed." |
| Causal effect | If appropriate intervention and confound control are present, "X produced a causal effect on Y." |
| Mechanism | Must be used if competing mechanisms have been directly disentangled. |
| General law | Requires multiple independent settings and replications. |

### 15.4 Must not be done

- A $p$-value must not be given on its own.
- For $p>0.05$, it must not be said that things are "equal" or that there is "no effect".
- An underpowered null result must not be presented as a refutation.
- A post hoc subgroup must not be written up as confirmatory.
- A family-level claim must not be constructed without multiple-comparisons correction.
- A precision claim must not be made without giving a confidence interval.
- An average improvement must not be turned into a universal benefit.

---

## 16. Additional rules for computational, ML and software studies

In these areas the following information can be critical for the interpretation of results and for replication:

- Exact model name and checkpoint
- Model version/digest
- Dataset version and split
- Prompt templates
- Decoding parameters
- Seed construction
- Number of samples/rounds
- Hardware and software versions, if the result or runtime is affected
- Context length and token limits
- Baselines and compute definition
- Training vs inference distinction
- Code execution sandbox
- Evaluation harness
- Public vs hidden tests
- Data leakage checks
- Model/data contamination risk
- Cost and wall-clock metrics, if relevant to the claim
- Code, logs and artifact availability

### Must be done

- "Matched compute" must be operationalized precisely.
- Output-sample equality must not be conflated with total FLOPs equality.
- Because a model family or API version can change, the exact version must be recorded.
- Benchmark contamination and test leakage risks must be discussed.
- If LLM-as-judge is used, the judge model, prompt, calibration and agreement must be given.
- If human evaluation is present, annotator training, blinding, rubric and agreement must be reported.

### Must not be done

- It must not be left at "same model" without specifying version/checkpoint.
- It must not be written as if determinism were guaranteed because a seed was given.
- Public benchmark success must not be presented as real-world deployment readiness.
- If hidden tests were used in sample selection, they must not be labeled as untouched.
- A model output collision must not be automatically interpreted as evidence of data reuse; provenance must be checked.

---

## 17. Figures, tables and equations

### 17.1 Figures

- A figure must not be placed before it is first mentioned in the text.
- Figures must be called out in ascending order.
- The caption must begin with a concise title and must give the details necessary for the figure to be understood.
- A figure must be understandable independently of the main text as far as possible.
- Axes, units, error bars, sample sizes and statistical annotations must be explained.
- Accessible colors and distinguishable markers must be used.
- The same data must not be given unnecessarily as both a table and a figure.

#### Figure functions

- Methods figure: workflow, architecture or study design
- Results figure: effect, trend, uncertainty, comparison or failure pattern
- Discussion figure: only if a conceptual synthesis is genuinely necessary

#### Must not be done

- A long Discussion must not be written inside a caption.
- A causal conclusion not visible in the figure must not be added to the caption.
- Color must not be the sole element carrying information.
- Low resolution or unreadable labels must not be used.
- A figure in Results must not unnecessarily repeat the Methods workflow.

### 17.2 Tables

- The table title must be short and descriptive.
- Units, abbreviations and statistical markers must be explained in footnotes.
- Decimal precision must be consistent.
- Sample size and endpoint must be explicit.
- A table must support the main text and must not replace it.

#### Must not be done

- Table content must not be repeated line by line in the prose.
- Different denominators must not be mixed in the same column without being explicitly stated.
- Cherry-picking must not be done by singling out significant results in bold only.
- A table must not be included as a screenshot.

### 17.3 Equations

- An equation must be introduced by prose.
- Every symbol must be defined.
- Equation punctuation must fit the sentence structure.
- The scientific purpose of the equation must be explained.
- Numbering and cross-references must be consistent.

#### Must not be done

- An equation must not be included as an image.
- Unnecessary equations must not be used merely for a technical appearance.
- Unused variables must not be left in.
- Signs, inequality directions or subscripts must not be altered during editing.

---

## 18. End matter and disclosure sections

The following sections must be assessed according to venue and study type:

### Acknowledgements

- Contributions that do not meet authorship criteria must be stated.
- It must be short and concrete.
- Effusive praise, thanks to reviewers/editors and vague expressions must not be used.

### Funding

- Funder names and grant numbers must be given correctly.
- The funder's role in study design, analysis or publication must be disclosed if the venue requires it.

### Author Contributions

- Each author's contribution must be stated explicitly.
- The CRediT taxonomy may be used.
- A contribution statement does not substitute for authorship criteria.

### Competing Interests / Conflict of Interest

- Financial and non-financial interests must be declared explicitly.
- If there is no conflict, it may be necessary to state this too with an explicit statement.

### Ethics and Consent

- For human/animal research, the committee, approval identifier, relevant standards and consent information must be given.
- For identifiable participant information, publication consent must additionally be addressed.

### Data Availability

- It must be stated where, under which conditions and with which identifier the minimum dataset is accessible.
- If "Available upon reasonable request" is used, the reason and the access conditions must be explained.

### Code Availability

- The code repository, version/tag, license and execution instructions may be given.
- If there is proprietary code, the restriction must be stated explicitly.

### Preregistration and Protocol

- The registry, timestamp, identifier and deviations must be explained.
- An internal version-control timestamp must not be presented as equivalent to a third-party registry.

### Supplementary Information and Appendix

- Content that is mandatory for the main argument must not be pushed into the supplement.
- Reproducibility details, extended tables, proofs, additional analyses and materials may be given here.
- If the venue requires a supplementary file instead of an appendix, that structure must be followed.

### AI-assisted writing declaration

- If venue or institutional policy requires it, the scope of AI tool use must be explained.
- Scientific accuracy, citation verification and authorship responsibility belong to the human authors.

---

## 19. Cross-section semantic consistency

The article must be checked as a **promise-delivery chain**:

| Section | Function |
|---|---|
| Introduction | Promises which problem must be tested and why. |
| Methods | Shows how this problem was tested. |
| Results | Reports what the test produced. |
| Discussion | Explains what the result means and what it does not mean. |
| Conclusion | Gives the most defensible answer to the research question. |

### A single source of truth table must be maintained

At minimum, the following fields must be recorded in a single consistency sheet:

- Research question
- Hypotheses
- Population and sample sizes
- Conditions/arms/groups
- Inclusion/exclusion counts
- Primary and secondary endpoints
- Baselines
- Model/dataset versions
- Exact effect sizes
- Confidence intervals
- $p$-values and corrections
- Tables/figures
- Preregistration status
- Limitations
- Contribution wording

### Cross-section audit questions

- Does every number in the Abstract appear in the Results?
- Has every major promise in the Introduction been tested in the Methods?
- Has every primary analysis in the Methods been reported in the Results?
- Is every interpretation in the Discussion tied to a specific result?
- Is the Conclusion stronger than the Abstract?
- Has the same sample been used under a different name in different sections?
- Has the direction of the baseline changed?
- Has the status of “replication”, “sensitivity” or “validation” shifted?

### Must not be done

- Number drift
- Terminology drift
- Baseline switching
- Endpoint switching
- Sample-status switching
- Discovery-confirmation mixing
- Result-discussion contamination
- Conclusion inflation

---

## 20. LaTeX safety rules

When LaTeX text is edited, the following elements must be preserved:

- `\section`, `\subsection`, `\paragraph`
- `\label`, `\ref`, `\eqref`, `\S\ref`
- `\citep`, `\citet`
- `\begin{...}` / `\end{...}` pairs
- `table`, `figure`, `equation`, `align`, `enumerate`, `itemize`
- Custom macros
- Mathematical symbols and operators
- `\input{...}` and file paths
- Placement specifiers `[t]`, `[h]`, etc.
- Width settings
- Escape characters: `\%`, `\_`, `\&`, `\#`
- Dashes: `--`, `---`

### Must be done

- Environment balance must be checked.
- Duplicate labels must be searched for.
- Undefined refs and citations must be detected.
- Equation punctuation and surrounding prose must be checked.
- Tables and figures must be verified against the order of first callout.
- Custom macros must not be changed without knowing their meaning.

### Must not be done

- A number, sign or inequality direction inside an equation must not be changed during language editing.
- `\citep` and `\citet` must not be converted arbitrarily.
- Table/figure environments must not be removed.
- Macro names must not be renamed for stylistic purposes.
- Special characters such as `%` and `_` must not be left unescaped.
- Technical English terms deliberately used by the author must not be changed on the assumption that they are LaTeX errors.

---

## 21. Things that must never be done

1. Fabricating data or citations
2. Guessing missing method detail
3. Writing a non-significant result as “no effect”
4. Presenting a pooled tie as equivalence
5. Inferring causality from association
6. Proving an internal mechanism from a behavioral result
7. Deriving a general law from a single benchmark
8. Using a stronger claim in the Abstract than in the main text
9. Adding a new result in the Conclusion
10. Explaining causes/mechanisms in the Results
11. Arguing in the Methods that the method was successful
12. Presenting unreported analysis in the Discussion
13. Using different terms for the same concept
14. Giving different numbers for the same quantity
15. Changing the baseline from section to section
16. Calling a sensitivity sample an independent replication
17. Mixing discovery data into confirmatory evidence
18. Using a “first”, “only”, “unprecedented” claim without a search
19. Misrepresenting prior work for the sake of novelty
20. Citation dumping
21. Breaking natural language by making every sentence passive
22. Choosing tenses independently of their rhetorical function
23. Fragmenting the story with excessive headings
24. Repeating every result at the same level of detail in the abstract, introduction, discussion and conclusion
25. Downplaying limitations or presenting them disconnected from the conclusion
26. Equating statistical significance with practical importance
27. Writing an average benefit as uniform safety
28. Contradicting the main text in a figure/table caption
29. Breaking an equation or LaTeX structure
30. Ignoring venue-specific instructions

---

## 22. Editing workflow

A text must not be made “more academic” in a single stage. The following stages must be followed.

### Stage 1 — Venue and study-type check

- The target journal is determined.
- The article type is determined.
- Word, figure, abstract and section limits are extracted.
- The appropriate reporting guideline is selected.

### Stage 2 — Extraction of the scientific skeleton

- Research question
- Hypotheses
- Design
- Population/sample
- Conditions
- Endpoints
- Main results
- Limitations
- Contributions

are extracted as a one-page summary.

### Stage 3 — Consistency sheet

All numbers, terms, models, datasets, symbols and claims are written into a single source-of-truth table.

### Stage 4 — Promise-delivery audit

Introduction promises, Methods tests, Results answers, Discussion interpretations and Conclusion claims are matched to one another.

### Stage 5 — Section-level restructuring

Each section is reordered according to its own epistemic task. Excess subheadings and repetitions are removed.

### Stage 6 — Claim audit

For every claim the following questions are asked:

- Which result supports it?
- Is it confirmatory or descriptive?
- Is causal language appropriate?
- Which confounds are open?
- Which scope is it limited to?

### Stage 7 — Language editing

- The passive/active balance is corrected.
- The tense matrix is applied.
- Long sentences are split.
- Exaggeration and metadiscourse are removed.
- Transitions are strengthened.

### Stage 8 — Citation and evidence audit

- The source of every factual claim is checked.
- Primary vs review sources are separated.
- Unsupported novelty claims are removed.

### Stage 9 — Technical/LaTeX audit

- Environments
- Labels/refs
- Citations
- Equations
- Tables/figures
- Macros
- Escaped characters

are checked.

### Stage 10 — Reverse reading

The article is read backwards from the Conclusion to the Abstract. This reveals claim inflation and promise-delivery mismatches.

---

## 23. Final checklist

### Scientific integrity

- [ ] Is the research question single and clear?
- [ ] Is every headline claim tied to a result?
- [ ] Is causal language appropriate to the design?
- [ ] Have null, tie and equivalence been correctly distinguished?
- [ ] Have descriptive and confirmatory analyses been separated?
- [ ] Do the limitations genuinely narrow the claims?

### Story

- [ ] Does the Introduction proceed from the general to the specific?
- [ ] Does each paragraph prepare the next one?
- [ ] Is the gap testable?
- [ ] Does the current study answer the gap directly?
- [ ] Can the contribution be expressed in a single sentence?

### Section coherence

- [ ] Do the Abstract, Results and Conclusion state the same main finding?
- [ ] Does every primary test in the Methods appear in the Results?
- [ ] Is every interpretation in the Discussion tied to the Results?
- [ ] Does the Conclusion contain new information?
- [ ] Are the sample, baseline and endpoint names consistent?

### Language

- [ ] Is the tense appropriate to its rhetorical function?
- [ ] Is the passive voice natural?
- [ ] Have long sentences been reduced?
- [ ] Have exaggerated adjectives been removed?
- [ ] Are acronyms defined in the right place?
- [ ] Have terms deliberately left in English been preserved?

### Methods and reproducibility

- [ ] Are the population, sample and unit of analysis clear?
- [ ] Are baselines and controls operationally defined?
- [ ] Have seeds/randomization/splits been given?
- [ ] Is the statistical plan adequate?
- [ ] Have deviations and amendments been reported?
- [ ] Is data/code availability clear?

### Figures, tables and equations

- [ ] Is every display item called out in the text?
- [ ] Are the captions understandable on their own?
- [ ] Are the exact $n$, units and symbols defined?
- [ ] Do the prose and the table/figure numbers agree?
- [ ] Have the symbols and assumptions in the equations been explained?

### LaTeX

- [ ] Are all `\begin`/`\end` pairs balanced?
- [ ] Are the labels unique?
- [ ] Are the refs and citations defined?
- [ ] Have the custom macros been preserved?
- [ ] Have the mathematical signs been left unchanged?

---

## 24. A binding instruction that can be given to an LLM or an editor

> Edit this article not only with respect to language, but also with respect to scientific argument, section function and cross-section consistency. First determine the reporting rules appropriate to the target venue and study type. Extract a source-of-truth for the research question, hypotheses, design, population, sample, conditions, endpoints, primary results, limitations and contributions. Establish a promise-delivery chain across the Abstract, Introduction, Methods, Results, Discussion and Conclusion. Organize the Introduction with a chain that proceeds from the general to the specific: problem → prior work → unresolved gap → current study → contributions → scope. Write the Methods so that they are reproducible and result-independent; explain the equations, symbols, assumptions, figures, algorithms and parameters. In the first paragraph of the Results, briefly summarize where and how the tests were performed; then report the primary, secondary and robustness analyses in the predetermined order, with effect size and uncertainty. Do not discuss causes or mechanisms in the Results. In the Discussion, separate result, interpretation, prior work, alternatives, practical implications and validity boundaries from one another. Do not add new information in the Conclusion; synthesize briefly what was done, what was shown, the scope, and the most important future directions. Use an academic, impersonal and measured tone; prefer the passive voice especially in process-focused sentences, but do not construct passive structures that hide the agent or that are artificial. Choose the tense according to rhetorical function: general knowledge present, prior studies past/present perfect, performed methods and observed results past, current implications present. Do not write a non-significant result as no effect, a pooled tie as equivalence, an association as causation, or a plausible explanation as mechanism. Do not fabricate unsupported novelty, citations, numbers or method detail. Do not change technical terms deliberately left in English. Preserve LaTeX commands, citations, labels, refs, macros, equations, tables, figures and environments exactly as they are. Report separately the substantive corrections made and the contradictions that could not be resolved.

---

## 25. General standards relied upon

This ruleset has been prepared in a manner consistent with the following official writing and reporting sources:

- [APA Style: Verb Tense](https://apastyle.apa.org/style-grammar-guidelines/grammar/verb-tense)
- [Nature: Initial Submission and Manuscript Structure](https://www.nature.com/nature/for-authors/initial-submission)
- [Scientific Reports: Submission Guidelines](https://www.nature.com/srep/author-instructions/submission-guidelines)
- [PLOS ONE: Submission Guidelines](https://journals.plos.org/plosone/s/submission-guidelines)
- [ICMJE Recommendations](https://www.icmje.org/recommendations/)
- [EQUATOR Network Reporting Guidelines](https://www.equator-network.org/)
- [CRediT Contributor Role Taxonomy](https://credit.niso.org/)

These sources provide the general framework; before every submission the target journal's current rules must additionally be checked.
