# boto3 をインポート
import boto3
# urllib をインポート
import urllib
# Translate サービスクライアントを作成
translate = boto3.client('translate')
# 用語データを取得
result = translate.get_terminology(
    Name='term_ja', TerminologyDataFormat='CSV')
# 用語データのURLを取得
url = result['TerminologyDataLocation']['Location']
# 用語データのURLを表示
print(url)
# 書き込み用のファイルを開く
with open('term_ja_download.csv', 'wb') as file_out:
    # 用語データのURLを開く
    with urllib.request.urlopen(url) as file_in:
        # 用語データをダウンロードしてファイルに書き込む
        file_out.write(file_in.read())
