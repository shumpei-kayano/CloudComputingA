# boto3, json, uuid, time インポート
import boto3
import json
import uuid
import time
# s3サービスクライアントを作成
region = 'ap-northeast-1'
s3 = boto3.client('s3', region)
# バケット名を生成
bucket = str(uuid.uuid1())
print('bucket:', bucket)
# バケットを作成
s3.create_bucket(
    Bucket=bucket,
    CreateBucketConfiguration={'LocationConstraint': region})
# バケットのポリシーを定義
policy_json = {
    "Version": "2012-10-17",
    "Id": "ForecastS3BucketAccessPolicy",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "forecast.amazonaws.com"
            },
            "Action": [
                "s3:Get*",
                "s3:List*",
                "s3:PutObject"
            ],
            "Resource": [
                "arn:aws:s3:::"+bucket,
                "arn:aws:s3:::"+bucket+"/*"
            ]
        }
    ]
}
# バケットにポリシーを追加
s3.put_bucket_policy(Bucket=bucket, Policy=json.dumps(policy_json))
# s3にファイルをアップロード
file_name = 'temperature.csv'
s3.upload_file(file_name, bucket, file_name)
# ロール（ForecastRole）のARNを取得
iam = boto3.client('iam')
role_arn = iam.get_role(RoleName='ForecastRole')['Role']['Arn']
# Forecastサービスクライアントを作成
forecast = boto3.client('forecast', region)
# データセット（MyDataset）を取得
for dataset in forecast.list_datasets()['Datasets']:
    if dataset['DatasetName'] == 'MyDataset':
        break
dataset_arn = dataset['DatasetArn']
# データ取り込みのジョブを開始
job_arn = forecast.create_dataset_import_job(
    DatasetImportJobName='MyJob',
    DatasetArn=dataset_arn,
    DataSource={'S3Config': {
        'Path': 's3://'+bucket+'/'+file_name, 'RoleArn': role_arn}},
    TimestampFormat='yyyy-MM-dd hh:mm:ss')['DatasetImportJobArn']
print('job ARN:', job_arn)
# データ取り込みのジョブの進捗を表示
start = time.time()
status = ''
while status in ['CREATE_PENDING', 'CREATE_IN_PROGRESS']:
    status = forecast.describe_dataset_import_job(
        DatasetImportJobArn=job_arn)['DatasetImportJob']['Status']
    time.sleep(10)
    print('{:7.2f} {}'.format(time.time()-start, status))