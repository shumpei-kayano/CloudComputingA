# boto3 をインポート
import boto3
# cotextlib をインポート
import contextlib

# Polly サービスクライアントを作成
polly = boto3.client('polly')
# 音声合成するテキスト
text = 'スピーチマークを出力してみます。'
# テキストからスピーチマークを作成
result = polly.synthesize_speech(
    Text=text, OutputFormat='json', VoiceId='Mizuki',
    SpeechMarkTypes=['sentence', 'word', 'viseme'])
# 出力ファイルのパス
path = 'polly_mark.txt'
# 音声のストリームを開く
with contextlib.closing(result['AudioStream']) as stream:
    # 出力ファイルを開く
    with open(path, 'wb') as file:
        # 音声（スピーチマーク）を読み込んで出力ファイルに書き込む
        file.write(stream.read())
