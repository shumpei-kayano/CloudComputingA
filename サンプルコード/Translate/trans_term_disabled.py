# boto3 をインポート
import boto3
# Translate サービスクライアントを作成
translate = boto3.client('translate')
# 日本語の文章
text = 'ひぐぺん工房の新しい本が秀和システムから出ます。'
# 日本語から英語に翻訳
result = translate.translate_text(
    Text=text, SourceLanguageCode='ja', 
    TargetLanguageCode='en')
# 翻訳されたテキストを表示
print(result['TranslatedText'])