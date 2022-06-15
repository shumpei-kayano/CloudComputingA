# boto3インポート
import boto3
# jsonインポート
import json
# IAMサービスクライアントを作成
iam = boto3.client('iam', 'us-east-1')
# ロールの定義
role_json = {
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
        "Principal": {
          "Service": "forecast.amazonaws.com"
         },
      "Action": "sts:AssumeRole"
    }
  ]
}
# ロールの作成
role = iam.create_role(
    RoleName='ForecastRole',
    AssumeRolePolicyDocument=json.dumps(role_json))
print('role ARN:', role['Role']['Arn'])
# ポリシーの定義
policy_json = {
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
        "s3:Get*",
        "s3:List*",
        "s3:PutObject"
      ],
      "Effect":"Allow",
      "Resource":[
        "arn:aws:s3:::*"
       ]
    }
  ]
}
# ポリシーを作成
policy = iam.create_policy(
    PolicyName='ForecastPolicy',
    PolicyDocument=json.dumps(policy_json))
print('policy ARN:', policy['Policy']['Arn'])
# ロールにポリシーを追加
iam.attach_role_policy(
    RoleName='ForecastRole',
    PolicyArn=policy['Policy']['Arn'])