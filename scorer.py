"""
Prompt Quality Scoring Agent - Standalone module (Gemini version)
Requires: pip install langchain langchain-google-genai
Usage: GEMINI_API_KEY=... python scorer.py "Your prompt here"
"""
import os
import json
import re
import sys
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


def extract_json(text: str) -> dict:
    pattern = r'```(?:json)?\s*(.*?)\s*```'
    matches = re.findall(pattern, text, re.DOTALL)
    if matches:
        return json.loads(matches[0])
    pattern = r'\{.*\}'
    matches = re.findall(pattern, text, re.DOTALL)
    if matches:
        return json.loads(matches[0])
    raise ValueError("No JSON found")


def score_prompt(user_prompt: str, api_key: str | None = None) -> dict:
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0.1,
        api_key=api_key or os.getenv("GEMINI_API_KEY"),
    )
    response = llm.invoke([
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=f"Score this prompt:\n---\n{user_prompt}"),
    ])
    data = extract_json(response.content)
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
    print(f"\n🎯 Final Score: {result['final_score']:.1f}/10\n")
    print("📊 Criteria:")
    for k, v in result["criteria_scores"].items():
        print(f"  {k}: {v:.1f}/10")
    print(f"\n📝 Feedback: {result['feedback']}\n")
    print("💡 Suggestions:")
    for i, s in enumerate(result["suggestions"], 1):
        print(f"  {i}. {s}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: GEMINI_API_KEY=... python scorer.py 'Your prompt here'")
        sys.exit(1)
    result = score_prompt(sys.argv[1])
    print_score(result)
