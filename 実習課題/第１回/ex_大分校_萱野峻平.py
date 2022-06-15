# boto3 をインポート
import boto3
# contextlib をインポート
import contextlib
# os をインポート
import os
# Polly サービスクライアントを作成
polly = boto3.client('polly')
# レキシコンファイルを開く
with open('tic_lexicon.pls', 'r', encoding='utf-8') as file:
    # レキシコンを登録
    polly.put_lexicon(Name='TICLexicon', Content=file.read())
# textの初期化
text = ''
totalText = ''

while text != '###':
    # 音声合成するテキストを入力
    text = input('音声合成するテキストを入力してください。\n終了する場合は###を入力してください。\n>>>')
    totalText = totalText + text
# 音声IDの選択
voice = input('出力する音声を入力してください。\nMizuki ⇨ 1（デフォルト）\nTakumi ⇨ 2\n>>>')
if(voice == 2):
    voiceName = 'Takumi'
else:
    voiceName = 'Mizuki'
# 音声合成する
result = polly.synthesize_speech(
    Text=totalText, # 音声合成するテキスト
    OutputFormat='mp3', # 音声のフォーマット
    VoiceId=voiceName, # 音声ID
    LexiconNames=['TICLexicon'] # 使用するレキシコン
)
# 出力ファイルのパス
path = 'polly_ensyu.mp3'
# 音声のストリームを開く
with contextlib.closing(result['AudioStream']) as stream:
    # 出力ファイルを開く
    with open(path, 'wb') as file:
        # 音声を読み込んで出力ファイルに書き込む
        file.write(stream.read())
# 出力ファイルを再生する
if os.name == 'nt':
    os.startfile(path)