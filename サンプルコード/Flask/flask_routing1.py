# flask から Flaskモジュールをインポート
from flask import Flask

# Flaskインスタンスを生成
app = Flask(__name__)

# http://XXX/aws-translateをルーティング
# 実行した場合に translate関数が実行される
@app.route('/aws-translate') 
def translate():
  return '<h1>Amazon Translateの概要</h1>'

# http://XXX/aws-pollyをルーティング
# 実行した場合にこの関数が実行される
@app.route('/aws-polly') 
def polly():
    return '<h1>Amazon Pollyの概要</h1>'

# http://XXX/aws-rekognitionを実行した場合にこの関数が実行される
@app.route('/aws-rekognition') 
def rekognition():
    return '<h1>Amazon Rekognitionの概要</h1>'

if __name__ == '__main__':
  app.run(host='localhost', port=8888)