import os
import json
from openai import OpenAI
from dotenv import load_dotenv
from .base import BaseProvider

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
if not HF_TOKEN:
    raise RuntimeError("HF_TOKEN não encontrado. Coloque no arquivo .env: HF_TOKEN=...")

MODEL = os.getenv("HF_MODEL", "meta-llama/Llama-3.1-8B-Instruct:novita")
DEBUG = os.getenv("DEBUG", "0") == "1"
BASE_URL = os.getenv("HF_BASE_URL", "https://router.huggingface.co/v1")

client = OpenAI(base_url=BASE_URL, api_key=HF_TOKEN)

def debug_print(*args):
    if DEBUG:
        print(*args)

class Llama8BProvider(BaseProvider):
    def chat(self, system_prompt: str, user_prompt: str, max_tokens: int = 220) -> str:
        completion = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.0,
            max_tokens=max_tokens,
        )

        if DEBUG:
            dump = completion.model_dump()
            debug_print("\n=== FULL DUMP ===")
            debug_print(json.dumps(dump, ensure_ascii=False, indent=2))
            debug_print("=== END FULL DUMP ===\n")

        return (completion.choices[0].message.content or "").strip()