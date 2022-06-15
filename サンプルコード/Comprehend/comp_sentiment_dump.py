# 各種ライブラリのインポート
import boto3
import json

# Comprehendサービスクライアントを作成
comprehend = boto3.client('comprehend', 'us-east-1')
# 処理対象の文字列
text = "I'm looking forward to visiting Japan next summer."
# 感情を分析
result = comprehend.detect_sentiment(Text=text, LanguageCode='en')
# 結果を整形して表示
print(json.dumps(result, indent=2))
