# 🔮 Prompt Quality Scoring Agent (Colab)

Google Colab notebooks for AI-powered prompt evaluation. Two versions available:

## Versions

### Gemini (Free Tier)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rdpgpuvm/prompt-scorer-colab/blob/main/Prompt_Quality_Scoring_Agent.ipynb)

- **Notebook:** `Prompt_Quality_Scoring_Agent.ipynb`
- **Model:** `gemini-2.0-flash`
- **API Key:** `GEMINI_API_KEY`
- **Note:** Free tier has rate limits (may hit quota)

### OpenAI
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rdpgpuvm/prompt-scorer-colab/blob/main/openai_version.ipynb)

- **Notebook:** `openai_version.ipynb`
- **Model:** `gpt-4o-mini`
- **API Key:** `OPENAI_API_KEY`
- **Note:** Requires OpenAI credits

## Quick Start

1. Pick a version above and click **Open in Colab**
2. Set API key in Colab secrets (left sidebar → 🔑 Secrets)
3. Run all cells (Runtime → Run all)

## Import in Your Own Notebook

```python
# Gemini version
!pip install -q langchain langchain-google-genai
!curl -sO https://raw.githubusercontent.com/rdpgpuvm/prompt-scorer-colab/main/colab_import.py
from colab_import import score_prompt, print_score

# OpenAI version
!pip install -q langchain langchain-openai
!curl -sO https://raw.githubusercontent.com/rdpgpuvm/prompt-scorer-colab/main/openai_scorer.py
from openai_scorer import score_prompt, print_score
```

## Files

- `Prompt_Quality_Scoring_Agent.ipynb` — Gemini notebook
- `openai_version.ipynb` — OpenAI notebook
- `scorer.py` — Gemini CLI version
- `openai_scorer.py` — OpenAI CLI version
- `colab_import.py` — Gemini importable module
