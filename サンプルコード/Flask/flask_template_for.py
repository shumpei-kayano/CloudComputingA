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
  # 辞書
  ml_service_dict = {'Translate' : 120,
                     'Polly' : 160,
                     'Textract' : 200,
                     'Rekognition' : 220}
  # テンプレートに各種変数を渡してレンダリング
  return render_template('template_for.html', 
              title=title, message=message, 
              ml_services=ml_services,
              ml_service_dict=ml_service_dict)

if __name__ == '__main__':
  app.run(host='localhost', port=8888)