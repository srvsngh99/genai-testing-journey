# 🚀 GenAI Testing Journey: The Complete 52-Week Roadmap

## Philosophy: Depth Over Speed

This roadmap prioritizes **understanding over completion**. Each week has:
- Focused learning (not cramming multiple topics)
- Time to practice and experiment
- A mini-project to solidify concepts
- Space to struggle and figure things out

**The goal isn't to finish fast. It's to finish ready.**

---

## Time Commitment

| Day | Time | Activity |
|-----|------|----------|
| Monday | 1 hr | Learn (videos, docs, reading) |
| Tuesday | 1 hr | Hands-on practice |
| Wednesday | 1 hr | Continue practice + experiments |
| Thursday | 1 hr | Mini-project work |
| Friday | 1 hr | Mini-project work |
| Saturday | 2 hrs | Complete mini-project |
| Sunday | 2 hrs | Review, document, plan next week |

**Total: 9 hours/week** — Sustainable for working professionals

---

## Roadmap Overview

| Phase | Weeks | Focus | Outcome |
|-------|-------|-------|---------|
| 🔵 **Foundation** | 1-8 | Python + Testing Fundamentals | Can write Python test automation |
| 🟣 **LLM Fundamentals** | 9-18 | How LLMs Work + APIs | Understand what you're testing |
| 🟢 **Evaluation Core** | 19-28 | Metrics + RAG + Hallucination | Can evaluate any LLM output |
| 🟡 **Frameworks Mastery** | 29-38 | DeepEval, RAGAS, Promptfoo | Production-ready tooling |
| 🟠 **Agentic AI + Production** | 39-46 | Agents + Monitoring + Scale | Test modern AI systems |
| ⭐ **Capstone** | 47-52 | Build LLMTestKit | Portfolio framework |

### Optional Tracks (Post-52 Weeks)
| Track | Weeks | For Whom |
|-------|-------|----------|
| 🔴 **Security & Red Teaming** | +10 weeks | AI Security careers |
| 🟤 **ML Deep Dive** | +10 weeks | Staff/Principal roles |

---

# 🔵 PHASE 0: Foundation (Weeks 1-8)

## Goal: Python proficiency for LLM testing

Java background helps, but Python patterns for AI/ML are different. Take time to internalize them.

---

### Week 1: Python Basics — Variables, Strings, Numbers

**Why This Matters for AI Testing:**
LLM testing is string manipulation at scale. Prompts are strings. Responses are strings. Everything flows through text.

**Learning Focus:**
- Variables and data types
- String creation, methods, slicing
- f-strings for prompt templates
- Type conversion
- **Bonus:** Basic functions & classes (just enough for project)

**Mini-Project: `prompt-formatter`**
```
Build a prompt template engine that:
├── Takes variables and inserts into templates
├── Validates inputs (not empty, within length)
├── Supports multiple template formats
└── Handles edge cases (special characters, unicode)
```

> **Note:** Week 1's project requires basic functions and classes (Week  3 concepts). The week includes `practice/02_functions_and_classes.py` to teach "just enough" before the project starts.

**Resources:**
- 🎯 Corey Schafer: Python Strings (YouTube)
- 📚 Python official docs: String methods

---

### Week 2: Data Structures — Lists, Dicts, Sets

**Why This Matters for AI Testing:**
Test cases are lists. Results are dictionaries. Unique values need sets. This is your daily bread.

**Learning Focus:**
- Lists: creation, methods, slicing, iteration
- Dictionaries: key-value pairs, nested structures
- Sets: unique values, set operations
- Tuples: immutable sequences
- **Bonus:** Basic functions intro (Day 3 - just enough for project)

**Mini-Project: `test-data-organizer` (Simplified)**
```
Build a test case organizer (single Python file):
├── Store test cases as list of dictionaries (in memory)
├── Add, search, filter test cases
├── Calculate statistics (pass rate, category breakdown)
└── Simple menu-driven interface

Note: JSON export/import moved to Week 5
      Package structure moved to Week 4
```

> **Improvement:** Unlike original plan, Week 2 now teaches basic functions on Day 3 before the project. No "surprise" prerequisites!

---

### Week 3: Control Flow & Functions

**Why This Matters for AI Testing:**
Functions are how you build reusable test utilities. Control flow handles the logic of evaluation.

**Learning Focus:**
- if/elif/else patterns
- for loops, while loops
- List comprehensions
- Function definition, arguments, return values
- *args, **kwargs

**Mini-Project: `llm-response-validator`**
```
Build validation functions:
├── validate_not_empty(response)
├── validate_max_length(response, limit)
├── validate_contains_keywords(response, keywords)
├── validate_json_format(response)
└── validate_no_pii(response)  # Basic patterns
```

