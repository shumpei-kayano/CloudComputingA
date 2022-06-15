# boto3 をインポート
import boto3
# Translate サービスクライアントを作成
translate = boto3.client('translate')
# 日本語の文章
text = 'ひぐぺん工房の新しい本が秀和システムから出ます。'
# 日本語から英語に翻訳（登録した用語を使用）
result = translate.translate_text(
    Text=text, SourceLanguageCode='ja', 
    TargetLanguageCode='en',
    TerminologyNames=['term_ja'])
# 翻訳された文章を表示
print(result['TranslatedText'])
