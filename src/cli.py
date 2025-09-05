import sys
from .agent import run_agent

def main():
    if len(sys.argv) > 1:
        prompt = " ".join(sys.argv[1:])
    else:
        # prompts default
        prompts = [
            "I like apples?",
            "Teach me SQL advanced queries",
            "What is the capital of France?",
            "Recommend me a great movie",
            "Recommend me a great movie currently in theaters",
            "What movies are available on Netflix?",
            "Show me a good film on Disney+ or Max"
        ]
        for p in prompts:
            print(f"\nPROMPT: {p}")
            print(run_agent(p).model_dump())
        return
    print(run_agent(prompt).model_dump())

if __name__ == "__main__":
    main()