---

### Week 4: Modules, Packages, Virtual Environments

**Why This Matters for AI Testing:**
Real projects have multiple files. You need to organize code properly and manage dependencies.

**Learning Focus:**
- Creating modules and packages
- `__init__.py` and imports
- Virtual environments (venv)
- pip and requirements.txt
- Project structure best practices

**Mini-Project: `llm-test-utils`**
```
Create a reusable package:
llm_test_utils/
├── __init__.py
├── validators.py      # From week 3
├── formatters.py      # From week 1
├── test_cases.py      # From week 2
├── helpers.py         # Common utilities
└── requirements.txt
```

---

### Week 5: File Handling & JSON

**Why This Matters for AI Testing:**
Test datasets are JSON/JSONL files. Results are saved as JSON. This is fundamental.

**Learning Focus:**
- Reading/writing text files
- JSON parsing and serialization
- JSONL (JSON Lines) format
- Error handling for file operations
- Path handling with pathlib

**Mini-Project: `dataset-loader`**
```
Build a dataset manager:
├── Load test cases from JSONL
├── Validate schema (required fields)
├── Handle malformed entries gracefully
├── Report statistics
├── Save results back to JSONL
└── Support for multiple dataset formats
```

---

### Week 6: Error Handling & Logging

**Why This Matters for AI Testing:**
LLM APIs fail. Responses are unexpected. Robust error handling is non-negotiable.

**Learning Focus:**
- try/except/finally patterns
- Custom exceptions
- Python logging module
- Log levels and formatting
- Debugging techniques

**Mini-Project: `robust-api-caller`**
```
Build a resilient HTTP caller:
├── Retry logic with exponential backoff
├── Timeout handling
├── Error categorization (retryable vs fatal)
├── Comprehensive logging
└── Rate limit awareness
```

---

### Week 7: pytest Fundamentals

**Why This Matters for AI Testing:**
pytest is the foundation. DeepEval builds on pytest. You'll use it daily.

**Learning Focus:**
- pytest installation and configuration
- Test functions and naming conventions
- Assertions and matchers
- Test discovery
- Running and filtering tests

**Mini-Project: `test-suite-basics`**
```
Write tests for your llm_test_utils package:
├── Test each validator function
├── Test formatters
├── Test dataset loader
├── Test error handling
└── Generate test report
```

---

### Week 8: pytest Advanced — Fixtures & Parametrization

**Why This Matters for AI Testing:**
Fixtures set up test data. Parametrization runs same test with different inputs. Essential for LLM testing.

**Learning Focus:**
- Fixtures: setup/teardown
- Fixture scopes (function, class, module, session)
- Parametrization with @pytest.mark.parametrize
- Conftest.py for shared fixtures
- Markers and skipping tests

**Mini-Project: `parametrized-test-suite`**
```
Enhance your test suite:
├── Fixtures for test data loading
├── Parametrized tests (multiple inputs)
├── Shared fixtures in conftest.py
├── Custom markers for test categories
└── HTML report generation
```

**🎯 Phase 0 Checkpoint:**
- [x] Can write clean Python code
- [x] Understand modules and packages
- [x] Comfortable with JSON/file handling
- [x] Can write pytest tests with fixtures
- [x] Have 8 mini-projects on GitHub

---

# 🟣 PHASE 1: LLM Fundamentals (Weeks 9-18)

## Goal: Understand what you're testing

You can't test what you don't understand. This phase builds mental models for how LLMs work.

---

### Week 9: How LLMs Work — Conceptual Foundation

**Why This Matters:**
You need intuition for WHY LLMs behave the way they do. This informs all testing decisions.

**Learning Focus:**
- What is a language model?
- Training vs inference
- Tokens and tokenization
- Probability and sampling
- Why "temperature" matters

**Mini-Project: `llm-concepts-notebook`**
```
Create a Jupyter notebook documenting:
├── Key LLM concepts in your own words
├── Diagrams/visualizations
├── Examples that demonstrate each concept
├── Common misconceptions
└── Testing implications for each
```

**Resources:**
- 🎯 Andrej Karpathy: "Intro to Large Language Models"
- 🎯 3Blue1Brown: "How LLMs Work"

---

### Week 10: Transformers & Attention — Visual Understanding

**Why This Matters:**
Attention is the core mechanism. Understanding it helps you understand failure modes.

**Learning Focus:**
- Attention mechanism intuition
- Self-attention and cross-attention
- Context windows
- Why transformers work for language

