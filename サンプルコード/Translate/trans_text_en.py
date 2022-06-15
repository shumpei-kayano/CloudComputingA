# boto3をインポート
import boto3
# Translateサービスクライアントを作成
translate = boto3.client('translate')
# （１）英語の文章
text = "I'll send you an email later."
# （２）英語から日本語に翻訳
result = translate.translate_text(
    Text=text, SourceLanguageCode='en', TargetLanguageCode='ja'
)
# 翻訳語の文章を表示
print(result['TranslatedText'])
print('翻訳元の言語コード = {}'.format(result['SourceLanguageCode']))
print('翻訳語の言語コード = {}'.format(result['TargetLanguageCode']))