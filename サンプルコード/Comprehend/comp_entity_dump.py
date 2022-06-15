# boto3インポート
import boto3
# jsonインポート
import json
# comprehendサービスクライアントを生成
comprehend = boto3.client('comprehend', 'us-east-1')
# エンティティ認識対象文字列の初期化
text = "I'm looking forward to visiting Japan next summer."
# エンティティを認識
result = comprehend.detect_entities(Text=text, LanguageCode='en')
# 結果をJSON形式で整形表示
print(json.dumps(result, indent=4))