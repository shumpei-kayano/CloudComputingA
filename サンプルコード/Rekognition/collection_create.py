import boto3
import json
import sys

# コマンドライン引数が不適切ならば使い方を表示して終了
if len(sys.argv) == 1:
    print('python', sys.argv[0], 'images...')
    exit()

# Rekognition サービスクライアントを作成
rekognition = boto3.client('rekognition')
# コレクションID
collection_id = 'MyCollection_takeda'

# コレクションの作成
print('create_collection:')
# コレクションを作成する
result = rekognition.create_collection(CollectionId=collection_id)
# コレクションの作成結果を表示
print(json.dumps(result, indent=4))

# 顔の登録
print('index_faces:')
# コマンドライン引数に指定された画像ファイルを順番に処理
for path in sys.argv[1:]:
    # 画像ファイルを開く
    with open(path, 'rb') as file:
        # 画像内の顔を登録
        result = rekognition.index_faces(
            CollectionId=collection_id,
            Image={'Bytes': file.read()})
        # 顔の登録結果を表示
        print(json.dumps(result, indent=4))

# コレクションの一覧の表示
print('list_collections:')
# コレクションの一覧を取得
result = rekognition.list_collections()
# コレクションの一覧を表示
print(json.dumps(result, indent=4))

print('list_faces:')
# 登録された顔の一覧を取得
result = rekognition.list_faces(CollectionId=collection_id)
# 登録された顔の一覧を表示
print(json.dumps(result, indent=4))
