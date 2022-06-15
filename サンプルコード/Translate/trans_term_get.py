# boto3 をインポート
import boto3
# pprint をインポート
import pprint
# Translate サービスクライアントを作成
translate = boto3.client('translate')
# 用語データを取得
result = translate.get_terminology(
    Name='term_ja', TerminologyDataFormat='CSV')
# 結果を整形して表示
pprint.pprint(result)
