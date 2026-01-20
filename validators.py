from config import MIN_DESCRIPTION_LENGTH, MIN_DESCRIPTION_WORDS


def validate_description(description: str) -> tuple[bool, str]:

    # Check for empty input
    if not description or not description.strip():
        return False, "Please enter a description of your project or work experience."
    
    cleaned = description.strip()
    
    # Check minimum length
    if len(cleaned) < MIN_DESCRIPTION_LENGTH:
        return False, f"Description is too short. Please provide at least {MIN_DESCRIPTION_LENGTH} characters to generate meaningful bullets."
    
    # Check minimum word count
    words = cleaned.split()
    if len(words) < MIN_DESCRIPTION_WORDS:
        return False, f"Please provide more detail. At least {MIN_DESCRIPTION_WORDS} words are needed to understand your work."
    
    return True, ""


def validate_tech_stack(tech_stack: str) -> str:

    if not tech_stack:
        return ""
    
    # Split, clean, and rejoin
    techs = [t.strip() for t in tech_stack.split(",") if t.strip()]
    return ", ".join(techs)


def validate_target_role(target_role: str) -> str:

    if not target_role or not target_role.strip():
        return "Software Engineer"
    return target_role.strip()


def parse_bullets(ai_response: str, max_bullets: int = 3) -> list[str]:

    if not ai_response:
        return []
    
    bullets = []
    lines = ai_response.strip().split("\n")
    
    for line in lines:
        line = line.strip()
        
        # Skip empty lines
        if not line:
            continue
        
        # Remove common bullet prefixes
        for prefix in ["•", "-", "*", "1.", "2.", "3.", "4.", "5.", "1)", "2)", "3)", "4)", "5)"]:
            if line.startswith(prefix):
                line = line[len(prefix):].strip()
                break
        
        # Skip if line is too short to be a bullet
        if len(line) < 10:
            continue
        
        bullets.append(line)
    
    return bullets[:max_bullets]  # Return at most max_bullets


def check_bullet_quality(bullets: list[str], expected_count: int = 3) -> tuple[bool, str]:

    if len(bullets) < expected_count:
        return False, f"Failed to generate {expected_count} distinct bullets"
    
    # Check for very short bullets
    for i, bullet in enumerate(bullets):
        if len(bullet.split()) < 5:
            return False, f"Bullet {i+1} is too short"
    
    # Check for duplicate bullets
    if len(set(bullets)) != len(bullets):
        return False, "Duplicate bullets detected"
    
    # Check that bullets start with capital letter (likely action verb)
    for i, bullet in enumerate(bullets):
        if not bullet[0].isupper():
            return False, f"Bullet {i+1} doesn't start with an action verb"
    
    # Check for overly long bullets
    for i, bullet in enumerate(bullets):
        if len(bullet.split()) > 40:
            return False, f"Bullet {i+1} is too long"
    
    return True, ""


def is_input_too_verbose(description: str) -> bool:

    words = description.split()
    return len(words) > 500
