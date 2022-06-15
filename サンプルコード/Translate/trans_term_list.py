# boto3 をインポート
import boto3
# pprint をインポート
import pprint
# Translate サービスクライアントを作成
translate = boto3.client('translate')
# 登録名の一覧を取得
result = translate.list_terminologies()
# 結果を整形して表示
pprint.pprint(result)
