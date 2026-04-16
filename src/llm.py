import requests
import json

def ask_llm(prompt):
    url = "http://localhost:11434/api/generate"

    data = {
        "model": "llama3:latest",   # you have this model
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, json=data)

    result = response.json()
    return result['response']

def extract_preference(memory):
    prompt = f"""
    Extract the main interest from this text.

    Text: {memory}

    Return ONLY one word from:
    shoes, tech, music, fitness, fashion, travel, gaming

    If unsure, return "general".
    """

    response = ask_llm(prompt).strip().lower()
    response = response.replace(".", "").replace("\n", "").strip()

    return response