# boto3インポート
import boto3
# Forecastサービスクライアントを作成
forecast = boto3.client('forecast')
# 予測を取得
for fc in forecast.list_forecasts()['Forecasts']:
    forecast_arn = fc['ForecastArn']
    print('forecast ARN:', forecast_arn)
    # 予測を削除
    forecast.delete_forecast(ForecastArn=forecast_arn)
# 予測子を取得
for predictor in forecast.list_predictors()['Predictors']:
    predictor_arn = predictor['PredictorArn']
    print('predictor ARN:', predictor_arn)
    # 予測子を削除
    forecast.delete_predictor(PredictorArn=predictor_arn)