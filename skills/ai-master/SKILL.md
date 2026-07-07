---
name: ai-master
description: "Master AI & Data Orchestrator. Coordinates ML Architecture, Data Engineering, and Advanced Research."
category: engineering
metadata:
  category: master-orchestrator
  triggers: [ai-ml, data-engineering, search, exa, deep-research]
---

# 🤖 AI & Data Master Orchestrator

The technical lead for intelligent systems. This master skill coordinates data pipelines, machine learning models, and deep technical research.

---

## 🧭 Intelligence Strategy
- **Data-Centric**: Quality data is the foundation of effective AI.
- **Representations over Tokens**: Focus on learning data structure and world models (JEPA/EBM), not just sequence prediction.
- **Efficient Inference**: Optimize for latency and cost.
- **Deep Context**: Leverage search and research to ground AI responses.

---

## 🔗 Sub-Discipline Chain (MANDATORY DELEGATION)

When performing AI or data-related tasks, you **MUST** chain to the following sub-skills. Navigate the sub-skills in the sequential order defined below to ensure structured research, data exploration, and model modeling:

### 🔄 Sequential Sub-Skill Pipeline
```
[Exa Search] ──→ [Deep Research] ──→ [AI/ML Architect] ──→ [Fal AI Media]
```


### 1. ML Architecture & Modeling
- **[AI/ML Architect](sub-skills/ai-ml-architect/SKILL.md)** — designs advanced neural architectures (JEPA, EBM) and representation-learning systems in PyTorch. **Use when:** building self-supervised or world-model architectures, or applying/reviewing LeCun-style objective-driven designs. **Not for:** classical tabular ML (use Scikit-Learn) or inference-focused statistics (use Statsmodels).
- **[Scikit-Learn Machine Learning](sub-skills/scikit-learn/SKILL.md)** — classical ML in Python: classification, regression, clustering, model evaluation, and pipelines. **Use when:** training/evaluating estimators on tabular data or composing preprocessing-plus-model pipelines. **Not for:** deep neural architectures (use AI/ML Architect).
- **[Statsmodels Analysis](sub-skills/statsmodels/SKILL.md)** — statistical modeling, estimation, inference, diagnostics, and time-series forecasting. **Use when:** you need p-values, confidence intervals, regression/econometric diagnostics, or ARIMA-style forecasts. **Not for:** black-box prediction without inference (use Scikit-Learn).
- **[Vercel AI SDK](sub-skills/vercel-ai-sdk/SKILL.md)** — builds LLM apps with the Vercel AI SDK (generateText/streamText, useChat/useCompletion, tool calling, streaming UI). **Use when:** wiring streaming text, structured objects, or generative UI into a React/Next.js app.

### 2. Data Engineering & DataFrames
- **[Data Master](sub-skills/data-master/SKILL.md)** — designs scalable data pipelines, warehouses, and real-time streaming architectures (Snowflake, dbt, Spark, Kafka). **Use when:** building or reviewing ETL/ELT, lakehouse, or streaming platforms with reliability and cost-efficiency in mind.
- **[Polars DataFrames](sub-skills/polars/SKILL.md)** — high-performance in-memory DataFrame engineering with lazy evaluation and an Apache Arrow backend. **Use when:** pandas is too slow but data still fits in RAM (roughly 1-100GB ETL). **Not for:** larger-than-RAM datasets (use Dask or Vaex).

### 3. Data Visualization
- **[Plotly Visualizations](sub-skills/plotly/SKILL.md)** — interactive, web-embeddable charts with hover, zoom, and pan. **Use when:** building dashboards, exploratory analysis, or presentation graphics that need interactivity. **Not for:** static publication figures (use matplotlib).
- **[Claude D3.js Visualizations](sub-skills/claude-d3js/SKILL.md)** — bespoke, interactive SVG visualizations with fine-grained data binding in D3.js. **Use when:** you need custom control over data-bound SVG beyond what a charting library offers. **Not for:** quick standard charts (use Plotly).

