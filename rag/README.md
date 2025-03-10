# ワンデイインターン生 タスク

## タスク前の事前知識

### token
当然ですが、文章をそのままコンピュータに理解させることはできません。  
そこで ChatGPT 等の大規模言語モデル（LLM）では、自然言語処理として文章を一度「token」と呼ばれる数字に変換してから諸々の計算を行なっています。  
そして、ほとんどの LLM は token の数によって使用料金を決定しているので token を数えることは業務上重要な役割を果たします。

### embedding
テキストを正規化されたベクトルに変換することで、文章がどのくらい似ているか（類似度）を計算できるようになります。  
その「ベクトルへの変換（埋め込み）」を「embedding」といい、多くの会社がその仕組みを提供しています。

## お願い

### github
```
feature/{your-name}
```
という branch を作成し、そこでタスクを行ってください。  
最終的にキリが良いところで remote に push してください。  


## タスク

### タスク01: Token count
何かしら方法で以下のテキストをトークン化し、トークンの数を数えてください。


```txt
アインシュタインの「相対性理論」は、だれでもその名前ぐらいは聞いたことがあるだろう。そして、いろいろな「早分かり本」で、その理論のもたらす奇妙な諸帰結についても
読んだことがあるだろう。曰く、光速に近い速さで飛んでいるロケットと地上では時間の進み方が違う、とか、空間は曲がっている、とか、原子爆弾の理論的根拠となったＥ＝ｍｃ2 という方程式は相対性理論から帰結する・・・とか、である。

こんな不思議な相対性理論だから、そのエッセンスだけでも知っておきたいと思う人もおおいだろう。この私もその一人である。しかし、現代物理学の最高峰の一つがそんなかんたんにわかるはずがない、と尻込みしていまうひとが多いだろう（この私もそうでした）。
しかし、最近すこし勉強してみると、特殊相対性理論に関しては意外に簡単に理解することができることがわかった。
ここで、その成果を二頁で(!!) 述べてみよう。「教えることほど、よい勉強法はない」。
いわば「知ったかぶりの相対性理論講義」である。
```

コードは `/task/01_token_count.py` に記載してください。
___


### タスク02: Embedding
`/data/Norwegian-Wood.txt` このテキストを好きなように分割し、分割したテキストをそれぞれベクトル化してください。  

分割したテキストと、そのベクトル、どちらの情報も保持したjsonlファイルを `/json/embedding.jsonl` に作成してください。jsonlのデータ構造は以下のようにしてください。
```
{"text": "separated text 1", "vector": [1.00, 1.00, ...]}
{"text": "separated text 2", "vector": [1.00, 1.00, ...]}
{"text": "separated text 3", "vector": [1.00, 1.00, ...]}
...
```
コードは全て `02_embedding.py` に記載してください。
___


### タスク03: LLM API
何かしらの方法でLLMをプログラム上で使えるようにしてください。

コードは全て `03_llm.py` に記載してください。
___


### タスク04: RAG
今まで作ったコードをもとに好きな方法で RAG 開発を行ってください。  
* 詳細  
1. LLM への質問を入力すると、それがベクトル化される。
2. その質問と似た文章（最も類似度が大きいもの）を jsonl から探してください。
3. 以下の質問を user prompt 、似ていた文章を system prompt として LLM に送信してください。

```txt
同居人がラジオ体操を始めたのは何時でしたか。
```
（正しい回答: 6時半）
コードは全て `4_rag.py` に記載してください。
