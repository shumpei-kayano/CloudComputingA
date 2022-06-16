from flask import Flask, render_template, session, request, redirect, url_for
import os
# boto3 をインポート
import boto3
# json をインポート
import json
# sys をインポート
import sys
# pillow の Image モジュールとImageDrawモジュールをインポート
from PIL import Image, ImageDraw

# インスタンスの作成
app = Flask(__name__)

# メイン
@app.route('/', methods=['GET', 'POST'])
# アクセスした時に実行する関数を直下に記述する
def index():
    # methodが POST かを判断
    if request.method == 'POST':
        # ファイルのリクエストパラメータを取得
        f1 = request.files['image1']
        f2 = request.files['image2']
        # ファイル名を取得
        filename1 = f1.filename
        filename2 = f2.filename
        # ファイルを保存するディレクトリを指定
        filepath = 'static/image/' + filename2
        # try:
        # Rekognition サービスクライアントを作成
        rekognition = boto3.client('rekognition')
        # ソース画像を開く
        with open(filename1, 'rb') as source:
            # ターゲット画像を開く
            with open(filename2, 'rb') as target:
                # ソース画像の顔をターゲット画像から探す
                result = rekognition.compare_faces(
                    SourceImage={'Bytes': source.read()},
                    TargetImage={'Bytes': target.read()})

        # 入力画像のファイルを読み込む
        image_in = Image.open(filename2)
        # 座像のサイズを取得
        w, h = image_in.size
        # 描画用のオブジェクトを作成
        draw = ImageDraw.Draw(image_in)
        try:
            # 一致した顔を順番に処理
            for face in result['FaceMatches']:
                # バウンディングボックスを取得
                box = face['Face']['BoundingBox']
                # 顔の左、上、右、下の座標を取得
                left = int(box['Left']*w)
                top = int(box['Top']*h)
                right = left+int(box['Width']*w)    
                bottom = top+int(box['Height']*h)
                # 検知した顔を赤枠で囲む draw.rectangle((座標), fill=(塗りつぶしの色：任意), outline=(赤枠の色：任意),width=(太さ：任意))
                draw.rectangle((left, top, right, bottom), outline=(255, 0, 0),width=5)
            # 出力画像をファイルに保存
            image_in.save(filepath)
            flg = True
            text = '処理が完了しました。'
        except InvalidImageFormatException:
            text = '顔を認識できませんでした。'
            filepath = ''
            flg = True
    # GETのとき
    else:
        text = ''
        filepath = ''
        flg = False
    return render_template('index.html',
                    text = text,
                    image_url = filepath,
                    flg = flg)
# アプリケーションの起動 おまじない debug=Trueでエラーを表示してくれる
if __name__ == '__main__':
    app.run(debug=True)
