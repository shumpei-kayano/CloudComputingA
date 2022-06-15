# boto3 をインポート
import boto3
# Translate サービスクライアントを作成
translate = boto3.client('translate')
# 入力ファイルの指定
inputFileName = input("翻訳するファイル名を入力してください。(拡張子を除く)\n>>>")
# 出力ファイル名の指定
outputFileName = inputFileName + '_trans'
# 拡張子の設定
inputFileName = inputFileName + '.txt'
outputFileName = outputFileName + '.txt'
# 入力ファイルを開く
with open(inputFileName, 'r', encoding='utf-8') as file_in:
  # 翻訳言語の指定
  SourceLanguage = input('翻訳言語を指定してください。\n日本語:ja 英語:en イタリア語:it\n韓国語:ko ロシア語:ru 中国語（簡体）:zh\n>>>')
  # 出力ファイルを開く
  with open(outputFileName, 'w', encoding='utf-8') as file_out:
    # 入力ファイルを１行ずつ読み込む
    for text in file_in:
      # 空行でなければ翻訳する
      if text != '\n':
        result = translate.translate_text(
                    Text=text,
                    SourceLanguageCode='auto', 
                    TargetLanguageCode=SourceLanguage,
                    TerminologyNames=['term_ja'])
        # 翻訳されたテキストをファイルに書き込む
        file_out.write(result['TranslatedText'])
      # 改行をファイルに書き込む
      file_out.write('\n')
