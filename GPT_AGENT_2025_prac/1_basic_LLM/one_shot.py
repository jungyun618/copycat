from openai import OpenAI

api_key = ''

client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model = "gpt-4o-mini",
    temperature=0.1,
    messages=[
        {"role": "system", "content": "말 끝에 '아마도~?'를 붙여서 답변하라."},
        {"role": "user", "content": "레알 마드리드의 가장 대표적인 라이벌 클럽은 어디야?"},
        {"role": "assistant", "content":"바르셀로나겠지요. 아마도~?"},
        {"role": "user", "content": "맨체스터 유나이티드에서 13번의 리그우승을 차지한 감독은 누구야?"},
    ]
)

print(response)
print('----')
print(response.choices[0].message.content)