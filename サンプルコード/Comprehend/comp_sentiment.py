# boto3インポート
import boto3
# csvインポート
import csv
# リージョンを設定
region = 'us-east-1'
# Translateサービスクライアントを生成
translate = boto3.client('translate', region)
# Comprehendサービスクライアントを生成
comprehend = boto3.client('comprehend', region)
# CSVファイルの読み込み
with open('comp_sentiment.csv', 'r', encoding='utf-8') as file:
    # 行単位で読み込む
    for row in csv.reader(file):
        # ３列目の文字列を英語に翻訳
        result_en = translate.translate_text(
            Text=row[2],
            SourceLanguageCode='auto',
            TargetLanguageCode='en')
        # ３列目の文字列を日本語に翻訳
        result_ja = translate.translate_text(
            Text=row[2],
            SourceLanguageCode='auto',
            TargetLanguageCode='ja')
        # 英語に翻訳された列の文字列の感情を分析
        result_comp = comprehend.detect_sentiment(
            Text=result_en['TranslatedText'],
            LanguageCode='en')
        # 原文を表示
        print(row[2])
        # 翻訳された英文を表示
        print('(', result_en['TranslatedText'], ')')
        # 翻訳された日本文を表示
        print('(', result_ja['TranslatedText'], ')')
        # 感情を表示
        print(result_comp['Sentiment'])
        # 各感情の情報を取得
        for key, value in result_comp['SentimentScore'].items():
            # 各感情の名前とスコアを表示
            print('  {:10} {}'.format(key, value))
        print() # 改行