**Mini-Project: `attention-explainer`**
```
Create educational content:
├── Visual explanation of attention
├── Code demo showing attention weights
├── Examples of attention patterns
└── How this relates to testing
```

**Resources:**
- 🎯 3Blue1Brown: "Attention in Transformers"
- 🎯 Jay Alammar: "The Illustrated Transformer"

---

### Week 11: Tokenization Deep Dive

**Why This Matters:**
Tokenization causes many "weird" LLM behaviors. Understanding it prevents confusion during testing.

**Learning Focus:**
- BPE (Byte Pair Encoding)
- tiktoken library
- Token limits and truncation
- Why "strawberry" letter counting fails
- Tokenization edge cases

**Mini-Project: `tokenizer-explorer`**
```
Build an interactive tokenizer tool:
├── Tokenize any text
├── Show token count
├── Visualize token boundaries
├── Compare tokenizers (GPT vs Claude)
├── Document edge cases found
└── Testing implications
```

---

### Week 12: OpenAI API — Your First LLM Integration

**Why This Matters:**
You'll test LLM APIs constantly. Start with the most common one.

**Learning Focus:**
- API setup and authentication
- Chat completions endpoint
- Messages format (system, user, assistant)
- Parameters (temperature, max_tokens, etc.)
- Response parsing

**Mini-Project: `openai-test-client`**
```
Build an OpenAI API wrapper:
├── Clean interface for chat completions
├── Parameter configuration
├── Response parsing and validation
├── Error handling
├── Request/response logging
└── Basic retry logic
```

---

### Week 13: Anthropic Claude API — Multi-Provider Testing

**Why This Matters:**
Real testing often compares models. You need to work with multiple providers.

**Learning Focus:**
- Claude API differences from OpenAI
- Messages format for Claude
- Claude-specific features
- API design patterns across providers

**Mini-Project: `multi-provider-client`**
```
Extend your client to support both:
├── Abstract interface for LLM calls
├── OpenAI implementation
├── Anthropic implementation
├── Consistent response format
├── Provider-specific config handling
└── Easy to add new providers
```

---

### Week 14: Prompt Engineering Fundamentals

**Why This Matters:**
Testing prompts requires understanding prompting. You'll evaluate prompt quality constantly.

**Learning Focus:**
- Zero-shot vs few-shot prompting
- Chain-of-thought (CoT)
- System prompts and their role
- Prompt structure best practices
- Common prompting mistakes

**Mini-Project: `prompt-tester`**
```
Build a prompt experimentation tool:
├── Define prompt variants
├── Run each against test inputs
├── Collect and compare outputs
├── Basic scoring (length, contains expected)
└── Report best performing prompts
```

**Resources:**
- 🎯 promptingguide.ai
- 🎯 Anthropic Prompt Engineering docs

---

### Week 15: LLM Failure Modes — Part 1 (Hallucination)

**Why This Matters:**
This is the #1 thing you'll test for. Understand it deeply.

**Learning Focus:**
- What is hallucination?
- Types: factual, reasoning, citation
- Why hallucinations occur
- Examples and patterns
- Detection approaches

**Mini-Project: `hallucination-examples`**
```
Create a hallucination catalog:
├── Collect 20+ real hallucination examples
├── Categorize by type
├── Document reproduction steps
├── Hypothesize causes
└── Suggest detection methods
```

---

### Week 16: LLM Failure Modes — Part 2 (Inconsistency & Drift)

**Why This Matters:**
Non-determinism is a testing nightmare. Learn to handle it.

**Learning Focus:**
- Why same prompt gives different outputs
- Temperature and sampling effects
- Prompt sensitivity
- Model drift over time
- Statistical approaches to testing

**Mini-Project: `consistency-tester`**
```
Build a consistency analysis tool:
├── Run same prompt N times
├── Measure output variation
├── Statistical analysis (variance, similarity)
├── Visualize consistency
└── Threshold recommendations
```

---

### Week 17: LLM Failure Modes — Part 3 (Edge Cases)

**Why This Matters:**
QA mindset shines here. Apply your edge case thinking to LLMs.

**Learning Focus:**
- Input edge cases (empty, very long, special chars)
- Language edge cases (non-English, code-switching)
- Format edge cases (structured output failures)
- Context edge cases (conflicting information)
- Boundary testing for LLMs

**Mini-Project: `edge-case-generator`**
```
Build an edge case test generator:
├── Categories of edge cases
├── Generate test inputs programmatically
├── Run against LLM
├── Detect failures
└── Report problematic patterns
```

---

### Week 18: LangChain Basics — Understanding Chains

**Why This Matters:**
Many LLM applications use LangChain. Testing chains requires understanding them.

