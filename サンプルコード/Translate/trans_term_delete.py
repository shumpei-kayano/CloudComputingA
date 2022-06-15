# boto3 をインポート
import boto3
# Translate サービスクライアントを作成
translate = boto3.client('translate')
# 用語を削除
translate.delete_terminology(Name='term_ja')