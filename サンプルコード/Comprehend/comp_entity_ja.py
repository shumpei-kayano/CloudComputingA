# boto3インポート
import boto3
# Comprehendサービスクライアントを作成
comprehend = boto3.client('comprehend', 'us-east-1')
# 分析対象テキスト
text = "来年の夏に日本を訪れるのを楽しみにしています。"
# エンティティを認識（日本語）
result = comprehend.detect_entities(Text=text, LanguageCode='ja')
# 認識結果を整形して表示
for entity in result['Entities']:
    print('{:20} {:20} {:<018}'.format(
        entity['Text'], entity['Type'], entity['Score']))