**Learning Focus:**
- What is LangChain?
- PromptTemplates
- Chains and composition
- Output parsers
- When to use LangChain vs raw API

**Mini-Project: `simple-chain-tester`**
```
Build and test a LangChain application:
├── Create a simple chain
├── Write tests for the chain
├── Test intermediate outputs
├── Handle chain failures
└── Compare chain vs raw API
```

**🎯 Phase 1 Checkpoint:**
- [ ] Can explain how LLMs work (in simple terms)
- [ ] Comfortable with OpenAI and Claude APIs
- [ ] Understand tokenization implications
- [ ] Know the major failure modes
- [ ] Have built multi-provider LLM client
- [ ] 10 more mini-projects on GitHub (18 total)

---

# 🟢 PHASE 2: Evaluation Core (Weeks 19-28)

## Goal: Master LLM evaluation metrics and methodology

This is the heart of AI testing. Take your time here.

---

### Week 19: Evaluation Philosophy — What Does "Good" Mean?

**Why This Matters:**
Unlike traditional testing, there's no single "correct" answer. You need evaluation frameworks.

**Learning Focus:**
- Why LLM evaluation is hard
- Reference-based vs reference-free evaluation
- Human vs automated evaluation
- Evaluation dimensions (accuracy, relevance, fluency, safety)
- Choosing what to measure

**Mini-Project: `evaluation-framework-design`**
```
Design an evaluation framework for a chatbot:
├── Define evaluation dimensions
├── Create scoring rubrics
├── Design test case structure
├── Plan human vs automated split
└── Document trade-offs
```

**Resources:**
- 🎯 Eugene Yan: "LLM Evaluations"
- 🎯 Hamel Husain: "LLM Evaluation Guide"

---

### Week 20: Traditional NLP Metrics — The Classics

**Why This Matters:**
These metrics still have their place. Understand when to use them.

**Learning Focus:**
- Exact match
- BLEU score
- ROUGE score
- F1 score (token-level)
- Limitations of each

**Mini-Project: `classic-metrics`**
```
Implement classic metrics from scratch:
├── exact_match(pred, ref)
├── token_f1(pred, ref)
├── simple_bleu(pred, ref)
├── rouge_1(pred, ref)
└── Compare your implementation to libraries
```

---

### Week 21: Semantic Similarity — Beyond Exact Match

**Why This Matters:**
"The capital of France is Paris" and "Paris is France's capital" mean the same thing. Semantic similarity captures this.

**Learning Focus:**
- Text embeddings (what they are)
- Sentence transformers
- Cosine similarity
- When semantic > exact match
- Embedding model selection

**Mini-Project: `semantic-scorer`**
```
Build a semantic similarity evaluator:
├── Generate embeddings (OpenAI or sentence-transformers)
├── Calculate cosine similarity
├── Compare to exact match results
├── Find threshold for "similar enough"
└── Visualize embedding space
```

---

### Week 22: LLM-as-Judge — Using AI to Evaluate AI

**Why This Matters:**
This is the most powerful modern evaluation technique. Understand it deeply.

**Learning Focus:**
- What is LLM-as-Judge?
- G-Eval methodology
- Designing evaluation prompts
- Scoring rubrics
- Biases in LLM judges

**Mini-Project: `llm-judge`**
```
Build an LLM-based evaluator:
├── Create evaluation prompts for different criteria
├── Implement scoring (1-5 scale)
├── Test on sample outputs
├── Compare to human judgments
├── Measure judge consistency
└── Document biases observed
```

**Resources:**
- 🎯 G-Eval paper
- 🎯 Confident AI blog on LLM-as-Judge

---

### Week 23: RAG Fundamentals — What You're Testing

**Why This Matters:**
RAG (Retrieval-Augmented Generation) is everywhere. You must understand it to test it.

**Learning Focus:**
- RAG architecture
- Retrieval: embeddings, vector stores
- Generation: context injection
- The retrieval-generation pipeline
- Where RAG can fail

**Mini-Project: `simple-rag`**
```
Build a minimal RAG system:
├── Create document store (ChromaDB)
├── Implement retrieval
├── Connect to LLM for generation
├── End-to-end query handling
└── Identify failure points
```

---

### Week 24: RAG Evaluation — Retrieval Metrics

**Why This Matters:**
RAG has TWO systems to test: retrieval AND generation. Start with retrieval.

**Learning Focus:**
- Context precision
- Context recall
- Retrieval relevance
- Top-K evaluation
- Ground truth for retrieval

**Mini-Project: `retrieval-evaluator`**
```
Build retrieval evaluation:
├── Create test set with known relevant docs
├── Implement precision@k
├── Implement recall@k
├── Implement MRR (Mean Reciprocal Rank)
└── Generate retrieval quality report
```

