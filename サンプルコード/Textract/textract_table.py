# 各種ライブラリをインポート
import boto3
import csv
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
    print(json.dumps(result, indent=4))

# 検出された文字列を格納するために空の辞書を作成
text = {}
# 検出されたブロックを順番に処理
for block in result['Blocks']:
    # ブロックに文字列が含まれていたら辞書に追加
    if 'Text' in block:
        text[block['Id']] = block['Text']

# 検出されたセルを格納するために空の辞書を作成
cell = {}
# 検出されたブロックを順番に処理
for block in result['Blocks']:
    # ブロックタイプがセルかどうか調べる
    if block['BlockType'] == 'CELL':
        # 行番号と列番号を取得
        row = int(block['RowIndex'])-1
        column = int(block['ColumnIndex'])-1
        # 辞書にセルを追加
        cell[(row, column)] = ''
        # ブロック内の他のブロックを順番に処理
        if 'Relationships' in block:
            for relationship in block['Relationships']:
                # 他のブロックのIDを順番に処理
                if relationship['Type'] == 'CHILD':
                    for id in relationship['Ids']:
                        # セル内の文字列を辞書に登録
                        if id in text:
                            cell[(row, column)] += text[id]+' '

# 列の処理（４列分）
for row in range(8):
    for column in range(4):
        # セル内の文字列を出力
        if (row, column) in cell:
            print('{:20}'.format(cell[(row, column)]), end='')
    # 改行
    print()
