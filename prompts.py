SYSTEM_PROMPT = """You are an expert resume writer specializing in tech industry resumes.

STRICT RULES YOU MUST FOLLOW:
1. NEVER invent metrics, percentages, or numbers unless explicitly provided by the user
2. NEVER use vague phrases like "significantly improved" or "greatly enhanced"
3. ALWAYS start each bullet with a strong action verb
4. NEVER include soft skills without concrete examples
5. Use industry-standard terminology appropriate for the role
6. Avoid buzzwords and fluff - be specific and concrete
7. Do not repeat the same action verb across bullets

FORMAT REQUIREMENTS:
- Each bullet on its own line
- Start each bullet with "•" followed by a space
- No numbering, no extra formatting
- No explanations or commentary - just the bullets"""

def build_generation_prompt(
    description: str,
    tech_stack: str,
    experience_level: str,
    target_role: str,
    bullet_style: str,
    bullet_count: int = 3,
    bullet_length: str = "Medium (15-25 words)"
) -> str:
    
    # Parse bullet length
    length_instructions = {
        "Short (10-15 words)": "Keep each bullet between 10-15 words. Be extremely concise.",
        "Medium (15-25 words)": "Keep each bullet between 15-25 words for optimal readability.",
        "Long (25-35 words)": "Each bullet should be 25-35 words, providing more detail and context."
    }
    
    # Style-specific instructions that produce visibly different outputs
    style_instructions = {
        "ATS Optimized": """
STYLE: ATS OPTIMIZED
- Include relevant keywords that match job descriptions
- Use standard industry terminology (no creative synonyms)
- Mention specific technologies, tools, and methodologies
- Structure: Action Verb + Task + Technology/Method + Context""",
        
        "Concise": """
STYLE: CONCISE
- Focus on one key achievement per bullet
- Remove all unnecessary words
- Structure: Action Verb + Core Achievement + Key Technology""",
        
        "Impact-Focused": """
STYLE: IMPACT-FOCUSED
- Lead with the outcome or contribution
- Emphasize what was delivered or improved
- Show scope (team size, user base, system scale) if mentioned
- Structure: Action Verb + Outcome/Contribution + How/Using What"""
    }
    
    experience_guidance = {
        "Beginner": "Use foundational action verbs (Developed, Created, Assisted, Learned, Built). Focus on learning and contribution to team efforts.",
        "Intermediate": "Use growth-oriented verbs (Designed, Implemented, Optimized, Led, Collaborated). Show ownership of features or components.",
        "Advanced": "Use leadership verbs (Architected, Spearheaded, Mentored, Drove, Established). Emphasize strategic impact and technical leadership."
    }
    
    prompt = f"""Convert this raw description into exactly {bullet_count} professional resume bullet points.

RAW DESCRIPTION:
{description}

TECHNOLOGIES USED: {tech_stack if tech_stack else "Not specified"}

TARGET ROLE: {target_role if target_role else "Software Engineer"}

EXPERIENCE LEVEL: {experience_level}
{experience_guidance.get(experience_level, experience_guidance["Intermediate"])}

{style_instructions.get(bullet_style, style_instructions["ATS Optimized"])}

LENGTH REQUIREMENT: {length_instructions.get(bullet_length, length_instructions["Medium (15-25 words)"])}

IMPORTANT REMINDERS:
- Only include information that can be derived from the description
- Do not fabricate metrics or statistics
- Each bullet must be distinct and cover different aspects
- Adapt technical depth to the experience level

Generate exactly {bullet_count} bullet points now:"""

    return prompt


def build_rewrite_prompt(original_bullet: str, rewrite_style: str) -> str:
    
    style_instructions = {
        "Shorter": """Rewrite this bullet to be more concise:
- Reduce to under 15 words
- Keep only the most important information
- Preserve the core achievement and key technology
- Maintain professional tone""",
        
        "More Technical": """Rewrite this bullet with more technical depth:
- Add specific technical details where appropriate
- Include methodology or approach if relevant
- Use precise technical terminology
- Do NOT add technologies not implied by the original""",
        
        "More Impact-Focused": """Rewrite this bullet to emphasize impact:
- Lead with the outcome or result
- Show the value delivered
- Connect the work to business or user benefit
- Do NOT invent metrics or numbers"""
    }
    
    prompt = f"""Rewrite this resume bullet point.

ORIGINAL BULLET:
{original_bullet}

{style_instructions.get(rewrite_style, style_instructions["Shorter"])}

RULES:
- Return ONLY the rewritten bullet
- Start with "•" followed by a space
- Preserve the core meaning
- No explanations or alternatives

Rewritten bullet:"""

    return prompt


def build_quality_check_prompt(bullets: list[str]) -> str:
    bullets_text = "\n".join(bullets)
    
    prompt = f"""Evaluate these resume bullets for quality issues.

BULLETS:
{bullets_text}

Check for these problems:
1. Vague language without specifics
2. Made-up metrics or percentages
3. Repeated action verbs
4. Too long (over 30 words)
5. Missing action verb at start
6. Buzzwords without substance

Respond with ONLY one word:
- "PASS" if all bullets are acceptable
- "FAIL" if any bullet has issues

Your assessment:"""

    return prompt
