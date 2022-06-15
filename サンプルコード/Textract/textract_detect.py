# 各種ライブラリのインポート
import boto3
import json
import sys
from PIL import Image

# 引数チェック
if len(sys.argv) != 2:
    print('python', sys.argv[0], 'image')
    exit()

# Textractサービスクライアントを作成
textract = boto3.client('textract', 'us-east-1')
# 画像ファイルを開く
with open(sys.argv[1], 'rb') as file:
    # 文字列を検出
    result = textract.detect_document_text(
        Document={'Bytes': file.read()})
    # 結果を整形して表示
    print(json.dumps(result, indent=4))

# 入力画像のファイルを読み込む
image_in = Image.open(sys.argv[1])
# 画像サイズを取得
w, h = image_in.size
# 出力画像を作成
image_out = Image.new('RGB', (w, h), (200, 200, 200))
# 検出されたブロックを順番に処理
for block in result['Blocks']:
    # ブロックタイプが行かどうかを調べる
    if block['BlockType'] == 'LINE':
        # バウンディングボックスを取得
        box = block['Geometry']['BoundingBox']
        # 文字列の左、上、右、下の座標を計算
        left = int(box['Left']*w)
        top = int(box['Top']*h)
        right = left+int(box['Width']*w)
        bottom = top+int(box['Height']*h)
        # 入力画像から出力画像に文字列の部分を貼り付け
        image_out.paste(
            image_in.crop((left, top, right, bottom)), (left, top))
        # 文字列の内容を表示
        print(block['Text']),
# 出力画像をファイルに保存
image_out.save('detect_'+sys.argv[1])
# 出力画像を表示
image_out.show()
