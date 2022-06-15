# boto3インポート
import boto3
# jsonインポート
import json
# comprehendサービスクライアントを生成
comprehend = boto3.client('comprehend', 'us-east-1')
# 構文解析対象文字列の初期化
text = "I'm looking forward to visiting Japan next summer."
# 構文を解析
result = comprehend.detect_syntax(Text=text, LanguageCode='en')
# 結果を整形して表示
print(json.dumps(result, indent=2))