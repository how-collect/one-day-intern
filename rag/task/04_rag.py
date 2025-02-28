from openai import OpenAI
import openai
import os
import tiktoken
import numpy


text = input("ここに質問してください:")

response = openai.embeddings.create(
    input=text,
    model="text-embedding-ada-002"
)

embedding_vector = response.data[0].embedding

vector1 = numpy.array(embedding_vector)

# ファイルからテキストを読み込む
for i in :
with open("C:/Users/taker/OneDrive/ドキュメント/デスクトップ/one-day-intern/json/embedding.jsonl", "r", encoding="utf-8") as f:
    file_data = f.read()



    vector2 = numpy.array()

    dot_product = np.dot(vector1, vector2)
    print("内積:", dot_product)  
