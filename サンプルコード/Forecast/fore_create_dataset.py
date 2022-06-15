# boto3インポート
import boto3
# jsonインポート
import json
# forecastサービスクライアントを作成
forecast = boto3.client('forecast')
# スキーマ定義
schema_json = {
    "Attributes": [
        # タイムスタンプ
        {
             "AttributeName": "timestamp",
             "AttributeType": "timestamp"
        },
        # 数値
        {
             "AttributeName": "target_value",
             "AttributeType": "float"
        },
        # アイテム
        {
             "AttributeName": "item_id",
             "AttributeType": "string"
        }
    ]
}
# データセットを作成
dataset_arn = forecast.create_dataset(
    Domain='CUSTOM', DatasetType='TARGET_TIME_SERIES',
    DatasetName='MyDataset', DataFrequency='M',
    Schema=schema_json)['DatasetArn']
print('dataset ARN:', dataset_arn)
# データセットグループを作成
group_arn = forecast.create_dataset_group(
    DatasetGroupName='MyGroup', Domain='CUSTOM',
    DatasetArns=[dataset_arn])['DatasetGroupArn']
print('dataset group ARN:', group_arn)