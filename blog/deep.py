from openai import OpenAI

client = OpenAI(api_key="sk-00c943fc9fef4f1ba710bbe37802cbb8", base_url="https://api.deepseek.com/v1")

def trnslate(text):
    prompt = f"Переведи приведенный текст: {text} на русский язык, сохраняя структуру, стиль и смысл текста."
    response = client.chat.completions.create(
        model="gpt-5.4",
        messages=[{"role": "user", "content": prompt}],
        temperature="0.5",
        max_tokens=400
    )

    return response.choices[0].message.content