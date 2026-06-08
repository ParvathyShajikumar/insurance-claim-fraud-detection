import json
import anthropic
import os

from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

def analyse_duplicate(pair):

    record1, record2 = pair

    prompt = f"""
    You are an insurance fraud detection expert.

    Compare these claims:

    Claim 1:
    {record1}

    Claim 2:
    {record2}

    Determine:
    - duplicate_claim
    - possible_fraud
    - fraud_indicators
    - recommended_action

    Return concise valid JSON only.
    """

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=500,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    text_output = response.content[0].text.strip()

    text_output = text_output.replace(
        "```json",
        ""
    )

    text_output = text_output.replace(
        "```",
        ""
    )

    try:
        return json.loads(text_output)

    except:
        return {
            "error": text_output
        }