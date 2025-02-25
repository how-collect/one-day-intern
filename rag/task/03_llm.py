from openai import OpenAI
import openai
import os



client = OpenAI()

prompt = input("ここに入力してください：")

completion = client.chat.completions.create(
    model="gpt-4",  
    messages=[
        {"role": "system", "content": "あなたは有能なアシスタントです。"},
        {"role": "user", "content": prompt}
    ],
)

# 生成された回答を出力
print(completion.choices[0].message.content)
