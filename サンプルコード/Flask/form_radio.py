# flask から Flask, render_template, requestモジュールをインポート
from flask import Flask, render_template, request

# Flaskインスタンスを生成
app = Flask(__name__)

# http://XXX/form_radioをルーティング
# 実行した場合に form_radio関数が実行される
@app.route('/form_radio', methods=['GET', 'POST'])
def form_radio():
  title = 'フォーム'
  # method が POST か否かを判断
  if request.method == 'POST':
    # POST のとき
    cource_name = request.form.get('radio')
  else:
    # GET のとき
    cource_name = ''
  form_type = 'ラジオボタン'
  return render_template('form_radio.html', 
                  title = title, 
                  cource_name = cource_name,
                  form_type = form_type)

if __name__ == '__main__':
  app.run(host='localhost', port=8888)