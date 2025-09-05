import random
from typing import Dict, Any
from .models import AgentResult
from .db import MOVIES_DB

def not_movies(ctx: Dict[str, Any]) -> AgentResult:
    return AgentResult(
        route="not_movies",
        message="I'm quite sure this is not about movies",
        prompt=ctx.get("prompt")
    )

def theater_movies(ctx: Dict[str, Any]) -> AgentResult:
    movies_in_theater = [m for m in MOVIES_DB if m.theater]
    
    if not movies_in_theater:
        return AgentResult(
            route="theater",
            message="No theatrical releases found",
            prompt=ctx.get("prompt")
        )
    
    movie = random.choice(movies_in_theater)

    return AgentResult(
        route="theater",
        message=f"movie in theater: {movie.title}, score: {movie.score}",
        prompt=ctx.get("prompt")
    )

def streaming_movies(ctx: Dict[str, Any]) -> AgentResult:
    movies_in_streaming = [m for m in MOVIES_DB if m.streamings]
    
    if not movies_in_streaming:
        return AgentResult(
            route="streaming",
            message="No streaming movies avalaible",
            prompt=ctx.get("prompt")
        )
    
    movie = random.choice(movies_in_streaming)
    
    return AgentResult(
        route="streaming",
        message=f"movie: {movie.title}, streamings: {movie.streamings}, score: {movie.score}",
        prompt=ctx.get("prompt")
    )

def high_score_movies(ctx: Dict[str, Any]) -> Dict[str, Any]:
    movies_high_score = [m for m in MOVIES_DB if m.score >= 8]

    if not movies_high_score:
        return AgentResult(
            route="high_score",
            message="High score (>=8) movies not found",
            prompt=ctx.get("prompt")
        )
        
    movie = random.choice(movies_high_score)
    return AgentResult(
        route="high_score",
        message=f"high score movie: {movie.title}, score: {movie.score}",
        prompt=ctx.get("prompt")
    )