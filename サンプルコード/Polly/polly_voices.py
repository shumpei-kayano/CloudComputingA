# boto3 をインポート
import boto3
# pprint をインポート
import pprint
# Polly サービスクライアントを作成
polly = boto3.client('polly')
# 音声IDの一覧を取得
result = polly.describe_voices()
# 取得した結果を整形して表示
pprint.pprint(result)