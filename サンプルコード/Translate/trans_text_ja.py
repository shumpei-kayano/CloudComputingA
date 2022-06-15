# (1) boto3 をインポート
import boto3
# (2) Translate サービスクライアントを作成
translate = boto3.client('translate')
# (3) 日本語の文章
text = 'あとでメールを送ります。'
# (4) 日本語から英語に翻訳
result = translate.translate_text(
            Text=text, SourceLanguageCode='ja', 
            TargetLanguageCode='en')
# (5) 翻訳後の文章を表示
print(result['TranslatedText'])
# 翻訳元の言語コードを表示
print('翻訳元の言語コード = {}'.format(result['SourceLanguageCode']))
# 翻訳先の言語コードを表示
print('翻訳先の言語コード = {}'.format(result['TargetLanguageCode']))