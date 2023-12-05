import g4f

print("Now Starting...")
print("which model do you want? \n1) gpt-3.5 \n2) gpt-4")
modsel = int(input())
if modsel == 1:
    model="gpt-3.5-turbo"
    provider=g4f.Provider.GeekGpt
else :
    model="gpt-4"   
    provider=g4f.Provider.Bing
print("initialize complete!")
conversation_history = []

while True:
    user_input = str(input())
    if user_input == "":
        break
    messages = conversation_history + [{"role": "user", "content": user_input}]
    response = g4f.ChatCompletion.create(
        model=model,
        provider=provider,
        messages=messages
    )

    for message in response:
        print(message, flush=True, end='')
    conversation_history = messages + [{"role": "assistant", "content": message} for message in response]
    print("\n")
