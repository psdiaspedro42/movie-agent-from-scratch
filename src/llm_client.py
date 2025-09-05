import os
from json_repair import repair_json
from openai import OpenAI

BASE_URL = os.getenv("OPENAI_BASE_URL", "http://127.0.0.1:1234/v1")
API_KEY  = os.getenv("OPENAI_API_KEY", "lm-studio")
MODEL    = os.getenv("OPENAI_MODEL", "lmstudio-community/gemma-2-2b-it-GGUF")

CLIENT = OpenAI(base_url=BASE_URL, api_key=API_KEY)

def call_llm(system: str, prompt: str) -> str:
    res = CLIENT.chat.completions.create(
        model=MODEL,
        temperature=0,
        messages=[{"role": "system", "content": system},
                  {"role": "user", "content": prompt}]
    )
    return res.choices[0].message.content.strip()

def parse_llm_json_str(raw: str) -> str:
    return repair_json(raw).strip()