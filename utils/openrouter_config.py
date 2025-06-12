# openrouter_config.py
# Setup LLM gratis via OpenRouter API

import os
from langchain.llms import OpenAI

# Pastikan kamu sudah dapat API Key gratis dari https://openrouter.ai

def load_openrouter_llm():
    api_key = os.getenv("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")
    if not api_key:
        raise ValueError("❌ OPENROUTER_API_KEY belum di-set di environment variables.")

    return OpenAI(
        temperature=0,
        model_name="mistralai/mixtral-8x7b-instruct",  # Bisa diganti dengan claude-3-haiku, dll
        openai_api_base="https://openrouter.ai/api/v1",
        openai_api_key=api_key
    )
