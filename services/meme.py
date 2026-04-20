import requests

def generate_meme(text, style):
    prompt = f"""
You are a viral meme creator.

Rules:
- Keep it short (max 10 words)
- Use Gen Z humor
- Make it relatable
- Add emojis if needed

Context: {text}
Style: {style}

Output only the caption.
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "phi3",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"].strip()
