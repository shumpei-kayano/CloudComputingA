# boto3 をインポート
import boto3
# json をインポート
import json
import pprint
# リージョンを指定して Translate サービスクライアントを作成
translate = boto3.client('translate', 'us-east-2')
# 入力ファイルを開く
with open('trans_json_in.json', 'r', encoding='utf-8') as file_in:
  # JSON ファイルを読み込む
  reviews = json.load(file_in)
  pprint.pprint(reviews)
# レビューを１件ずつ処理する
for review in reviews:
  # レビューの本文を翻訳する
  result = translate.translate_text(
        Text=review['Text'],
        SourceLanguageCode='auto', TargetLanguageCode='ja')
  # レビューの本文を翻訳結果に置き換える
  review['Text'] = result['TranslatedText']
# 出力ファイルを開く
with open('trans_json_out.json', 'w', encoding='utf-8') as file_out:
  # JSON ファイルを書き込む
  json.dump(reviews, file_out, indent=4, ensure_ascii=False)
