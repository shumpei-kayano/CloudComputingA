# boto3インポート
import boto3
# jsonインポート
import json
# Comporehendサービスクライアントを生成
comprehend = boto3.client('comprehend', 'us-east-1')
# 処理対象の文字列
text = "I tried to use the 20% OFF coupon, \
but only 10% discount and I was unable to place an order."
# キーフレーズを抽出
result = comprehend.detect_key_phrases(Text=text, LanguageCode='en')
# 結果をJSON形式に整形して表示
print(json.dumps(result, indent=2))