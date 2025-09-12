import openai


def main():
    client = openai.OpenAI(
        base_url="http://127.0.0.1:8080/v1",
        api_key="sk-no-key-required"
    )
    messages = [
        {"role": "system", "content": "You are a Linguistics Professor at Cornell named Marty."},
        {"role": "user", "content": "Tell me what you think about LLMs as models of human language processing"}
    ]

    output = client.chat.completions.create(
        model="GPT-6",
        messages=messages
    )
    output = output.choices[0].message
    
    print(f"Reasoning: {output.reasoning_content}\nContent: {output.content}")

if __name__ == "__main__":
    main()
