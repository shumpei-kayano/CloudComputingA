# 各種ライブラリのインポート
import boto3
import json
import sys
from PIL import Image

# 引数チェック
if len(sys.argv) != 2:
    print('正しく入力してください。','python', sys.argv[0], 'image')
    exit()

# 文字認識画像名設定(拡張子の削除)
s = sys.argv[1]
inputImageName = s.replace('.jpg', '')

# 出力ファイル名の指定
outputFileName = inputImageName + '_textract'
# 拡張子の設定
inputImageName = inputImageName + '.jpg'
outputFileName = outputFileName + '.txt'

# Textractサービスクライアントを作成
textract = boto3.client('textract', 'us-east-1')
# Translate サービスクライアントを作成
translate = boto3.client('translate')

# 画像ファイルを開いて文字認識処理
with open(inputImageName, 'rb') as file:
    # 文字列を検出
    result = textract.detect_document_text(
        Document={'Bytes': file.read()})
    # 結果を整形して表示
    # print(json.dumps(result, indent=4))

# 検出されたブロックを順番に処理
for block in result['Blocks']:
    # ブロックタイプが行かどうかを調べる
    if block['BlockType'] == 'LINE':
        # 文字列の内容を表示
        print(block['Text']),

# 出力ファイルを開く
with open(outputFileName, 'w', encoding='utf-8') as file_out:
    # 入力ファイルを１行ずつ読み込む
    for block in result['Blocks']:
        # ブロックタイプが行かどうかを調べる
        if block['BlockType'] == 'LINE':
            # 空行でなければ翻訳する
            if block['Text'] != '\n':
                result2 = translate.translate_text(
                        Text=block['Text'],
                        SourceLanguageCode='auto', 
                        TargetLanguageCode='ja',
                        TerminologyNames=['term_ja'])
                # 翻訳されたテキストをファイルに書き込む
                file_out.write(result2['TranslatedText'])
            # 改行をファイルに書き込む
            file_out.write('\n')

f = open(outputFileName, 'r', encoding='UTF-8')
data = f.read()
print('--------翻訳開始--------')
print(data)
f.close

