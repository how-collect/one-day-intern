from openai import OpenAI
import openai
import os
import tiktoken
import json




# ファイルからテキストを読み込む
with open("C:/Users/taker/OneDrive/ドキュメント/デスクトップ/one-day-intern/rag/data/Norwegian-Wood.txt", "r", encoding="utf-8") as f:
    file_data = f.read()

client = OpenAI()

def split_text_by_tokens(text, max_tokens=1000):
    encoding = tiktoken.get_encoding("cl100k_base")
    token_ids = encoding.encode(text)
    chunks = []
    for i in range(0, len(token_ids), max_tokens):
        chunk_tokens = token_ids[i: i + max_tokens]
        chunk_text = encoding.decode(chunk_tokens)
        chunks.append(chunk_text)
    return chunks

chunks = split_text_by_tokens(file_data, max_tokens=1000)

embeddings = []
for chunk in chunks:
    response = client.embeddings.create(
        input= chunk,
        model="text-embedding-3-small"
    )
    embeddings.append(response.data[0].embedding)

jsonl_path = "C:/Users/taker/OneDrive/ドキュメント/デスクトップ/one-day-intern/rag/json/embedding.jsonl"
os.makedirs(os.path.dirname(jsonl_path), exist_ok=True)
with open(jsonl_path, "w", encoding="utf-8") as f:
    for text_chunk, vector in zip(chunks, embeddings):
        record = {"text": text_chunk, "vector": vector}
        json.dump(record, f, ensure_ascii=False)
        f.write("\n")

print(f" JSONLファイルを作成しました: {jsonl_path}")
print(f" 分割チャンク数: {len(chunks)}")

