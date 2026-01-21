import os
import json
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

from config import MODEL_NAME, TEMPERATURE, MAX_RETRIES
from prompts import SYSTEM_PROMPT, build_generation_prompt, build_rewrite_prompt
from schemas import BulletResponse

load_dotenv()

class AIService:
    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("GROQ_API_KEY is missing. Please check your .env file.")
        
        self.client = OpenAI(
            api_key=api_key,
            base_url="https://api.groq.com/openai/v1"
        )

    def _call_llm(self, user_prompt: str) -> list[str]:
        try:
            response = self.client.chat.completions.create(
                model=MODEL_NAME,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=TEMPERATURE,
                response_format={"type": "json_object"}
            )
            
            content = response.choices[0].message.content
            data = json.loads(content)
            validated = BulletResponse(**data)
            return validated.bullets
            
        except json.JSONDecodeError:
            raise Exception("AI response error. Please try again.")
        except Exception as e:
            raise Exception(f"API Error: {str(e)}")

    def generate_bullets(self, **kwargs) -> list[str]:
        prompt = build_generation_prompt(**kwargs)
        return self._call_llm(prompt)

    def rewrite_bullet(self, bullet: str, style: str) -> str:
        prompt = build_rewrite_prompt(bullet, style)
        results = self._call_llm(prompt)
        return results[0] if results else bullet

@st.cache_resource
def get_ai_service():
    try:
        return AIService()
    except ValueError as e:
        st.error(str(e))
        return None