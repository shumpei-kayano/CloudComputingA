# boto3 をインポート
import boto3
# Polly サービスクライアントを作成
polly = boto3.client('polly')
# レキシコンファイルを開く
with open('my_lexicon.pls', 'r', encoding='utf-8') as file:
    # レキシコンを登録
    polly.put_lexicon(Name='MyLexicon', Content=file.read())
