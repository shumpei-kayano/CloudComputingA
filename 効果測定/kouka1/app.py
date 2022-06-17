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

# アクセスした時に実行する関数を直下に記述する
# -----------translate(翻訳)--------------
@app.route('/', methods=['GET', 'POST'])
def index():
    # methodが POST かを判断
    if request.method == 'POST':
        # Translate サービスクライアントを作成
        translate = boto3.client('translate')
        # 翻訳前テキストを取得
        getText = request.form.get('pretext')
        preText = getText
        # 翻訳言語の取得
        language = request.form.get('language')
        SourceLanguage = language
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
        preText = ''
    return render_template('index.html',
                transText = transText,
                preText = preText)

# -----------conprehend(感情分析)--------------
@app.route('/comprehend', methods=['POST'])
def comprehend():
        # Comprehend サービスクライアントを作成
        comprehend = boto3.client('comprehend', 'us-east-1')
        # 感情分析するテキストを取得
        getText = request.form.get('pretext')
        text = getText
        # 感情分析するテキストの言語を取得
        result = comprehend.detect_dominant_language(Text=text)
        language = result['Languages'][0]['LanguageCode'] #Languagesには複数の言語コードがあり得る
        # 感情を分析
        result = comprehend.detect_sentiment(Text=text, LanguageCode=language)
        # 結果を表示
        sentiment = result['Sentiment']  #推測した感情
        positive = result['SentimentScore']['Positive'] #肯定的な感情のスコア
        negative = result['SentimentScore']['Negative'] #否定的な感情のスコア
        neutral = result['SentimentScore']['Neutral'] #中立的な感情のスコア
        mixed = result['SentimentScore']['Mixed'] #混じった感情のスコア
        return render_template('comprehend.html',
                        sentiment = sentiment,
                        language = language,
                        positive = round((positive * 100),2),
                        negative = round((negative * 100),2),
                        neutral = round((neutral * 100),2),
                        mixed = round((mixed * 100),2))
# アプリケーションの起動 おまじない debug=Trueでエラーを表示してくれる
if __name__ == '__main__':
    app.run(debug=True)
