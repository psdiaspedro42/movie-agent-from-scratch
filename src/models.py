from typing import Optional, List, Literal
from pydantic import BaseModel

class Movie(BaseModel):
    title: str
    theater: bool
    score: float
    streamings: Optional[List[str]] = None

class AgentResult(BaseModel):
    route: str
    message: str
    prompt: Optional[str] = None
    erro: Optional[str] = None

class TopRoute(BaseModel):
    route: Literal["not_movies", "movies_router"]

class MovieRoute(BaseModel):
    route: Literal["theater", "streaming", "high_score"]