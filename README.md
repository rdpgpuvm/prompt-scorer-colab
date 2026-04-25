# 🔮 Prompt Quality Scoring Agent (Colab)

Google Colab notebook for AI-powered prompt evaluation using LangChain + OpenAI.

## Quick Start

1. Open the notebook in Colab: [Open in Colab](https://colab.research.google.com/github/rdpgpuvm/prompt-scorer-colab/blob/main/Prompt_Quality_Scoring_Agent.ipynb)
2. Set your `OPENAI_API_KEY` in Colab secrets (left sidebar → 🔑 Secrets)
3. Run all cells (Runtime → Run all)

## How It Works

- Uses **LangChain** with `ChatOpenAI` (gpt-4o-mini)
- Evaluates prompts on 5 criteria: Clarity, Specificity, Context, Format, Persona
- Returns structured scores + actionable suggestions
- API key handled via Colab secrets (secure, no hardcoding)

## Test Prompts Included

7 pre-loaded prompts from weak ("What is AI?") to strong (cybersecurity expert blog post).

## Files

- `Prompt_Quality_Scoring_Agent.ipynb` — Main notebook
- `scorer.py` — Standalone Python module (optional)
