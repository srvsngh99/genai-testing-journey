# 🚀 GenAI Testing Journey: 52 Weeks to AI Test Developer/Architect

<div align="center">

![Week](https://img.shields.io/badge/Current_Week-9%2F52-blue?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-In_Progress-green?style=for-the-badge)
![Followers](https://img.shields.io/badge/Community-Growing-orange?style=for-the-badge)
[![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube)](https://youtube.com/@SouravAILabs)

**A structured 52-week journey from QA/SDET to GenAI Test Framework Developer**

*Learning in public. Building in public. Growing together.*

[📚 Full Roadmap](#-the-52-week-roadmap) • [🎯 Weekly Progress](#-weekly-progress-tracker) • [📺 YouTube](https://www.youtube.com/@SouravAILabs) • [🔗 LinkedIn](https://www.linkedin.com/in/srv-sngh) • [🤝 Join the Journey](#-join-the-community) • [📖 Resources](#-resources)

</div>

---

## 🎯 What This Is

After 10 years as a Lead SDET, I asked myself: **"How do you test non-deterministic systems?"**

This repository documents my 52-week journey to answer that question — learning GenAI testing in public, building real projects, and sharing everything along the way.

### Why QA Engineers Are Uniquely Positioned for AI Testing

```
Traditional QA Mindset          →    AI Testing Application
─────────────────────────────────────────────────────────────
Think in edge cases             →    Adversarial prompt testing
Break things systematically     →    Red teaming LLMs
"It works on my machine" ≠ OK   →    Non-deterministic output validation
Build automation frameworks     →    LLM evaluation pipelines
Test for regression             →    Prompt drift detection
Validate against requirements   →    Evaluate against metrics
```

---

## 📊 The 52-Week Roadmap

<details>
<summary><b>🔵 Phase 0: Foundation (Weeks 1-8)</b> — Python & Data Handling for AI Testing</summary>

| Week | Focus | Mini-Project | Skills |
|------|-------|--------------|--------|
| 1 | Python Basics | `prompt-formatter` — String manipulation for prompts | Variables, strings, f-strings |
| 2 | Data Structures | `test-data-organizer` — Manage test cases (simplified) | Lists, dicts, sets, basic functions |
| 3 | Functions & Control Flow | `llm-response-validator` — Validate outputs | Functions, loops, error handling |
| 4 | Modules & Packages | `llm-test-utils` — First reusable package | Modules, pip, virtualenv |
| 5 | File Handling & JSON | `dataset-loader` — Load JSONL datasets | JSON, file I/O, validation |
| 6 | Error Handling & Logs | `robust-api-caller` — Resilient API wrapper | try/except, logging, retries |
| 7 | pytest Fundamentals | `test-suite-basics` — Testing your package | pytest basics, assertions |
| 8 | pytest Advanced | `parametrized-test-suite` — Data-driven tests | Fixtures, parametrization |

**Phase Outcome:** Python proficiency for LLM testing, first GitHub projects published.
</details>

<details>
<summary><b>🟣 Phase 1: LLM Fundamentals (Weeks 9-18)</b> — Understanding What You're Testing</summary>

| Week | Focus | Mini-Project | Skills |
|------|-------|--------------|--------|
| 9 | How LLMs Work | `llm-concepts-notebook` — Visualizing concepts | Tokens, temperature, sampling |
| 10 | Transformers | `attention-explainer` — Attention visualization | Attention mechanism, context |
| 11 | Tokenization | `tokenizer-explorer` — Tokenizer deep dive | BPE, tiktoken, limits |
| 12 | OpenAI API | `openai-test-client` — API wrapper | API auth, chat completions |
| 13 | Claude API (Multi-Model) | `multi-provider-client` — Unified interface | Anthropic API, abstraction |
| 14 | Prompt Engineering | `prompt-tester` — Prompt experiments | CoT, few-shot, system prompts |
| 15 | Failure Modes 1 | `hallucination-examples` — Hallucination catalog | Hallucination types |
| 16 | Failure Modes 2 | `consistency-tester` — Inconsistency tests | Non-determinism, drift |
| 17 | Failure Modes 3 | `edge-case-generator` — Edge case suite | Boundary testing, inputs |
| 18 | LangChain Basics | `simple-chain-tester` — Chain testing | Chains, PromptTemplates |

**Phase Outcome:** Understand LLM internals, can interact with APIs, documented failure taxonomy.
</details>

<details>
<summary><b>🟢 Phase 2: Evaluation Core (Weeks 19-28)</b> — Measuring AI Quality</summary>

| Week | Focus | Mini-Project | Skills |
|------|-------|--------------|--------|
| 19 | Eval Philosophy | `evaluation-framework-design` — Rubric design | Evaluation dimensions |
| 20 | Classic Metrics | `classic-metrics` — NLP metrics | F1, BLEU, ROUGE |
| 21 | Semantic Similarity | `semantic-scorer` — Embedding similarity | Embeddings, cosine similarity |
| 22 | LLM-as-Judge | `llm-judge` — AI evaluating AI | G-Eval, rubric scoring |
| 23 | RAG Fundamentals | `simple-rag` — Build minimal RAG | Vector stores, retrieval |
| 24 | RAG Retrieval Eval | `retrieval-evaluator` — Test retrieval | Precision@k, Recall@k |
| 25 | RAG Generation Eval | `generation-evaluator` — Test generation | Faithfulness, relevancy |
| 26 | Hallucination Detection | `hallucination-detector` — Claim verification | Claims extraction, grounding |
| 27 | Custom Metrics | `custom-metric` — Domain specific metric | Metric design, calibration |
| 28 | Eval at Scale | `eval-pipeline` — Automated pipeline | Synthetic data, automation |

**Phase Outcome:** Can evaluate LLM outputs, understand key metrics, first custom metric built.
</details>

<details>
<summary><b>🟡 Phase 3: Frameworks Mastery (Weeks 29-38)</b> — Production-Ready Tooling</summary>

| Week | Focus | Mini-Project | Skills |
|------|-------|--------------|--------|
| 29 | DeepEval Setup | `deepeval-starter` — First DeepEval tests | Installation, basic usage |
| 30 | DeepEval Metrics | `deepeval-metrics-explorer` — All built-in metrics | 14+ metrics mastery |
| 31 | DeepEval Advanced | `deepeval-custom` — Custom metrics & datasets | Custom metric integration |
| 32 | DeepEval CI/CD | `deepeval-pipeline` — GitHub Actions integration | CI/CD for LLM tests |
| 33 | RAGAS Fundamentals | `ragas-starter` — First RAGAS evaluation | Core RAGAS metrics |
| 34 | RAGAS Advanced | `ragas-advanced` — Synthetic data generation | Full RAGAS pipeline |
| 35 | Promptfoo Setup | `promptfoo-starter` — Prompt comparison testing | Promptfoo basics |
| 36 | Promptfoo Advanced | `promptfoo-advanced` — Full A/B testing | Advanced comparisons |
| 37 | Tool Comparison | `tool-benchmark` — Compare all 3 frameworks | Framework selection strategy |
| 38 | Open Source Contribution | `first-contribution` — First PR to a framework | OSS contribution |

**Phase Outcome:** Proficient in DeepEval, RAGAS, and Promptfoo. First OSS contribution merged.
</details>

<details>
<summary><b>� Phase 4: Agentic AI & Production (Weeks 39-46)</b> — Testing Modern Systems</summary>

| Week | Focus | Mini-Project | Skills |
|------|-------|--------------|--------|
| 39 | Agent Architecture | `agent-anatomy` — ReAct pattern study | Agent internals, tracing |
| 40 | Tool Use Testing | `tool-tester` — Test function calling | Tool validation |
| 41 | Agent Evaluation | `agent-evaluator` — Task completion metrics | Trajectory evaluation |
| 42 | Multi-Agent Systems | `multi-agent-tester` — Collaborative agents | Coordination testing |
| 43 | Production Monitoring | `production-monitor` — LangSmith setup | Observability, tracing |
| 44 | Drift Detection | `drift-detector` — Catch regressions | Regression testing |
| 45 | Performance & Cost | `perf-cost-tester` — Latency/Token benchmarks | Load testing, optimization |
| 46 | Human Evaluation | `human-eval-framework` — Annotation systems | Human-in-the-loop |

**Phase Outcome:** Can test complex agentic systems and monitor them in production.
</details>

<details>
<summary><b>⭐ Phase 5: Capstone (Weeks 47-52)</b> — Building LLMTestKit</summary>

| Week | Focus | Capstone Milestone | Deliverable |
|------|-------|--------------------|-------------|
| 47 | Architecture Design | Core framework structure | Design doc, folder structure |
| 48 | Core Evaluation Engine | Test inputs & runner | Working evaluation loop |
| 49 | Built-in Metrics | Suite of 10+ metrics | Metric library |
| 50 | Reporting & CLI | HTML reports, CLI tool | User interface |
| 51 | CI/CD Integration | GitHub Action, Docs | Production ready |
| 52 | Launch | PyPI Publish, Launch Post | **LLMTestKit v1.0** 🚀 |

**Phase Outcome:** LLMTestKit published on PyPI, portfolio-ready open source project.
</details>

<details>
<summary><b>🎓 Optional Tracks (Post-52 Weeks)</b> — Specialization</summary>

### 🔴 Track A: Security & Red Teaming (+10 Weeks)
For those targeting AI Security roles.
*   **Focus:** Prompt Injection, Jailbreaking, Garak, OWASP Top 10.
*   **Key Projects:** `garak-scanner`, `injection-tester`, `red-team-suite`.

### 🟤 Track B: ML Deep Dive (+10 Weeks)
For Staff/Principal engineering roles.
*   **Focus:** Loss functions, Transformer math, building metrics from scratch.
*   **Key Projects:** `nn-from-scratch`, `attention-math`, `novel-metric`.
</details>



---

## 📈 Weekly Progress Tracker

| Phase | Weeks | Status | Progress |
|-------|-------|--------|----------|
| 🔵 Foundation | 1-8 | 🟢 Completed | ██████████ 100% |
| 🟣 LLM Fundamentals | 9-18 | 🟡 In Progress | ░░░░░░░░░░ 0% |
| 🟢 Evaluation Core | 19-28 | ⚪ Not Started | ░░░░░░░░░░ 0% |
| 🟡 Frameworks Mastery | 29-38 | ⚪ Not Started | ░░░░░░░░░░ 0% |
| 🟠 Agentic AI | 39-46 | ⚪ Not Started | ░░░░░░░░░░ 0% |
| ⭐ Capstone | 47-52 | ⚪ Not Started | ░░░░░░░░░░ 0% |

**Overall: Week 9/52** — 17.3% Complete

---

## 🗂️ Repository Structure

```
genai-testing-journey/
├── README.md                    # You are here
├── ROADMAP.md                   # Detailed weekly breakdown
├── PROGRESS.md                  # Detailed progress tracking
├── RESOURCES.md                 # Curated learning resources
│
├── weeks/                       # Weekly learning & projects
│   ├── week-01/
│   │   ├── notes/              # Learning notes
│   │   ├── practice/           # Practice code
│   │   ├── project/            # Mini-project
│   │   └── README.md           # Week summary
│   ├── week-02/
│   └── ...
│
├── projects/                    # Major projects
│   ├── test-suite-v1/          # Week 4 project
│   ├── rag-evaluator/          # Week 20 project
│   ├── red-team-suite/         # Week 42 project
│   └── LLMTestKit/             # Capstone (Weeks 49-52)
│
└── templates/                   # Reusable templates
    ├── test-case-template.json
    ├── evaluation-report.html
    └── weekly-update.md
```

---

## 🤝 Join the Community

**Learning alone is hard. Learning together is fun.**

### Ways to Participate:

1. **⭐ Star the Repo** — The best way to follow the journey.
2. **💬 Join Discussions** — Use the **Discussions tab** to share your weekly progress, find accountability partners, or ask questions.
3. **🍴 Fork & Build** — Don't just read—build! Fork this repo and follow the weekly guides.
4. **📺 Watch & Learn** — I break down complex GenAI testing concepts into simple explanations on [YouTube](https://www.youtube.com/@SouravAILabs).
5. **🔗 Connect** — Share your wins on [LinkedIn](https://www.linkedin.com/in/srv-sngh).

### Community Stats

| Metric | Count |
|--------|-------|
| GitHub Stars | 🌟 Growing |
| Forks | 🍴 Growing |
| Learning Together | 👥 Many! |

---

## 📖 Resources

### Quick Links
- [Full Detailed Roadmap](./ROADMAP.md)
- [Progress Tracker](./PROGRESS.md)
- [Resource Library](./RESOURCES.md)

### Key Tools We'll Master
| Tool | Purpose | Phase |
|------|---------|-------|
| [DeepEval](https://github.com/confident-ai/deepeval) | LLM evaluation framework | Phase 3 |
| [RAGAS](https://github.com/explodinggradients/ragas) | RAG evaluation | Phase 3 |
| [Promptfoo](https://github.com/promptfoo/promptfoo) | Prompt testing | Phase 3 |
| [Garak](https://github.com/NVIDIA/garak) | LLM vulnerability scanning | Phase 4 |
| [LangSmith](https://smith.langchain.com/) | LLM observability | Phase 3 |

### Essential Blogs
- [Jay Alammar](https://jalammar.github.io/) — Visual LLM explanations
- [Simon Willison](https://simonwillison.net/) — Prompt injection, LLM security
- [Eugene Yan](https://eugeneyan.com/) — LLM evaluation, MLOps
- [Confident AI Blog](https://www.confident-ai.com/blog) — LLM testing practices

---

## 📝 License

This project is licensed under the MIT License — feel free to use, modify, and share.

---

## 🙏 Acknowledgments

Special thanks to:
- The QA community for the incredible support on Day 1
- [Confident AI](https://confident-ai.com) for DeepEval
- [NVIDIA](https://nvidia.com) for Garak
- Everyone learning in public

---

<div align="center">

**Week 9/52— The journey of a thousand miles begins with a single step.**

*Started: January 2026 | Target Completion: January 2027*

[![LinkedIn](https://img.shields.io/badge/Follow_the_Journey-LinkedIn-0077B5?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/srv-sngh)
[![YouTube](https://img.shields.io/badge/Subscribe-YouTube-FF0000?style=for-the-badge&logo=youtube)](https://youtube.com/@SouravAILabs)

</div>
