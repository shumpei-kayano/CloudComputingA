# boto3 をインポート
import boto3
# Polly サービスクライアントを作成
polly = boto3.client('polly')
# レキシコンを削除
polly.delete_lexicon(Name='MyLexicon')