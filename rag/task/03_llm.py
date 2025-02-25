from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# 使用するモデル名を指定する．
model_name = "gpt2"  # GPT‐2 モデルを使用する．

# トークナイザーをロードする．
tokenizer = AutoTokenizer.from_pretrained(model_name)

# モデルをロードする．
model = AutoModelForCausalLM.from_pretrained(model_name)

# プロンプトを定義する．
prompt = "相対性理論とは"

# プロンプトをトークン化する．
inputs = tokenizer(prompt, return_tensors="pt")

# テキストを生成する．
outputs = model.generate(**inputs, max_length=100, do_sample=True, temperature=0.7)

# 生成されたトークンをテキストに変換する．
generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

# 結果を出力する．
print("生成されたテキスト：")
print(generated_text)