### 4. Search & Research
- **[Exa Search](sub-skills/exa-search/SKILL.md)** — neural search via Exa MCP across web, code, company, and people intelligence. **Use when:** fetching latest web/news info or finding code examples and API references. **Not for:** multi-theme research report synthesis (use Deep Research).
- **[Tavily Search](sub-skills/tavily-search/SKILL.md)** — Tavily API web search, content extraction, and site crawling for RAG and agents. **Use when:** an agent needs real-time structured web results, URL extraction, or crawling. **Not for:** deep multi-source report synthesis (use Deep Research).
- **[Deep Research](sub-skills/deep-research/SKILL.md)** — multi-source investigation synthesized into cited reports with explicit source attribution. **Use when:** in-depth research, competitive analysis, technology evaluation, or market sizing. **Not for:** quick single-fact lookups (use Exa or Tavily).

### 5. Media & Creative Generation
- **[Fal AI Media](sub-skills/fal-ai-media/SKILL.md)** — unified image, video, and audio generation via fal.ai MCP (text-to-image, text/image-to-video, TTS, video-to-audio). **Use when:** generating media assets from text or image prompts. **Not for:** social campaign strategy/distribution, or when a non-fal provider is required.
- **[Stability AI Media](sub-skills/stability-ai/SKILL.md)** — Stability AI image generation and editing (SD3.5, Ultra, Core): text-to-image, img2img, inpainting, upscale, background removal, search-replace. **Use when:** you specifically need Stable Diffusion image generation or edits. **Not for:** video or audio (use Fal AI Media).
- **[Vizcom AI Rendering](sub-skills/vizcom/SKILL.md)** — transforms product-design sketches into full-fidelity 3D renders. **Use when:** turning rough concept sketches into polished product visualizations.
- **[Visual Emotion Engineer](sub-skills/visual-emotion-engineer/SKILL.md)** — maps color, typography, spacing, and imagery to target emotions, demographics, and conversion goals. **Use when:** visuals must reinforce a specific emotional response or support persuasion rather than act as decoration.

### 6. Scientific & Bioinformatics
- **[Biopython Data Science](sub-skills/biopython/SKILL.md)** — computational molecular biology: sequence manipulation, FASTA/GenBank I/O, NCBI Entrez access, structural bioinformatics, phylogenetics. **Use when:** parsing or analyzing biological sequences or querying biological databases.
- **[Scanpy Genomics](sub-skills/scanpy/SKILL.md)** — scalable single-cell RNA-seq analysis on AnnData (QC, normalization, PCA/UMAP, clustering, marker genes, trajectory). **Use when:** running single-cell transcriptomics workflows.

### 7. Health & Wellness Domain
- **[Claude Ally Health](sub-skills/claude-ally-health/SKILL.md)** — health assistant for medical information analysis, symptom tracking, and wellness guidance. **Use when:** extracting or organizing medical information, or tracking symptoms and wellness metrics.
- **[Rehabilitation Motion Analyzer](sub-skills/rehabilitation-analyzer/SKILL.md)** — analyzes rehabilitation-training data to identify recovery patterns, assess progress, and give personalized recommendations. **Use when:** reviewing rehab training records, functional-recovery trends, or rehab-stage progression.
- **[TCM Analyzer](sub-skills/tcm-analyzer/SKILL.md)** — classifies Traditional Chinese Medicine body-constitution types and gives personalized wellness advice, correlating nutrition, exercise, and sleep data. **Use when:** evaluating a user's TCM constitution data or state.

### 8. Model Probing & Distillation
- **[Behavioral X-Ray](sub-skills/bdistill-behavioral-xray/SKILL.md)** — probes an AI model's behavioral patterns: refusal boundaries, hallucination tendencies, reasoning style, formatting defaults (no API key needed). **Use when:** red-teaming, compliance testing, or profiling a model's behavior. **Not for:** extracting domain facts (use Model Knowledge Extraction).
- **[Model Knowledge Extraction](sub-skills/bdistill-knowledge-extraction/SKILL.md)** — extracts structured domain knowledge from AI models in-session or from local Ollama models (no API key needed). **Use when:** mining or distilling reference data and domain knowledge from an LLM.

---

## 🔄 Sequential Master Chains (Next Recommended Action)

Upon completion of the AI/ML design and data analysis:
- 👉 Recommend calling **[Backend Architect](../backend-architect/SKILL.md)** next to translate the ML models and data pipelines into production-ready API schemas and architectural designs.

---

## 🏗️ Operating Pipeline
1. **Data Ingestion**: Gather and clean relevant datasets.
2. **Analysis**: Use deep research and search to identify patterns.
3. **Modeling**: Design AI architectures and select appropriate models.
4. **Validation**: Test AI outputs for accuracy and performance.
