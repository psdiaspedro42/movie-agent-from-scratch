import networkx as nx
from .executors import not_movies, theater_movies, streaming_movies, high_score_movies

def build_graph() -> nx.DiGraph:
    G = nx.DiGraph()
    G.add_node("root_router")
    G.add_node("movies_router")
    G.add_node("not_movies", fn=not_movies)
    G.add_node("theater",    fn=theater_movies)
    G.add_node("streaming",  fn=streaming_movies)
    G.add_node("high_score", fn=high_score_movies)

    G.add_edge("root_router", "not_movies",    cond="not_movies")
    G.add_edge("root_router", "movies_router", cond="movies")
    G.add_edge("movies_router", "theater",     cond="theater")
    G.add_edge("movies_router", "streaming",   cond="streaming")
    G.add_edge("movies_router", "high_score",  cond="high_score")
    return G