# boto3インポート
import boto3
# IAMサービスクライアントを作成
iam = boto3.client('iam')
# ポリシー（ForecastPolicy）を取得
for policy in iam.list_policies()['Policies']:
    if policy['PolicyName'] == 'ForecastPolicy':
        break
policy_arn = policy['Arn']
print('policy ARN:', policy_arn)
# ロールからポリシーを分離
iam.detach_role_policy(
    RoleName='ForecastRole', PolicyArn=policy_arn)
# ポリシーを削除
iam.delete_policy(PolicyArn=policy_arn)
# ロールを削除
iam.delete_role(RoleName='ForecastRole')