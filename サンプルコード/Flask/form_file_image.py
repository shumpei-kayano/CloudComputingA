# flask から Flask, render_template, requestモジュールをインポート
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

# Flaskインスタンスを生成
app = Flask(__name__)

# http://XXX/form_file_imageをルーティング
# 実行した場合に form_file_image関数が実行される
@app.route('/form_file_image', methods=['GET', 'POST'])
def form_file_image():
  title = 'フォーム'
  # method が POST か否かを判断
  if request.method == 'POST':
    # POST のとき
    # ファイルのリクエストパラメータを取得
	  f = request.files.get('image')
	  # ファイル名を取得
	  filename = secure_filename(f.filename)
	  # ファイルを保存するディレクトリを指定
	  filepath = 'static/image/' + filename
	  # ファイルを保存する
	  f.save(filepath)
  else:
    # GET のとき
    filename = ''
    filepath = ''
  form_type = 'ファイル選択'
  return render_template('form_file_image.html', 
                  title = title, 
                  filename = filename,
                  form_type = form_type,
                  image_name = filename,
                  image_url = filepath)

if __name__ == '__main__':
  app.run(host='localhost', port=8888)