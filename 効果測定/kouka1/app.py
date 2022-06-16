from flask import Flask, render_template, session, request, redirect, url_for
import os
# boto3 をインポート
import boto3
# json をインポート
import json
# sys をインポート
import sys

# インスタンスの作成
app = Flask(__name__)

# メイン
@app.route('/', methods=['GET', 'POST'])
# アクセスした時に実行する関数を直下に記述する
def index():
    # methodが POST かを判断
    if request.method == 'POST':
        # Translate サービスクライアントを作成
        translate = boto3.client('translate')
        # 翻訳前テキストを取得
        preText = request.form.get('text')
        # 翻訳言語の取得
        SourceLanguage = request.form.get('language')
        # 翻訳
        result = translate.translate_text(
            Text= preText,
            SourceLanguageCode='auto', 
            TargetLanguageCode=SourceLanguage,
            TerminologyNames=['term_ja'])
        translatedText = result['TranslatedText']
        transText = translatedText
    # GETのとき
    else:
        transText = ''
    return render_template('index.html',
                transText = transText)
# アプリケーションの起動 おまじない debug=Trueでエラーを表示してくれる
if __name__ == '__main__':
    app.run(debug=True)
