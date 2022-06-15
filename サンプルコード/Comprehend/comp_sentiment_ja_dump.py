# 各種ライブラリのインポート
import boto3
import json

# Comprehendサービスクライアントを作成
comprehend = boto3.client('comprehend', 'us-east-1')
# 処理対象の文字列
text = "来年の夏に日本を訪れるのを楽しみにしています。"
# 感情を分析
result = comprehend.detect_sentiment(Text=text, LanguageCode='ja')
# 結果を整形して表示
print(json.dumps(result, indent=2))