---

### Week 25: RAG Evaluation — Generation Metrics

**Why This Matters:**
Even with perfect retrieval, generation can fail. Test it separately.

**Learning Focus:**
- Faithfulness (grounded in context?)
- Answer relevancy (addresses the question?)
- Context utilization
- Hallucination in RAG context

**Mini-Project: `generation-evaluator`**
```
Build generation evaluation:
├── Implement faithfulness check
├── Implement answer relevancy
├── Detect hallucination vs context
├── Score context utilization
└── End-to-end RAG evaluation
```

---

### Week 26: Hallucination Detection — Deep Dive

**Why This Matters:**
This is the most critical evaluation for most applications. Go deep.

**Learning Focus:**
- Intrinsic vs extrinsic hallucination
- Claim extraction
- Claim verification approaches
- NLI (Natural Language Inference) for hallucination
- Building detection pipelines

**Mini-Project: `hallucination-detector`**
```
Build a hallucination detection system:
├── Extract claims from response
├── Verify claims against context
├── Score groundedness
├── Flag unsupported statements
├── Generate detailed report
└── Handle edge cases
```

---

### Week 27: Custom Metrics — Designing Your Own

**Why This Matters:**
Off-the-shelf metrics don't cover everything. You'll need custom metrics for specific use cases.

**Learning Focus:**
- When to build custom metrics
- Metric design principles
- Combining multiple signals
- Calibration and thresholds
- Validating your metric

**Mini-Project: `custom-metric`**
```
Design and build a custom metric:
├── Identify a gap in existing metrics
├── Design the metric (what it measures, how)
├── Implement it
├── Test on labeled data
├── Compare to existing metrics
└── Document usage and limitations
```

---

### Week 28: Evaluation at Scale — Datasets & Automation

**Why This Matters:**
Manual evaluation doesn't scale. Automate everything.

**Learning Focus:**
- Building evaluation datasets
- Synthetic data generation
- Automation strategies
- Statistical significance
- Evaluation pipelines

**Mini-Project: `eval-pipeline`**
```
Build an automated evaluation pipeline:
├── Load test dataset
├── Run LLM on all test cases
├── Apply multiple metrics
├── Aggregate results
├── Generate comprehensive report
└── CI/CD ready
```

**🎯 Phase 2 Checkpoint:**
- [ ] Understand evaluation philosophy
- [ ] Can implement classic + semantic metrics
- [ ] Comfortable with LLM-as-Judge
- [ ] Can evaluate RAG systems end-to-end
- [ ] Built a hallucination detector
- [ ] Created a custom metric
- [ ] 10 more mini-projects (28 total)

---

# 🟡 PHASE 3: Frameworks Mastery (Weeks 29-38)

## Goal: Production-ready tooling with industry-standard frameworks

Now apply your knowledge using the tools companies actually use.

---

### Week 29: DeepEval Setup & First Tests

**Why This Matters:**
DeepEval is "pytest for LLMs" — the most pytest-like LLM testing framework.

**Learning Focus:**
- Installation and configuration
- LLMTestCase structure
- Your first DeepEval test
- Running and viewing results
- Integration with pytest

**Mini-Project: `deepeval-starter`**
```
Set up DeepEval testing:
├── Install and configure
├── Convert previous tests to DeepEval
├── Run and analyze results
├── Understand the output format
└── Document learnings
```

---

### Week 30: DeepEval Metrics — The Full Suite

**Why This Matters:**
DeepEval has 14+ built-in metrics. Know when to use each.

**Learning Focus:**
- Hallucination metric
- Answer relevancy metric
- Faithfulness metric
- Contextual metrics
- Bias and toxicity metrics

**Mini-Project: `deepeval-metrics-explorer`**
```
Explore all DeepEval metrics:
├── Test each metric on sample data
├── Document what each measures
├── Find edge cases for each
├── Create a decision guide (when to use what)
└── Benchmark metric performance
```

---

### Week 31: DeepEval Advanced — Custom Metrics & Datasets

**Why This Matters:**
Real projects need customization. Learn to extend DeepEval.

**Learning Focus:**
- Creating custom metrics in DeepEval
- Building evaluation datasets
- Synthetic data generation with DeepEval
- Confident AI platform integration

**Mini-Project: `deepeval-custom`**
```
Build custom DeepEval components:
├── Create 2 custom metrics
├── Build a domain-specific dataset
├── Generate synthetic test data
├── Integrate all into test suite
└── Push to Confident AI dashboard
```

---

