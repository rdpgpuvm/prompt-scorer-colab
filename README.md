# 🔮 Prompt Quality Scoring Agent (Colab)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rdpgpuvm/prompt-scorer-colab/blob/main/Prompt_Quality_Scoring_Agent.ipynb)

Google Colab notebook for AI-powered prompt evaluation using LangChain + Google Gemini.

## Quick Start

### Option 1: Open in Colab (Recommended)
Click the badge above or go to:  
https://colab.research.google.com/github/rdpgpuvm/prompt-scorer-colab/blob/main/Prompt_Quality_Scoring_Agent.ipynb

### Option 2: Import in Your Own Notebook
```python
# In any Colab notebook, run:
!pip install -q langchain langchain-google-genai
!curl -sO https://raw.githubusercontent.com/rdpgpuvm/prompt-scorer-colab/main/colab_import.py
from colab_import import score_prompt, print_score

# Set your API key
import os
os.environ['GEMINI_API_KEY'] = '...'  # or use Colab secrets

# Score any prompt
result = score_prompt("Your prompt here")
print_score(result)
```

### Option 3: Clone & Run Locally
```bash
git clone https://github.com/rdpgpuvm/prompt-scorer-colab.git
cd prompt-scorer-colab
pip install langchain langchain-google-genai
GEMINI_API_KEY=... python scorer.py "Your prompt here"
```

## Setup

1. Get a Gemini API key: https://aistudio.google.com/app/apikey
2. In Colab: Left sidebar → 🔑 Secrets → Add `GEMINI_API_KEY`
3. Run all cells

## How It Works

- Uses **LangChain** with `ChatGoogleGenerativeAI` (gemini-1.5-flash)
- Evaluates prompts on 5 criteria: Clarity, Specificity, Context, Format, Persona
- Returns structured scores + actionable suggestions
- API key handled via Colab secrets (secure, no hardcoding)

## Files

- `Prompt_Quality_Scoring_Agent.ipynb` — Main notebook (Colab-ready)
- `scorer.py` — Standalone CLI version
- `colab_import.py` — Importable module for any notebook
- `README.md` — This file
