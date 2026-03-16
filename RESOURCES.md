# Resource Library

A curated collection of resources for the GenAI Test Architect journey, organized by phase.

---

## Phase 0: Foundation (Weeks 1-8)

### Python for Testing
- [Real Python](https://realpython.com/)
- [TestDriven.io](https://testdriven.io/)
- [Corey Schafer's Python Tutorials](https://www.youtube.com/@coreyms) (YouTube)

### pytest
- [pytest Documentation](https://docs.pytest.org/)
- [pytest-html](https://github.com/pytest-dev/pytest-html) (HTML report plugin)

---

## Phase 1: LLM Fundamentals (Weeks 9-18)

### Conceptual Understanding
- [Andrej Karpathy: "Intro to Large Language Models"](https://www.youtube.com/watch?v=zjkBMFhNj_g) (YouTube)
- [3Blue1Brown: "How LLMs Work"](https://www.youtube.com/c/3blue1brown) (YouTube)
- [Jay Alammar: The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)

### Tokenization
- [tiktoken](https://github.com/openai/tiktoken) (OpenAI tokenizer library)
- [Anthropic Token Counting](https://docs.anthropic.com/en/docs/build-with-claude/token-counting)

### Official API Documentation
- [OpenAI Platform Docs](https://platform.openai.com/docs/) (Responses API, Structured Outputs, Function Calling)
  - [Responses API Reference](https://platform.openai.com/docs/api-reference/responses)
  - [Structured Outputs Guide](https://platform.openai.com/docs/guides/structured-outputs)
  - [Function Calling Guide](https://platform.openai.com/docs/guides/function-calling)
- [Anthropic Docs](https://docs.anthropic.com/) (Messages API, Claude 4.x)
  - [Messages API Reference](https://docs.anthropic.com/en/api/messages)
  - [Prompt Engineering Guide](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering)
- [Google AI Docs](https://ai.google.dev/gemini-api/docs) (Gemini API)

### Prompt Engineering
- [Anthropic Prompt Engineering](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering)
- [OpenAI Prompt Engineering](https://platform.openai.com/docs/guides/prompt-engineering)

### Evaluation Best Practices
- [OpenAI Evaluation Best Practices](https://platform.openai.com/docs/guides/evaluation-best-practices)

### Security (Introduction)
- [OWASP LLM Top 10 2025](https://genai.owasp.org/llm-top-10/)
- [Promptfoo Red Team Guide](https://www.promptfoo.dev/docs/red-team/)

### LLM Workflows
- [LangChain 1.0 Migration Guide](https://python.langchain.com/docs/versions/migrating_chains/)
- [LangGraph Overview](https://langchain-ai.github.io/langgraph/)

---

## Phase 2: Evaluation Core (Weeks 19-28)

### Free Courses
- [DeepLearning.AI: Automated Testing for LLMOps](https://www.deeplearning.ai/short-courses/automated-testing-llmops/)
- [Evidently AI: LLM Evaluation Course](https://www.evidentlyai.com/ml-observability-course) (theory + applied, free)
- [DeepLearning.AI: Building & Evaluating Advanced RAG](https://www.deeplearning.ai/short-courses/building-evaluating-advanced-rag/)

### Evaluation Guides
- [Eugene Yan: "LLM Evaluations"](https://eugeneyan.com/)
- [Hamel Husain: "LLM Evaluation Guide"](https://hamel.dev/)
- [Hugging Face Evaluation Guidebook](https://github.com/huggingface/evaluation-guidebook)

### Research
- G-Eval paper (LLM-as-Judge methodology)
- Semantic entropy for hallucination detection (Nature 2024)

---

## Phase 3: Frameworks Mastery (Weeks 29-38)

### Tools Documentation
- [DeepEval](https://docs.confident-ai.com/) (v3.8+, 50+ metrics, pytest-native)
  - [GitHub](https://github.com/confident-ai/deepeval) (13,600+ stars)
- [RAGAS](https://docs.ragas.io/) (v0.4.x, RAG evaluation, EACL 2024 cited)
  - [GitHub](https://github.com/explodinggradients/ragas)
- [Promptfoo](https://www.promptfoo.dev/docs/) (OpenAI-acquired March 2026, red-teaming leader)
  - [GitHub](https://github.com/promptfoo/promptfoo)
- [Arize Phoenix](https://docs.arize.com/phoenix/) (observability + evaluation)
  - [GitHub](https://github.com/Arize-ai/phoenix)
- [MLflow GenAI](https://mlflow.org/docs/latest/llms/index.html) (v3.x, Databricks ecosystem)
- [Langfuse](https://langfuse.com/docs) (open-source LangSmith alternative, MIT license)

---

## Phase 4: Agentic AI & Production (Weeks 39-46)

### Agent Frameworks
- [LangGraph Docs](https://langchain-ai.github.io/langgraph/) (primary agent framework, 24,600+ stars)
- [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/)

### Free Courses
- [DeepLearning.AI: Evaluating AI Agents](https://www.deeplearning.ai/short-courses/evaluating-ai-agents/) (with Arize)

### Industry Reports
- [LangChain State of AI Agents Report](https://www.langchain.com/state-of-agent-engineering)

### Security
- [OWASP Top 10 for Agentic Applications](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) (December 2025)

---

## Security & Red Teaming (Optional Track)

- [Garak](https://github.com/NVIDIA/garak) (NVIDIA, ~100 attack vectors)
  - [Documentation](https://garak.readthedocs.io/)
- [Microsoft PyRIT](https://github.com/Azure/PyRIT) (v0.11.0, Azure AI Foundry integration)
- [Promptfoo Red-Teaming](https://www.promptfoo.dev/docs/red-team/) (now OpenAI-backed)

---

## Community Resources

### Blogs & Newsletters
- [Confident AI Blog](https://www.confident-ai.com/blog) (DeepEval, LLM testing)
- [LangChain Blog](https://blog.langchain.dev/) (agents, LangGraph)
- [Anthropic Research Blog](https://www.anthropic.com/research)
- [Simon Willison's Weblog](https://simonwillison.net/) (prompt injection, LLM security)
- [Eugene Yan](https://eugeneyan.com/) (LLM evaluation, MLOps)
- [Jay Alammar](https://jalammar.github.io/) (visual LLM explanations)
- [Sebastian Raschka: "Ahead of AI"](https://magazine.sebastianraschka.com/) (Substack)
- [Latent Space](https://www.latent.space/) (AI engineering)
- [Last Week in AI](https://lastweekin.ai/)

### Certifications (Optional)
- ISTQB CT-AI (AI Testing)
- ISTQB CT-GenAI (Testing with Generative AI)

---

## Paid Resources (Optional)

These are not required but may accelerate learning in specific areas:
- Udemy courses on LLM testing and evaluation (search for latest ratings)
- O'Reilly platform (if employer-sponsored)
