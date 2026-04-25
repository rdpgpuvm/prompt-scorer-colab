"""
Colab Importable Module for Prompt Quality Scoring (Gemini version)

Usage in any Colab notebook:
    !pip install -q langchain langchain-google-genai
    !curl -sO https://raw.githubusercontent.com/rdpgpuvm/prompt-scorer-colab/main/colab_import.py
    
    from colab_import import score_prompt, print_score, run_test_prompts
    
    # Set API key
    import os
    os.environ['GEMINI_API_KEY'] = '...'  # or use userdata.get()
    
    # Score one prompt
    result = score_prompt("What is AI?")
    print_score(result)
    
    # Run all test prompts
    run_test_prompts()
"""
import os
import json
import re
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage

SYSTEM_PROMPT = """You are an expert AI prompt engineer. Evaluate the user's prompt on 5 criteria:
1. Clarity — Is the request unambiguous and easy to understand?
2. Specificity/Details — Does it include enough detail (audience, scope, examples)?
3. Context — Is background or situational context provided?
4. Output Format & Constraints — Does it specify desired format, length, or constraints?
5. Persona/Role — Is a role or perspective assigned to the responder?

Score each 0-10. Final score = average. Provide 3 concrete suggestions.

Respond with ONLY valid JSON in this exact format:
{
  "final_score": 7.5,
  "clarity": 8.0,
  "specificity": 7.0,
  "context": 6.0,
  "format_constraints": 8.0,
  "persona": 7.5,
  "feedback": "Your feedback here.",
  "suggestion_1": "First suggestion.",
  "suggestion_2": "Second suggestion.",
  "suggestion_3": "Third suggestion."
}"""

TEST_PROMPTS = [
    "What is AI?",
    "Explain quantum computing.",
    "Write a summary of the French Revolution.",
    "Draft an email to my team about the project delay.",
    "As a fitness coach, create a 4-week workout plan for a beginner who wants to lose weight and has no gym access.",
    "Act as a senior marketing consultant. Draft 5 catchy taglines for sustainable coffee beans targeting millennials who value ethical sourcing.",
    "You are a cybersecurity expert. Write a 500-word blog post explaining zero-trust architecture to C-level executives, including 3 real-world implementation examples and a cost-benefit summary.",
]


def _extract_json(text: str) -> dict:
    matches = re.findall(r'```(?:json)?\s*(.*?)\s*```', text, re.DOTALL)
    if matches:
        return json.loads(matches[0])
    matches = re.findall(r'\{.*\}', text, re.DOTALL)
    if matches:
        return json.loads(matches[0])
    raise ValueError("No JSON found")


def score_prompt(user_prompt: str, api_key: str | None = None) -> dict:
    """Score a single prompt. Auto-fetches API key from env if not provided."""
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0.1,
        api_key=api_key or os.getenv("GEMINI_API_KEY"),
    )
    response = llm.invoke([
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=f"Score this prompt:\n---\n{user_prompt}"),
    ])
    data = _extract_json(response.content)
    return {
        "prompt": user_prompt,
        "final_score": data.get("final_score", 0),
        "criteria_scores": {
            "Clarity": data.get("clarity", 0),
            "Specificity": data.get("specificity", 0),
            "Context": data.get("context", 0),
            "Format": data.get("format_constraints", 0),
            "Persona": data.get("persona", 0),
        },
        "feedback": data.get("feedback", ""),
        "suggestions": [
            data.get("suggestion_1", ""),
            data.get("suggestion_2", ""),
            data.get("suggestion_3", ""),
        ],
    }


def print_score(result: dict):
    """Pretty-print score results."""
    print(f"\n🎯 Final Score: {result['final_score']:.1f}/10\n")
    print("📊 Criteria:")
    for k, v in result["criteria_scores"].items():
        print(f"  {k}: {v:.1f}/10")
    print(f"\n📝 Feedback: {result['feedback']}\n")
    print("💡 Suggestions:")
    for i, s in enumerate(result["suggestions"], 1):
        print(f"  {i}. {s}")


def run_test_prompts():
    """Run all 7 test prompts and print results."""
    for i, prompt in enumerate(TEST_PROMPTS, 1):
        print(f"\n{'═' * 60}")
        print(f"Test {i}: {prompt[:60]}...")
        print('═' * 60)
        result = score_prompt(prompt)
        print_score(result)
