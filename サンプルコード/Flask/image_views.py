# flask から Flask, render_templateモジュールをインポート
from flask import Flask, render_template

# Flaskインスタンスを生成
app = Flask(__name__)

# http://XXX/をルーティング
# 実行した場合に index関数が実行される
@app.route('/image_view')
def image_view():
  return render_template('image_view.html')

# http://XXX/url_forをルーティング
# 実行した場合に url_for関数が実行される
@app.route('/image_link')
def image_link():
  return render_template('image_link.html')

if __name__ == '__main__':
  app.run(host='localhost', port=8888)