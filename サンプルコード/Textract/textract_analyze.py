# 各種ライブラリのインポート
import boto3
import json
import sys

# 引数チェック
if len(sys.argv) != 2:
    print('python', sys.argv[0], 'image')
    exit()

# Textractサービスクライアントを作成
textract = boto3.client('textract', 'us-east-1')
# 画像ファイルを開く
with open(sys.argv[1], 'rb') as file:
    # 表やフォームを検出
    result = textract.analyze_document(
        Document={'Bytes': file.read()},
        FeatureTypes=['TABLES', 'FORMS'])
    # 結果を整形して表示
    print(json.dumps(result, indent=2))

