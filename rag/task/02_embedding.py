import json
import os
import numpy as np
from gensim.models import Word2Vec
from gensim.utils import simple_preprocess

# テキストファイルのパス（既に正しい絶対パスになっている）
file_path = "C:/Users/taker/OneDrive/ドキュメント/デスクトップ/one-day-intern/rag/data/Norwegian-Wood.txt"

# JSONLファイルの保存パス（相対パスに変更）
jsonl_path = "./json/embedding.jsonl"

# Word2Vec モデルの学習用パラメータ
# モデル保存パスも相対パスに変更（dataフォルダ内に保存）
W2V_MODEL_PATH = "./data/word2vec.model"
VECTOR_SIZE = 100  # 各単語の埋め込みベクトルの次元数
WINDOW = 5         # 周囲の単語を考慮する範囲
MIN_COUNT = 2      # 出現頻度がこの値未満の単語は無視
WORKERS = 4        # 並列処理用のスレッド数

# テキストを読み込む関数である
def load_text(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

# テキストを適当な長さで分割する関数である（例：500文字ごと）
def split_text(text, chunk_size=500):
    return [text[i : i + chunk_size] for i in range(0, len(text), chunk_size)]

# テキストを単語に分割（トークン化）する関数である
def tokenize_text(text):
    return simple_preprocess(text)  # 小文字化，不要文字除去，単語トークン化を行う

# Word2Vec モデルの学習（またはロード）する関数である
def train_or_load_w2v(chunks):
    tokenized_chunks = [tokenize_text(chunk) for chunk in chunks]

    # モデル保存用のディレクトリを作成する
    model_dir = os.path.dirname(W2V_MODEL_PATH)
    os.makedirs(model_dir, exist_ok=True)
    
    if os.path.exists(W2V_MODEL_PATH):
        model = Word2Vec.load(W2V_MODEL_PATH)
    else:
        model = Word2Vec(sentences=tokenized_chunks, vector_size=VECTOR_SIZE, window=WINDOW, min_count=MIN_COUNT, workers=WORKERS)
        model.save(W2V_MODEL_PATH)

    return model

# 各チャンクのベクトルを計算（単語ベクトルの平均）する関数である
def compute_chunk_vector(chunk, model):
    words = tokenize_text(chunk)
    word_vectors = [model.wv[word] for word in words if word in model.wv]
    
    if word_vectors:
        return np.mean(word_vectors, axis=0).tolist()  # 平均ベクトルをリストで返す
    else:
        return [0] * VECTOR_SIZE  # すべて未知語の場合はゼロベクトルを返す

# JSONL に保存する関数である
def save_to_jsonl(chunks, vectors, jsonl_path):
    # JSONL保存先ディレクトリを作成する
    os.makedirs(os.path.dirname(jsonl_path), exist_ok=True)
    with open(jsonl_path, "w", encoding="utf-8") as f:
        for text, vector in zip(chunks, vectors):
            json.dump({"text": text, "vector": vector}, f, ensure_ascii=False)
            f.write("\n")

# メイン処理である
text = load_text(file_path)                         # テキストを読み込む
chunks = split_text(text, chunk_size=500)            # 500文字ごとに分割する
w2v_model = train_or_load_w2v(chunks)                # Word2Vec モデルを学習またはロードする
vectors = [compute_chunk_vector(chunk, w2v_model) for chunk in chunks]  # 各チャンクをベクトル化する
save_to_jsonl(chunks, vectors, jsonl_path)           # JSONL に保存する

# 完了メッセージである
print(f"JSONLファイルを作成しました: {jsonl_path}")
print(f"分割数: {len(chunks)}")
