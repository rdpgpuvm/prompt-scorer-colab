# 🔮 Prompt Quality Scoring Agent (Colab)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rdpgpuvm/prompt-scorer-colab/blob/main/Prompt_Quality_Scoring_Agent.ipynb)

Google Colab notebook for AI-powered prompt evaluation using LangChain + OpenAI.

## Quick Start

### Option 1: Open in Colab (Recommended)
Click the badge above or go to:  
https://colab.research.google.com/github/rdpgpuvm/prompt-scorer-colab/blob/main/Prompt_Quality_Scoring_Agent.ipynb

### Option 2: Import in Your Own Notebook
```python
# In any Colab notebook, run:
!pip install -q langchain langchain-openai
!curl -sO https://raw.githubusercontent.com/rdpgpuvm/prompt-scorer-colab/main/scorer.py
from scorer import score_prompt, print_score

# Set your API key
import os
os.environ['OPENAI_API_KEY'] = 'sk-...'  # or use Colab secrets

# Score any prompt
result = score_prompt("Your prompt here")
print_score(result)
```

### Option 3: Clone & Run Locally
```bash
git clone https://github.com/rdpgpuvm/prompt-scorer-colab.git
cd prompt-scorer-colab
pip install langchain langchain-openai
OPENAI_API_KEY=sk-... python scorer.py "Your prompt here"
```

## How It Works

- Uses **LangChain** with `ChatOpenAI` (gpt-4o-mini)
- Evaluates prompts on 5 criteria: Clarity, Specificity, Context, Format, Persona
- Returns structured scores + actionable suggestions
- API key handled via Colab secrets (secure, no hardcoding)

## Test Prompts Included

7 pre-loaded prompts from weak ("What is AI?") to strong (cybersecurity expert blog post).

## Files

- `Prompt_Quality_Scoring_Agent.ipynb` — Main notebook (Colab-ready)
- `scorer.py` — Importable Python module
- `README.md` — This file
