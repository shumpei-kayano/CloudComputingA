# 各種ライブラリーのインポート
import boto3
import json

# Comprehend サービスクライアントを作成
comprehend = boto3.client('comprehend', 'us-east-1')
# 処理対象の文字列を設定
text = "来年の夏に日本を訪れるのを楽しみにしています。"
# 言語を検出
result = comprehend.detect_dominant_language(Text=text)
# 結果を整形して表示
print(json.dumps(result, indent=2))
