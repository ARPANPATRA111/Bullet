SYSTEM_PROMPT = """You are an expert technical resume writer. 
Your goal is to transform raw descriptions into high-impact, ATS-friendly bullet points.
You MUST output valid JSON only."""

def build_generation_prompt(
    description: str,
    tech_stack: str,
    experience_level: str,
    target_role: str,
    style: str,
    count: int,
    length: str
) -> str:
    
    return f"""
    TASK: Generate {count} professional resume bullet points.
    
    CONTEXT:
    - Role: {target_role}
    - Experience Level: {experience_level}
    - Tech Stack: {tech_stack}
    - User Input: "{description}"
    
    STRICT CONSTRAINTS:
    1. STYLE: {style}
    2. LENGTH GOAL: {length} 
       (CRITICAL: If the user asks for 'Long' bullets, you MUST expand on the 'how' and 'why' to meet the word count. If they ask for 'Short', cut all fluff.)
    3. FORMAT: Start with a strong action verb. No "I" or "We".
    4. ACCURACY: Do not invent numbers. If input implies impact, describe the *type* of impact (e.g. "improving latency") without making up a %.
    
    OUTPUT FORMAT:
    Return a JSON object with a single key "bullets" containing a list of strings.
    Example: {{ "bullets": ["Action verb + task + tool + result..."] }}
    """

def build_rewrite_prompt(bullet: str, style: str) -> str:
    return f"""
    TASK: Rewrite this resume bullet.
    
    ORIGINAL: "{bullet}"
    GOAL: Make it {style}.
    
    OUTPUT FORMAT:
    Return a JSON object with a single key "bullets" containing a list with exactly one string.
    """