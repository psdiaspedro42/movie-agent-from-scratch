from typing import List
from .models import Movie

MOVIES_DB: List[Movie] = [
    Movie(title="Dune: Part Two",       theater=True,  score=8.4),
    Movie(title="The Perfect Assassin", theater=True,  score=7.2),
    Movie(title="La La Land",           theater=False, score=8.0, streamings=["Prime Video"]),
    Movie(title="Drive",                theater=False, score=7.8, streamings=["Netflix"]),
    Movie(title="Whiplash",             theater=False, score=8.5, streamings=["Max"]),
    Movie(title="Oppenheimer",          theater=True,  score=8.6),
    Movie(title="Barbie",               theater=True,  score=7.1),
    Movie(title="Inception",            theater=False, score=8.8, streamings=["Netflix", "Max"]),
    Movie(title="The Social Network",   theater=False, score=7.7, streamings=["Prime Video"]),
    Movie(title="Interstellar",         theater=False, score=8.6, streamings=["Paramount+", "Netflix"]),
    Movie(title="The Dark Knight",      theater=False, score=9.0, streamings=["Max"]),
    Movie(title="Inside Out 2",         theater=True,  score=8.2),
    Movie(title="Avengers: Endgame",    theater=False, score=8.4, streamings=["Disney+"]),
    Movie(title="Parasite",             theater=False, score=8.6, streamings=["Prime Video", "Max"]),
]