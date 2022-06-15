# flask から Flask, render_templateモジュールをインポート
from flask import Flask, render_template

# Flaskインスタンスを生成
app = Flask(__name__)

# http://XXX/templateをルーティング
# 実行した場合に template関数が実行される
@app.route('/template') 
def template():
  # テンプレートに渡す各種変数を初期化
  title = 'AWS ML & Flask'
  message = 'AWS MLサービスをFlaskから利用'
  # リスト
  ml_services = ['Translate', 'Polly', 'Textract', 'Rekognition']
  # テンプレートに各種変数を渡してレンダリング
  return render_template('template_if.html', 
              title=title, 
              message=message, 
              ml_service=ml_services[2])

if __name__ == '__main__':
  app.run(host='localhost', port=8888)