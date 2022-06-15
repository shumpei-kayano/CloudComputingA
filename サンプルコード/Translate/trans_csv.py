# boto3 インポート
import boto3
# csv をインポート
import csv
# リージョンを指定して Translate サービスクライアントを作成
translate = boto3.client('translate', 'us-east-2')
# 入力ファイルを開く
with open('trans_csv_in.csv', 'r', encoding='utf-8') as file_in:
  # 出力ファイルを開く
  with open('trans_csv_out.csv', 'w', encoding='utf-8',
              newline='') as file_out:
    # csv を出力する準備
    writer = csv.writer(file_out)
    # 入力するファイルを１行ずつ読み込む
    for row in csv.reader(file_in):
      print(row)
      # レビューの本文を翻訳する
      result = translate.translate_text(
                Text=row[2],
                SourceLanguageCode='auto', 
                TargetLanguageCode='ja')
      # レビューの本文を翻訳結果に書き換える
      row[2] = result['TranslatedText']
      # 出力ファイルに書き込む
      writer.writerow(row)
