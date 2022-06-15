# boto3 をインポート
import boto3
# json をインポート
import json
# sys をインポート
import sys

# 引数チェック
if len(sys.argv) != 2:
    # プログラム名を含む引数の個数が２でないとき
    # 実行形式を表示
    print('python', sys.argv[0], 'image')
    # プログラムを強制終了
    exit()

# rekognition サービスクライアントを作成
rekognition = boto3.client('rekognition')
# 画像ファイルをオープン
with open(sys.argv[1], 'rb') as file:
    # 顔を検出
    result = rekognition.detect_faces(Image={'Bytes': file.read()})
    # 結果を整形して表示
    print(json.dumps(result, indent=4))
