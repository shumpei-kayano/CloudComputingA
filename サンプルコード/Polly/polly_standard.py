# boto3 をインポート
import boto3
# contextlib をインポート
import contextlib
# os をインポート
import os

# Polly サービスクライアントを作成
polly = boto3.client('polly')
# 音声合成するテキスト
text = 'Hello everyone! Welcome to the Programming World Report.'
# 音声合成する
result = polly.synthesize_speech(
    Text=text,  # 音声合成するテキスト
    OutputFormat='mp3', # 音声のフォーマット
    VoiceId='Matthew'    # 音声ID
)
# 出力ファイルのパス
path = 'polly_standard.mp3'
# 音声のストリームを開く
with contextlib.closing(result['AudioStream']) as stream:
    # 出力ファイルを開く
    with open(path, 'wb') as file:
        # 音声を読み込んで出力ファイルに書き込む
        file.write(stream.read())
# 出力ファイルを再生する
if os.name == 'nt':
    os.startfile(path)
