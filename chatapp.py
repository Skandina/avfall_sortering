import openai
import keys

openai.api_key = keys.OPENAI_API_KEY

def chat_answer(waste):
    model = "gpt-3.5-turbo"
    query =  "How can I sort" + waste

    messages = [
            {"role": "system", "content": "You are a helpful assistant for seperating garbage in Sweden. but you don't have to mention especially It's in Sweden"},
            {"role": "user", "content": query}
    ]

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages
    )

    answer = response['choices'][0]['message']['content']
    return answer

