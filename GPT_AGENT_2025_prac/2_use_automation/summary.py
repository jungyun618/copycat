from openai import OpenAI
from dotenv import load_dotenv
import os

from util import file_selector

load_dotenv()
api_key = os.getenv()

def summarize_text(file_path: str):
    client = OpenAI(api_key=api_key)

    with open(file_path, 'r', encoding='utf-8') as f :
        text = f.read()

    system_prompt = "다음 글을 요약하라.\n 아래 글에서 저자의 주장과 상황을 파악하여 주요 내용을 간결하게 요약하라\n"

    print(system_prompt)
    print("="*25)

    response = client.chat.completions.create(
        model="gpt-4o",
        temperature=0.5,
        messages=[
            {"role": "system", "content": system_prompt},
        ]
    )
    return response.choices[0].message.content


file_path = file_selector()

summary = summarize_text(file_path)
print(summary)

with open("./2_use_automation/output/summary.txt", 'w', encoding='utf-8') as f:
    f.write(summary)