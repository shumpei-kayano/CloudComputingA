# boto3インポート
import boto3
# comprehendサービスクライアントを生成
comprehend = boto3.client('comprehend', 'us-east-1')
# 構文解析対象文字列の初期化
text = "I'm looking forward to visiting Japan next summer."
# 構文を解析
result = comprehend.detect_syntax(Text=text, LanguageCode='en')

for token in result['SyntaxTokens']:
    print('{:20} {:20} {:<018}'.format(
        token['Text'],
        token['PartOfSpeech']['Tag'],
        token['PartOfSpeech']['Score']))
