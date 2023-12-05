import g4f

# g4f.debug.logging = False  # Enable logging
# g4f.check_version = False  # Disable automatic version checking
# print(g4f.version)  # Check version
# print(g4f.Provider.Ails.params)  # Supported args

from g4f.Provider import (
    AItianhu,
    Aichat,
    Bard,
    Bing,
    ChatBase,
    ChatgptAi,
    OpenaiChat,
    Vercel,
    You,
    Yqcloud,
    Raycast,
    Liaobots,
    GeekGpt,
    Phind
)

conversation_history = []

while True:
    user_input = str(input())
    messages = conversation_history + [{"role": "user", "content": user_input}]
    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        provider=g4f.Provider.You,
        messages=messages
    )

    for message in response:
        print(message, flush=True, end='')
    conversation_history = messages + [{"role": "assistant", "content": message} for message in response]
    print("\n")
