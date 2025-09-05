from .models import TopRoute, MovieRoute
from .llm_client import call_llm, parse_llm_json_str

TOP_ROUTER_SYSTEM = """
You are a strict binary router.

Goal: Decide if the user prompt is about MOVIES or NOT about movies.

Rules:
- If the prompt DOES NOT clearly mention movies/films, watching, theaters/cinema, streaming platforms (Netflix, Prime Video, Disney+, Max, etc.), recommendations of films, ratings/scores, or similar movie-related terms, choose "not_movies".
- Only choose "movies_router" if the intent is clearly about movies (recommendations, what's on Netflix, what's in theaters, best rated films, etc.).

- "not_movies": when the subject is NOT about movies
- "movies_router": when the subject IS about movies (any context)

Respond with VALID JSON ONLY:
{"route": "<not_movies|movies_router>"}
Do not add comments or explanations.
"""

MOVIE_ROUTER_SYSTEM = """
You are a movie router. 
If the user is asking for movie recommendations, choose EXACTLY ONE route:
- "theater": when the user wants movies currently in theater / "at the cinema"
- "streaming": when the user wants movies available on streaming platforms such as Netflix, Prime, Disney+, Max, etc.
- "high_score": when the user does not specify theater or streaming, and simply wants to watch a movie

Respond with VALID JSON ONLY, in the exact format:
{"route": "<theater|streaming|high_score>"}
Do not add comments or explanations.
"""

def route_top(prompt: str) -> TopRoute:
    try:
        txt = parse_llm_json_str(call_llm(TOP_ROUTER_SYSTEM, prompt))
        return TopRoute.model_validate_json(txt)
    except Exception:
        return TopRoute(route="not_movies")

def route_movies(prompt: str) -> MovieRoute:
    try:
        txt = parse_llm_json_str(call_llm(MOVIE_ROUTER_SYSTEM, prompt))
        return MovieRoute.model_validate_json(txt)
    except Exception:
        return MovieRoute(route="high_score")