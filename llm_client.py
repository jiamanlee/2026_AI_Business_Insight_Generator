import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("LLM_API_KEY", "")
BASE_URL = os.getenv("LLM_BASE_URL", "https://api.openai.com/v1").rstrip("/")
MODEL = os.getenv("LLM_MODEL", "gpt-4o-mini")

def call_llm(prompt):
    if not API_KEY:
        return "ERROR: Missing LLM_API_KEY. Please set it in your .env file."

    url = f"{BASE_URL}/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "You are a business insights expert."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.2
    }

    response = requests.post(url, headers=headers, json=data, timeout=60)

    # 如果不是200，直接把错误返回到页面（最关键）
    if response.status_code != 200:
        return f"API ERROR (status={response.status_code}):\n{response.text}"

    result = response.json()

    # 如果返回里没有 choices，就把整个返回打印出来（最关键）
    if "choices" not in result:
        return f"API ERROR (unexpected response):\n{result}"

    return result["choices"][0]["message"]["content"]
