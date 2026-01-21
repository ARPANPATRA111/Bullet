from pydantic import BaseModel, Field
from typing import List

class BulletResponse(BaseModel):
    """Structure for the AI JSON response."""
    bullets: List[str] = Field(description="List of optimized resume bullet points")