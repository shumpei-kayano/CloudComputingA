from flask import Flask, render_template, session, request, redirect, url_for
import os

# インスタンスの作成
app = Flask(__name__)

# urandom関数で指定した桁数のランダムな値が生成される
key = os.urandom(21)
# app.secret_kayにランダム値をセット
app.secret_key = key

# IDとパスワードの登録
id_pwd = {
    'kayano':'1234'
}

# メイン
@app.route('/')
# アクセスした時に実行する関数を直下に記述する
def index():
    if not session.get('login'):
        # url_for関数の引数は関数を指定するつまりlogin関数が呼ばれている
        return redirect(url_for('login'))
    else:
        return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

# ログイン認証
@app.route('/logincheck', methods=['POST'])
def logincheck():
    user_id = request.form['user_id']
    password = request.form['password']
    
    if user_id in id_pwd:
        if password == id_pwd[user_id]:
            session['login'] = True
        else:
            session['login'] = False
    else:
        session['login'] = False

    if session['login']:
        return redirect(url_for('index'))
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('login', None)
    return redirect(url_for('index'))

# アプリケーションの起動 おまじない debug=Trueでエラーを表示してくれる
if __name__ == '__main__':
    app.run(debug=True)
