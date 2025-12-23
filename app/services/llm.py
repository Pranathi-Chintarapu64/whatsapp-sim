import os
import logging

try:
    from openai import OpenAI
except ImportError:
    OpenAI = None

logger = logging.getLogger(__name__)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_NAME = os.getenv("OPENAI_MODEL", "gpt-4o-mini")


def generate_llm_response(prompt: str) -> str:
    if not OPENAI_API_KEY or not OpenAI:
        logger.warning("OpenAI not configured. Using mock LLM response.")
        return (
            "Based on your report, consider maintaining a balanced diet, "
            "regular physical activity, and consistent sleep patterns. "
            "Please consult a healthcare professional for personalized advice."
        )

    try:
        client = OpenAI(api_key=OPENAI_API_KEY)
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "You are a helpful health assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        logger.exception("LLM call failed")
        return "Sorry, I couldn't process your request at the moment."
