from typing import Dict, Any
from .models import AgentResult
from .routers import route_top, route_movies
from .graph import build_graph

def run_agent(prompt: str) -> AgentResult:
    G = build_graph()
    ctx: Dict[str, Any] = {"prompt": prompt}
    top = route_top(prompt).route
    if top == "not_movies":
        fn = G.nodes["not_movies"]["fn"]
        return fn(ctx)

    sub = route_movies(prompt).route
    if sub not in {"theater", "streaming", "high_score"}:
        return AgentResult(route=sub, erro="Invalid movie route")
    fn = G.nodes[sub]["fn"]
    return fn(ctx)