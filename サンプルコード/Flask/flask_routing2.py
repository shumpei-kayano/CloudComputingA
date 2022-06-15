# flask から Flaskモジュールをインポート
from flask import Flask

# Flaskインスタンスを生成
app = Flask(__name__)

# http://XXX/aws-translateをルーティング
# 実行した場合に translate関数が実行される
@app.route('/aws-translate') 
def translate():
  return '<a href="https://aws.amazon.com/jp/translate/">Amazon Translateの紹介</a>'

# http://XXX/aws-pollyをルーティング
# 実行した場合にこの関数が実行される
@app.route('/aws-polly') 
def polly():
    return '<a href="https://aws.amazon.com/jp/polly/">Amazon Pollyの紹介</a>'

# http://XXX/aws-rekognitionを実行した場合にこの関数が実行される
@app.route('/aws-rekognition') 
def func3():
    return '<a href="https://aws.amazon.com/jp/rekognition/">Amazon Rekognitionの紹介</a>'

if __name__ == '__main__':
  app.run(host='localhost', port=8888)