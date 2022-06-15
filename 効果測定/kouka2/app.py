from flask import Flask, render_template, session, request, redirect, url_for
import os

# インスタンスの作成
app = Flask(__name__)

# メイン
@app.route('/')
# アクセスした時に実行する関数を直下に記述する
def index():
    return render_template('index.html')

@app.route('/awsRekog', methods=['POST'])
def awsRekog():
    return render_template('result.html')

# アプリケーションの起動 おまじない debug=Trueでエラーを表示してくれる
if __name__ == '__main__':
    app.run(debug=True)
