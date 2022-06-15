# flask から Flask, render_templateモジュールをインポート
from flask import Flask, render_template

# Flaskインスタンスを生成
app = Flask(__name__)

# http://XXX/templateをルーティング
# 実行した場合に template関数が実行される
@app.route('/template') 
def template():
  title = 'AWS ML & Flask'
  message = 'AWS MLサービスをFlaskから利用'
  return render_template('template1.html', 
                  title = title, 
                  message = message)

if __name__ == '__main__':
  app.run(host='localhost', port=8888)