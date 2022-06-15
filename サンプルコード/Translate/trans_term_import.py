# boto3 をインポート
import boto3
# Translate サービスクライアントを作成
translate = boto3.client('translate')
# CSVファイルを開く
with open('term_ja.csv', 'rb') as file:
    # 用語を登録
    translate.import_terminology(
        Name='term_ja',
        MergeStrategy='OVERWRITE',
        TerminologyData={'File': file.read(), 'Format': 'CSV'})
