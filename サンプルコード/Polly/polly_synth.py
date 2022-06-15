# boto3 をインポート
import boto3
# contextlib をインポート
import contextlib
# os をインポート
import os
# Polly サービスクライアントを作成
polly = boto3.client('polly')
# 音声合成するテキスト
text = 'こんにちは！音声合成を使ったプログラムを一緒に作りましょう。'
# テキストから音声を合成
result = polly.synthesize_speech(
    Text=text, OutputFormat='mp3', VoiceId='Takumi')
# 出力ファイルのパス
path = 'polly_synth.mp3'
# 音声のストリームを開く
with contextlib.closing(result['AudioStream']) as stream:
  # 出力ファイルを開く
  with open(path, 'wb') as file:
    file.write(stream.read())
# 出力ファイルを再生する
if os.name == 'nt':
  os.startfile(path)