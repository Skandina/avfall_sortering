import openai
from PyKakao import Karlo

OPENAI_API_KEY = "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"
openai.api_key = OPENAI_API_KEY

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

#KAKAO_API_KEY = "d071bf06aa30e53cf2bb882489026b09"
#karlo = Karlo(service_key = KAKAO_API_KEY)

#def image_answer(describe):
#    text = ("Example of" + describe + " for recycling")
#    img_dict = karlo.text_to_image(text, 1)
#    img_str = img_dict.get("images")[0].get('image')
#    img = karlo.string_to_image(base64_string = img_str, mode = 'RGBA')
#    img.save("./static/img/temp.png")
#    return print("The img by karlo has been saved")
