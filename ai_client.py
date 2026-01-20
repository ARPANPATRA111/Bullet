import os
from openai import OpenAI
from dotenv import load_dotenv

from config import TEMPERATURE, MAX_RETRIES
from prompts import SYSTEM_PROMPT, build_generation_prompt, build_rewrite_prompt
from validators import parse_bullets, check_bullet_quality

# Load environment variables from .env file
load_dotenv()

def get_ai_client() -> OpenAI:
    api_key = os.getenv("GROQ_API_KEY")
    
    if not api_key:
        raise ValueError("GROQ_API_KEY not found in environment variables. Please check your .env file.")
    
    # Groq uses OpenAI-compatible API
    client = OpenAI(
        api_key=api_key,
        base_url="https://api.groq.com/openai/v1"
    )
    
    return client


def call_ai(system_prompt: str, user_prompt: str) -> str:
    client = get_ai_client()
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",  # Groq's Llama model
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=TEMPERATURE,
        max_tokens=500  # Sufficient for 3 bullet points
    )
    
    return response.choices[0].message.content.strip()


def generate_bullets(
    description: str,
    tech_stack: str,
    experience_level: str,
    target_role: str,
    bullet_style: str,
    bullet_count: int = 3,
    bullet_length: str = "Medium (15-25 words)"
) -> tuple[list[str], str]:

    user_prompt = build_generation_prompt(
        description=description,
        tech_stack=tech_stack,
        experience_level=experience_level,
        target_role=target_role,
        bullet_style=bullet_style,
        bullet_count=bullet_count,
        bullet_length=bullet_length
    )
    
    attempts = 0
    last_error = ""
    bullets = []
    
    while attempts <= MAX_RETRIES:
        try:
            response = call_ai(SYSTEM_PROMPT, user_prompt)
            bullets = parse_bullets(response, bullet_count)
            passes, issue = check_bullet_quality(bullets, bullet_count)
            
            if passes:
                return bullets, ""

            last_error = issue
            attempts += 1
            
        except ValueError as e:
            return [], str(e)
        
        except Exception as e:
            # API or network error
            return [], f"Failed to generate bullets: {str(e)}"
    
    if bullets:
        return bullets, f"Note: {last_error}. Results may need manual review."
    
    return [], "Failed to generate quality bullets after multiple attempts."


def rewrite_bullet(original_bullet: str, rewrite_style: str) -> tuple[str, str]:
    
    user_prompt = build_rewrite_prompt(original_bullet, rewrite_style)
    
    # Simplified system prompt for rewriting
    rewrite_system = """You are a resume writing expert. Rewrite the given bullet point exactly as instructed.
Return ONLY the rewritten bullet, nothing else. Start with the bullet character "•"."""
    
    try:
        response = call_ai(rewrite_system, user_prompt)
        rewritten = response.strip()
        # Remove bullet prefix for consistency
        for prefix in ["•", "-", "*"]:
            if rewritten.startswith(prefix):
                rewritten = rewritten[len(prefix):].strip()
                break
        
        if len(rewritten) < 10:
            return "", "Rewrite failed - response too short"
        
        return rewritten, ""
        
    except ValueError as e:
        return "", str(e)
    
    except Exception as e:
        return "", f"Failed to rewrite bullet: {str(e)}"
