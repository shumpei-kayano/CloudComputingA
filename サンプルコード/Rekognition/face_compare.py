# boto3 をインポート
import boto3
# json をインポート
import json
# sys をインポート
import sys
# pillow の Image モジュールをインポート
from PIL import Image

# コマンドラインの引数の個数が不適切ならば使い方を表示して終了
if len(sys.argv) != 3:
    print('python', sys.argv[0], 'source-image', 'target-image')
    exit()

# Rekognition サービスクライアントを作成
rekognition = boto3.client('rekognition')
# ソース画像を開く
with open(sys.argv[1], 'rb') as source:
    # ターゲット画像を開く
    with open(sys.argv[2], 'rb') as target:
        # ソース画像の顔をターゲット画像から探す
        result = rekognition.compare_faces(
            SourceImage={'Bytes': source.read()},
            TargetImage={'Bytes': target.read()})
        # 結果を整形して表示
        print(json.dumps(result, indent=4))

# 入力画像のファイルを読み込む
image_in = Image.open(sys.argv[2])
# 座像のサイズを取得
w, h = image_in.size
# 出力画像を作成
image_out = Image.new('RGB', (w, h), (200, 200, 200))
# 一致した顔を順番に処理
for face in result['FaceMatches']:
    # バウンディングボックスを取得
    box = face['Face']['BoundingBox']
    # 顔の左、上、右、下の座標を取得
    left = int(box['Left']*w)
    top = int(box['Top']*h)
    right = left+int(box['Width']*w)
    bottom = top+int(box['Height']*h)
    # 入力画像から出力画像に顔の部分を貼り付け
    image_out.paste(
        image_in.crop((left, top, right, bottom)),
        (left, top))
# 出力画像をファイルに保存
image_out.save('compare_'+sys.argv[2])
# 出力画像を表示
image_out.show()
