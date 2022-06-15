# boto3 をインポート
import boto3
# json をインポート
import json
# sys をインポート
import sys
# pillow の Image モジュールと ImageDraw モジュールをインポート
from PIL import Image, ImageDraw

# 任意の太さで矩形を描画する関数
def thick_rectangle(draw:ImageDraw, xy, outLine, width):
    x1, y1, x2, y2 = xy
    draw.line((x1,y1,x2,y1), outLine, width)
    draw.line((x2,y1,x2,y2), outLine, width)
    draw.line((x2,y2,x1,y2), outLine, width)
    draw.line((x1,y2,x1,y1), outLine, width)

# コマンドラインの引数の個数が不適切ならば使い方を表示して終了
if len(sys.argv) != 3:
    print('python', sys.argv[0], 'source-image', 'target-image')
    exit()

try:
    # Rekognition サービスクライアントを作成
    rekognition = boto3.client('rekognition')
# エラーが発生した場合
except Exception as e:
    print("AWSに接続できませんでした.")
    print(e)
    print("プログラムを終了します.")
    exit()

try:
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
# 画像が開けなかった場合
except Exception as e:
    print("画像が開けませんでした.")
    print(e)
    print("プログラムを終了します.")
    exit()

# 入力画像のファイルを読み込む
image_in = Image.open(sys.argv[2])
# 座像のサイズを取得
w, h = image_in.size
# 一致した顔を順番に処理
for face in result['FaceMatches']:
    # バウンディングボックスを取得
    box = face['Face']['BoundingBox']
    # 顔の左、上、右、下の座標を取得
    left = int(box['Left']*w)
    top = int(box['Top']*h)
    right = left+int(box['Width']*w)
    bottom = top+int(box['Height']*h)
    # 図形を表示するためのオブジェクトを生成
    draw = ImageDraw.Draw(image_in)
    # 一致した顔に赤の枠線を重ねて表示
    thick_rectangle(
        draw=draw,
        xy=(left, top, right, bottom),
        outLine=(255,0,0,255),
        width=5)
# 出力画像をファイルに保存
image_in.save('compare_'+sys.argv[2])
# 出力画像を表示
image_in.show()
