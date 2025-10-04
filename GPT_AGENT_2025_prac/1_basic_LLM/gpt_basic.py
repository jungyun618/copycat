from openai import OpenAI

api_key = ''

client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model = "gpt-4o-mini",
    temperature=0.1,
    messages=[
        {"role": "system", "content": "You are a helpful assistant AI."},
        {"role": "user", "content": "2000년 이후의 월드컵 우승팀들을 모두 알려줘."},
    ]
)

print(response)
print('----')
print(response.choices[0].message.content)