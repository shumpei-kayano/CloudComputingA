# boto3 のインポート
import boto3
# Comprehendサービスクライアントを作成
comprehend = boto3.client('comprehend', 'us-east-1')
# テキストファイルを開く
with open('comp_phrase_ja.txt', 'r', encoding='utf-8') as file:
    # 文章からキーフレーズを抽出
    result = comprehend.detect_key_phrases(
        Text=file.read(), 
        LanguageCode='ja'
    )
    # レポート作成用の辞書を初期化
    report = {}
    # キーフレーズを順番に処理
    for phrase in result['KeyPhrases']:
        # 文字列とスコアを取得
        text, score = phrase['Text'], phrase['Score']
        # レポートにスコアと文字列を登録
        report[text] = '{:<018} {}'.format(score, text)
    # レポートをソートしてから表示
    for line in sorted(report.values(), reverse=True):
        print(line)