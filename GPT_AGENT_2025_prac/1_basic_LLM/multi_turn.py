from openai import OpenAI

api_key = ''

client = OpenAI(api_key=api_key)

def get_response(messages):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0.1,
        messages=messages
    )
    return response.choices[0].message.content

def exit_condition(input):
    exit_list = ['exit', 'EXIT', '종료', '끝', 'quit', 'Quit']
    if input in exit_list:
        return True
    return False

messages = [
    {"role": "system", "content": "너는 보조 ai AGENT 이다."},
]

while True:
    user_input = input("USER: ")

    if exit_condition(user_input)==True:
        break

    messages.append({"role": "user", "content": user_input})
    ai_response = get_response(messages)
    messages.append({"role": "assistant", "content": ai_response})
    print("AI: "+ ai_response)