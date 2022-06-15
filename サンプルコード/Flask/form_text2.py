# flask から Flask, render_template, requestモジュールをインポート
from flask import Flask, render_template, request

# Flaskインスタンスを生成
app = Flask(__name__)

# http://XXX/form_textをルーティング
# 実行した場合に form_text関数が実行される
@app.route('/form_text', methods=['GET', 'POST'])
def form_text_post():
  title = 'フォーム(text)'
  if request.method == 'POST':
    file_name = request.form.get('name')
  else:
    file_name = ''
  form_type = 'インプット　テキスト'
  return render_template('form_text.html', 
                  title = title, 
                  file_name = file_name,
                  form_type = form_type)

if __name__ == '__main__':
  app.run(host='localhost', port=8888)