### Week 32: DeepEval CI/CD — Production Integration

**Why This Matters:**
Tests that don't run automatically don't run at all.

**Learning Focus:**
- GitHub Actions for DeepEval
- Test thresholds and gates
- Regression detection
- Reporting and notifications
- Best practices for CI/CD

**Mini-Project: `deepeval-pipeline`**
```
Build a complete CI/CD pipeline:
├── GitHub Actions workflow
├── Run on PR and push
├── Threshold-based pass/fail
├── Generate and upload reports
├── Slack/email notifications
└── Baseline comparison
```

---

### Week 33: RAGAS Fundamentals

**Why This Matters:**
RAGAS is the gold standard for RAG evaluation. Essential knowledge.

**Learning Focus:**
- RAGAS architecture
- Core metrics (faithfulness, relevancy, precision, recall)
- Dataset preparation
- Running evaluations
- Interpreting results

**Mini-Project: `ragas-starter`**
```
Implement RAGAS evaluation:
├── Set up RAGAS
├── Prepare evaluation dataset
├── Run all core metrics
├── Analyze results
└── Compare to your custom RAG evaluator
```

---

### Week 34: RAGAS Advanced — Synthetic Data & Custom Metrics

**Why This Matters:**
RAGAS can generate test data automatically. Powerful for coverage.

**Learning Focus:**
- Synthetic test generation
- Custom metrics in RAGAS
- Integration with other tools
- RAGAS vs DeepEval comparison

**Mini-Project: `ragas-advanced`**
```
Advanced RAGAS usage:
├── Generate synthetic test set
├── Create custom RAGAS metric
├── Compare RAGAS vs DeepEval results
├── Build hybrid evaluation pipeline
└── Document when to use which
```

---

### Week 35: Promptfoo — Prompt Testing & Comparison

**Why This Matters:**
Promptfoo excels at A/B testing prompts. Different tool, different strengths.

**Learning Focus:**
- YAML-based configuration
- Prompt variants
- Model comparison
- Assertions and scoring
- Red team features (preview)

**Mini-Project: `promptfoo-starter`**
```
Set up prompt testing with Promptfoo:
├── Create YAML config
├── Define prompt variants
├── Run comparison tests
├── Analyze results
└── Integrate with CI
```

---

### Week 36: Promptfoo Advanced — Multi-Model & Red Team

**Why This Matters:**
Promptfoo's model comparison and built-in red team features are unique.

**Learning Focus:**
- Testing across multiple models
- Built-in red team probes
- Custom assertions
- Cost tracking
- Integration patterns

**Mini-Project: `promptfoo-advanced`**
```
Advanced Promptfoo usage:
├── Compare 3+ models on same prompts
├── Run red team probes
├── Create custom assertions
├── Track costs across providers
└── Build decision framework
```

---

### Week 37: Tool Comparison & Selection Framework

**Why This Matters:**
You now know 3 frameworks. Know when to use each.

**Learning Focus:**
- DeepEval vs RAGAS vs Promptfoo
- Strengths and weaknesses
- Combination strategies
- Selection criteria
- Migration patterns

**Mini-Project: `tool-benchmark`**
```
Create comprehensive comparison:
├── Same tests across all 3 tools
├── Benchmark: speed, ease, coverage
├── Document strengths/weaknesses
├── Create selection decision tree
└── Build "unified" wrapper (optional)
```

---

### Week 38: First Open Source Contribution

**Why This Matters:**
Contributing to these tools builds credibility and deepens understanding.

**Learning Focus:**
- Finding good first issues
- Understanding codebase structure
- PR process and etiquette
- Getting feedback incorporated
- Building relationships

**Mini-Project: `first-contribution`**
```
Make your first OSS contribution:
├── Find issue in DeepEval/RAGAS/Promptfoo
├── Understand the codebase
├── Implement fix/feature
├── Write tests
├── Submit PR
└── Document the experience
```

**🎯 Phase 3 Checkpoint:**
- [ ] Proficient in DeepEval
- [ ] Proficient in RAGAS
- [ ] Proficient in Promptfoo
- [ ] Can set up CI/CD for LLM testing
- [ ] Know when to use which tool
- [ ] First open source contribution
- [ ] 10 more mini-projects (38 total)

---

# 🟠 PHASE 4: Agentic AI & Production (Weeks 39-46)

## Goal: Test modern AI systems and production concerns

AI is evolving. Agents are the future. Production is where it matters.

---

### Week 39: Agent Architecture — Understanding What You Test

**Why This Matters:**
Agents are fundamentally different from simple LLM calls. Understand the architecture.

