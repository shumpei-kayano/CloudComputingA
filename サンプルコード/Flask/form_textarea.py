# flask から Flask, render_template, requestモジュールをインポート
from flask import Flask, render_template, request

# Flaskインスタンスを生成
app = Flask(__name__)

# http://XXX/form_textareaをルーティング
# 実行した場合に form_text_area関数が実行される
@app.route('/form_textarea', methods=['GET', 'POST'])
def form_text_area():
  title = 'フォーム（textarea）'
  # method が POST か否かを判断
  if request.method == 'POST':
    # POST のとき
    texts = request.form.get('texts')
  else:
    # GET のとき
    texts = ''
  form_type = 'テキストエリア'
  return render_template('form_textarea.html', 
                  title = title, 
                  texts = texts,
                  form_type = form_type)

if __name__ == '__main__':
  app.run(host='localhost', port=8888)