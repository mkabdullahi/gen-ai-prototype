import ollama

response = ollama.generate(
    model='llama3',
    prompt="Write a short bedtime story about a unicorn.",
    stream=False
)

print(response['response'])