**Learning Focus:**
- What is an AI agent?
- ReAct pattern (Reason → Act → Observe)
- Tool/function calling
- Memory and state
- Multi-step planning

**Mini-Project: `agent-anatomy`**
```
Study and document agent architecture:
├── Build a simple ReAct agent
├── Trace execution step-by-step
├── Identify decision points
├── Map failure modes
└── Design testing strategy
```

---

### Week 40: Tool Use Testing

**Why This Matters:**
Agents use tools. Testing tool selection and execution is critical.

**Learning Focus:**
- Function calling APIs
- Tool definition and schema
- Tool selection accuracy
- Parameter extraction
- Error handling in tools

**Mini-Project: `tool-tester`**
```
Build tool testing framework:
├── Define test tools
├── Test tool selection accuracy
├── Test parameter extraction
├── Inject tool failures
├── Measure recovery behavior
└── Generate tool usage report
```

---

### Week 41: Agent Evaluation — Task Completion

**Why This Matters:**
Agents are goal-oriented. Test whether they achieve goals.

**Learning Focus:**
- Task completion metrics
- Trajectory evaluation
- Efficiency metrics (steps, cost)
- Partial success handling
- Evaluation datasets for agents

**Mini-Project: `agent-evaluator`**
```
Build agent evaluation framework:
├── Define task completion criteria
├── Implement trajectory scoring
├── Measure efficiency
├── Handle partial completions
├── Generate agent performance report
```

---

### Week 42: Multi-Agent & Complex Flows

**Why This Matters:**
Real systems have multiple agents collaborating. Test the interactions.

**Learning Focus:**
- Multi-agent architectures
- Agent communication
- Coordination testing
- Conflict detection
- End-to-end flows

**Mini-Project: `multi-agent-tester`**
```
Test multi-agent systems:
├── Build simple multi-agent setup
├── Test inter-agent communication
├── Detect coordination failures
├── Test conflict resolution
└── End-to-end scenario testing
```

---

### Week 43: Production Monitoring — Observability

**Why This Matters:**
Testing doesn't stop at deployment. Production monitoring is ongoing testing.

**Learning Focus:**
- LangSmith for tracing
- Logging best practices
- Metrics to track in production
- Alerting strategies
- Debug workflows

**Mini-Project: `production-monitor`**
```
Build monitoring setup:
├── Integrate LangSmith tracing
├── Define key metrics
├── Set up dashboards
├── Create alerting rules
├── Debug workflow documentation
```

---

### Week 44: Drift Detection & Regression

**Why This Matters:**
LLMs change. Prompts drift. Catch regressions before users do.

**Learning Focus:**
- What is model/prompt drift?
- Baseline establishment
- Drift detection methods
- Automated regression testing
- Alert thresholds

**Mini-Project: `drift-detector`**
```
Build drift detection system:
├── Establish baseline metrics
├── Implement drift detection
├── Automate comparison
├── Generate drift reports
└── Integration with CI/CD
```

---

### Week 45: Performance & Cost Testing

**Why This Matters:**
LLMs are expensive and slow. Test and optimize both.

**Learning Focus:**
- Latency benchmarking
- Throughput testing
- Token usage optimization
- Cost tracking and budgeting
- Caching strategies

**Mini-Project: `perf-cost-tester`**
```
Build performance testing suite:
├── Latency benchmarking tool
├── Throughput tester
├── Token usage analyzer
├── Cost calculator
├── Caching effectiveness tester
└── Optimization recommendations
```

---

### Week 46: Human Evaluation Design

**Why This Matters:**
Automated metrics are proxies. Human evaluation is ground truth.

**Learning Focus:**
- When to use human evaluation
- Task design for annotators
- Inter-annotator agreement
- Combining human + automated
- Scaling human evaluation

**Mini-Project: `human-eval-framework`**
```
Design human evaluation system:
├── Create annotation guidelines
├── Build annotation interface (simple)
├── Calculate agreement metrics
├── Combine with automated scores
└── Document best practices
```

**🎯 Phase 4 Checkpoint:**
- [ ] Understand agent architectures
- [ ] Can test tool use and agents
- [ ] Set up production monitoring
- [ ] Built drift detection
- [ ] Performance and cost testing
- [ ] Human evaluation framework
- [ ] 8 more mini-projects (46 total)

---

# ⭐ PHASE 5: Capstone (Weeks 47-52)

## Goal: Build LLMTestKit — Your Portfolio Framework

Everything comes together. Build something real.

---

### Week 47: Architecture & Design

**Focus:**
- Design framework architecture
- Define core interfaces
- Plan feature set
- Create project structure
- Write design document

**Deliverable:** Design doc + folder structure + core interfaces

---

