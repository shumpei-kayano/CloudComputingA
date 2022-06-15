# 各種ライブラリのインポート
import boto3
import json
import sys
from PIL import Image

# 引数チェック
if len(sys.argv) != 2:
    print('python', sys.argv[0], 'image')
    exit()

try:
    # Textractサービスクライアントを作成
    textract = boto3.client('textract', 'us-east-1')
    # Translate サービスクライアントを作成
    translate = boto3.client("translate")
# エラーが発生した場合
except Exception as e:
    print("AWSに接続できませんでした.")
    print(e)
    print("プログラムを終了します.")
    exit()

try:
    # 画像ファイルを開く
    with open(sys.argv[1], 'rb') as file:
        # 文字列を検出
        result = textract.detect_document_text(
            Document={'Bytes': file.read()})
# 画像が開けなかった場合
except Exception as e:
    print("画像が開けませんでした.")
    print(e)
    print("プログラムを終了します.")
    exit()

# ファイル名を"."で分割
filename_split = sys.argv[1].split(".")
# ファイル名の拡張子以外の取り出し
filename_base = ".".join(filename_split[0:-1])
# ファイル拡張子の取り出し
filename_ext = filename_split[-1]
# 出力ファイル名のに"_textract"を付加する
filename_out = filename_base+"_textract.txt"

text=""

# 出力ファイルを開く
with open(filename_out, "w", encoding="utf-8") as file:
    # 検出されたブロックを順番に処理
    for block in result['Blocks']:
        # ブロックタイプが行かどうかを調べる
        if block['BlockType'] == 'LINE':
            # 文字列の内容を取得
            text_line = block['Text']
            # 文字列の内容を表示
            print(text_line)
            # 出力ファイルに書き出す
            file.write(text_line + "\n")

            text += text_line+" "

            if text_line[-1:] == ".":
                text += "\n "

print("翻訳開始")

result = translate.translate_text(
    Text=text,
    SourceLanguageCode="auto",
    TargetLanguageCode="ja")
# 翻訳されたテキストをディスプレイに表示する
print(result['TranslatedText'], end="")