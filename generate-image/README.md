## お願い
`feature/{your-name}` というブランチを作成し、そこでタスクを行い、最終的にキリが良いところでプッシュしてください。  

> [!IMPORTANT]
> わからないことがあれば、どんな基礎的なことでも気軽に聞いてください！

## タスク１：環境構築の理解度チェック
pyenv を使い、python のバージョンを指定できるようにしてください。  
venv を使い、プロジェクトごとにパッケージを使い分けられるようにしてください。  
linter として flake8 をインストールしてください。

> [!NOTE]
> 既に pyenv を使ったバージョン管理、 venv を使ったパッケージ管理ができる状態であれば、このタスクは飛ばしてください

## タスク２：python の理解度チェック
数字を入力し、素数であれば True 、素数でなければ False を表示するようなコードを作成してください。

例）  
```
input : 31  
output: True
```

条件）  
* コードは [ここ](./tasks/python.py) に記載してください
* 1e5 よりも大きい数では error を返してください
* 素数の判定は関数で行ってください
* 関数の説明には numpy 形式の docstring を使用してください

## タスク３：api の理解度チェック
郵便番号を入力すると、それに対応した 都道府県、市区町村 が出てくるようなコードを作成してください。

例）
```
input : 162-0801  
output: 東京都 新宿区
```

条件）
* コードは [ここ](./tasks/api.py) に記載してください
* api は zipcloud api を用いてください
* 関数の説明には numpy 形式の docstring を使用してください

## タスク４：flask を使った api 開発
flask というフレームワークを用いて、「タスク２、タスク３」で作成した関数を RPC api にしてください。

仕様）
```shell
# 素数判定API
request-url: {local-host}/judge-primary-number
request-method: POST
content-type: application/json
request-body: {"number": 24}
response: {"is-prime": false}

# 郵便番号から住所を取得するAPI
request-url: {local-host}/get-province-and-city
request-method: POST
content-type: application/json
request-body: {"postal-code": "162-0801"}
response: {"province": "東京都", "city": "新宿区"}
```

条件）
* [このフォルダ](./tasks/flask) を自由に利用して api を作成してください
* 関数の説明には numpy 形式の docstring を使用してください

<!-- 
## タスク４：comfy ui を使ってみる
用意した[スライド](https://docs.google.com/presentation/d/1ZHw_5ZWXcORP126wJmbFmvjfG9h9KZZW/edit?usp=drive_link&ouid=102839788932558976251&rtpof=true&sd=true)に沿って進める。

以下のリンクの資料を使ってください。

[controlnet_lora.json](https://drive.google.com/file/d/18loAoeaqxf8KyMyJBwVaq1kyO3erNPV7/view?usp=drive_link)

[input2.png](https://drive.google.com/file/d/13DcLpFtfAD8141GQ-eW2cFolm4VQFR3g/view?usp=drive_link)

[こちら](https://github.com/comfyanonymous/ComfyUI)を参考に、colab 上で comfy ui を起動し、何らかの画像を生成してみてください。 -->
