from flask import Flask, request

app = Flask(__name__)


# サーバールートへアクセスがあった時 --- (*1)
@app.route("/")
def index():
    main_html = """
        <html><body>
        <form action="/hello" method="GET">
            <p>名前: <input type="text" name="name"></p>
            <p>一言: <input type="text" name="word"></p>
            <input type="submit" value="送信">
        </form>
        </body></html>
    """
    # フォームを表示する --- (*2)
    return main_html


# /hello へアクセスがあった時 --- (*3)
@app.route("/hello")
def hello():
    # nameのパラメータを得る --- (*4)
    name = request.args.get("name")
    word = request.args.get("word")
    if name is None:
        name = "Guest User"
    if word is None:
        word = "null"

    # 自己紹介を自動作成
    return """
        <h1>Welcome, {0}.</h1>
        <p>{1}</p>
    """.format(name, word)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
