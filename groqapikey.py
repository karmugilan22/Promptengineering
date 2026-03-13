import os
from groq import Groq
GROQ_KEY = os.getenv('GROQ_API_KEY')
if not GROQ_KEY:
    raise ValueError("GROQ_API_KEY environment variable is not set")
client = Groq(api_key=GROQ_KEY)
roles={
    "teacher": "You are a helpful assistant that provides detailed explanations to students' questions.",
    "doctor": "You are a knowledgeable medical assistant that provides accurate and concise medical information to patients.",
    "programmer": "You are an experienced software developer who provides clear and efficient coding solutions to programming problems.",
    "motivator": "You are an inspiring coach who provides motivational advice and encouragement to help individuals achieve their goals.",
    "fashion_expert": "You are a stylish fashion consultant who offers trendy and personalized fashion advice to clients.",
    "farmer": "You are a skilled agricultural expert who provides practical farming advice and solutions to farmers."
}
print("Available roles:")
for role in roles:
    print("-",role)

selected_role = input("Please select a role from the above options: ").lower()
if selected_role not in roles:
    print("Invalid role selected. Please choose a valid role.")
    selected_role="teacher"

system_prompt = roles[selected_role]
messages=[
    {"role": "system", "content": system_prompt}
]

print(f"\n Multi-Role Assistant - {selected_role.capitalize()} Mode")
print("Type 'exit' to quit the assistant.\n")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Exiting the assistant. Goodbye!")
        break
    messages.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages,
        temperature=0.7,
        max_tokens=150
    )
    assistant_reply = response.choices[0].message.content
    print(f"Assistant: {assistant_reply}\n")
    messages.append({"role": "assistant", "content": assistant_reply})