### Week 48: Core Evaluation Engine

**Focus:**
- Test case model
- Metric registry
- Evaluation runner
- Result aggregation
- Basic reporting

**Deliverable:** Working evaluation engine

---

### Week 49: Built-in Metrics

**Focus:**
- Implement 8-10 metrics
- Hallucination detection
- Relevancy scoring
- Faithfulness checking
- Semantic similarity
- Custom metric support

**Deliverable:** Full metric suite

---

### Week 50: Reporting & CLI

**Focus:**
- HTML report generator
- JSON output
- CLI interface
- Configuration system
- Pretty console output

**Deliverable:** Complete reporting + usable CLI

---

### Week 51: CI/CD Integration & Polish

**Focus:**
- GitHub Action
- Documentation
- Examples
- Tests for the framework
- Edge case handling

**Deliverable:** CI/CD ready + full docs

---

### Week 52: Launch 🚀

**Focus:**
- Final testing
- PyPI publish
- GitHub release
- Launch content
- Community announcement

**Deliverable:** LLMTestKit v1.0 live on PyPI

**🎯 Phase 5 Checkpoint:**
- [ ] LLMTestKit published on PyPI
- [ ] Comprehensive documentation
- [ ] CI/CD GitHub Action
- [ ] 10+ built-in metrics
- [ ] HTML/JSON reporting
- [ ] Community launch post
- [ ] **52 mini-projects complete!**

---

# 🎓 Post-52 Weeks: Optional Specialization Tracks

## 🔴 Track A: Security & Red Teaming (+10 weeks)

*For those targeting AI Security roles*

| Week | Topic | Project |
|------|-------|---------|
| 53 | Garak Introduction | `garak-scanner` |
| 54 | Prompt Injection Deep Dive | `injection-tester` |
| 55 | Jailbreak Testing | `jailbreak-suite` |
| 56 | Custom Garak Probes | `custom-probes` |
| 57 | OWASP LLM Top 10 (Part 1) | `owasp-tester-1` |
| 58 | OWASP LLM Top 10 (Part 2) | `owasp-tester-2` |
| 59 | DeepTeam Red Teaming | `deepteam-harness` |
| 60 | Security Reporting | `security-reporter` |
| 61-62 | Red Team Capstone | `red-team-suite` |

**Career Outcome:** AI Security Engineer, Red Team Specialist

---

## 🟤 Track B: ML Deep Dive (+10 weeks)

*For Staff/Principal roles*

| Week | Topic | Project |
|------|-------|---------|
| 53 | ML Fundamentals & Loss Functions | `ml-basics` |
| 54 | Neural Network Foundations | `nn-from-scratch` |
| 55 | Embeddings Mathematics | `embedding-deep-dive` |
| 56 | Transformer Math | `attention-math` |
| 57 | How Evaluation Metrics Work | `metric-internals` |
| 58 | Build Metric from Scratch | `novel-metric` |
| 59 | Fine-tuning Evaluation | `finetune-eval` |
| 60 | Advanced LLM-as-Judge | `judge-calibration` |
| 61-62 | Research-Grade Evaluation | `research-eval` |

**Career Outcome:** Staff AI Test Architect, Principal Engineer

---

# 📊 Career Outcomes Summary

| Completion | Role |
|------------|------|
| Weeks 1-28 | Junior AI QA Engineer |
| Weeks 1-46 | AI Evaluation Engineer |
| Weeks 1-52 + LLMTestKit | Senior AI Test Engineer |
| + Security Track | AI Security Engineer |
| + ML Track + Visibility | Staff AI Test Architect |
| + OSS + Talks + Network | Principal/Director |

---

# ✅ What You CAN Do After 52 Weeks

1. **Test any LLM-powered application** (chatbots, RAG, agents)
2. **Build evaluation pipelines** (DeepEval, RAGAS, custom)
3. **Detect hallucinations** at scale
4. **Evaluate RAG systems** end-to-end
5. **Test AI agents** (tool use, multi-step, multi-agent)
6. **Set up CI/CD** for LLM testing
7. **Monitor production** LLM systems
8. **Design human evaluations**
9. **Optimize cost and performance**
10. **Build custom evaluation frameworks**

---

# 📅 Milestone Summary

| Week | Milestone |
|------|-----------|
| 8 | Python + pytest proficient |
| 18 | LLM fundamentals complete |
| 28 | Evaluation expert |
| 38 | Framework master + first OSS contribution |
| 46 | Agentic + Production ready |
| 52 | **LLMTestKit launched** 🚀 |

---

*This roadmap respects your time and prioritizes depth. Take each week fully. The destination is worth the journey.*
