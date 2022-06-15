# boto3 をインポート
import boto3
# contextlib をインポート
import contextlib
# os をインポート
import os
# Translate サービスクライアントを作成
translate = boto3.client('translate')
# Polly サービスクライアントを作成
polly = boto3.client('polly')
# 翻訳するテキスト
text_ja = '一番近い駅までの道を教えてください。'
# 翻訳
result = translate.translate_text(
    Text=text_ja, # 翻訳するテキスト
    SourceLanguageCode='ja', # 翻訳元言語コード
    TargetLanguageCode='en' # 翻訳先言語コード
)
# 翻訳されたテキストを取り出す
text_en = result['TranslatedText']
# 翻訳されたテキストを標準出力
print(text_en)
# テキストから音声を合成
result = polly.synthesize_speech(
    Text=text_en, # 音声合成するテキスト
    OutputFormat='mp3', # 音声データのフォーマット
    VoiceId='Joanna' # 音声ID
)
# 出力ファイルのパス
path = 'polly_translate.mp3'
# 音声のストリームを開く
with contextlib.closing(result['AudioStream']) as stream:
    # 出力ファイルを開く
    with open(path, 'wb') as file:
        file.write(stream.read())
# 出力ファイルを再生する
if os.name == 'nt':
    os.startfile(path)