# flask から Flask, render_template, requestモジュールをインポート
from flask import Flask, render_template, request

# Flaskインスタンスを生成
app = Flask(__name__)

# http://XXX/form_checkをルーティング
# 実行した場合に form_check関数が実行される
@app.route('/form_check', methods=['GET', 'POST'])
def form_check():
  title = 'フォーム'
  # method が POST か否かを判断
  if request.method == 'POST':
    # POST のとき
    selected_list = request.form.getlist('checkbox')
    subject_name = ', '.join(selected_list)
  else:
    # GET のとき
    subject_name = ''
  form_type = 'チェックボックス'
  return render_template('form_check.html', 
                  title = title, 
                  subject_name = subject_name,
                  form_type = form_type)

if __name__ == '__main__':
  app.run(host='localhost', port=8888)