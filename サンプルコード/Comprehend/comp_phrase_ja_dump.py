# boto3インポート
import boto3
# jsonインポート
import json
# Comporehendサービスクライアントを生成
comprehend = boto3.client('comprehend', 'us-east-1')
# 処理対象の文字列
text = "20％OFFクーポンを使おうとしたのですが、\
  10％割引で注文できませんでした。"
# キーフレーズを抽出
result = comprehend.detect_key_phrases(Text=text, LanguageCode='ja')
# 結果をJSON形式に整形して表示
print(json.dumps(result, indent=2, ensure_ascii=False))