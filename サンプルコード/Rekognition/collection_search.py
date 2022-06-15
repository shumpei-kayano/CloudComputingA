import boto3
import json
import sys
from PIL import Image

# コマンドライン引数が不適切ならば使い方を表示して終了
if len(sys.argv) != 2:
    print('python', sys.argv[0], 'image')
    exit()

# Rekognition サービスクライアントを作成
rekognition = boto3.client('rekognition')
# コレクションID
collection_id = 'MyCollection_takeda'
# 画像ファイルを開く
with open(sys.argv[1], 'rb') as file:
    # 画像内の顔をコレクションから探す
    result = rekognition.search_faces_by_image(
        CollectionId=collection_id,     # コレクションID
        Image={'Bytes': file.read()})   # 検索したい顔が含まれる画像
    # 検索結果を表示
    print(json.dumps(result, indent=4))
# 入力画像のファイルを読み込む
image_in = Image.open(sys.argv[1])
# 画像のサイズを取得
w, h = image_in.size
# 出力画像を作成
image_out = Image.new('RGB', (w, h), (200, 200, 200))
# 画像の顔がコレクションに登録されているか否かを判断
if result['FaceMatches']:
    # 顔がコレクションに登録されている場合
    # バウンディングボックスを取得
    box = result['SearchedFaceBoundingBox']
    # 顔の左座標を計算
    left = int(box['Left']*w)
    # 顔の上座標を取得
    top = int(box['Top']*h)
    # 顔の右座標を取得
    right = left+int(box['Width']*w)
    # 顔の下座標を取得
    bottom = top+int(box['Height']*h)
    # 入力画像から出力画像の顔の部分を貼り付け
    image_out.paste(
        image_in.crop((left, top, right, bottom)),
        (left, top))
# 出力画像をファイルに保存
image_out.save('search_'+sys.argv[1])
# 出力画像を表示
image_out.show()