# boto3, sysインポート
import boto3
import sys
# コマンドライン引数の個数が不適切ならば使い方を表示して終了
if len(sys.argv) != 2:
    print('python', sys.argv[0], 'item-id')
    exit()
# Forecastサービスクライアントを作成
forecast = boto3.client('forecast')
# ForecastQueryサービスクライアントを作成
forecast_query = boto3.client('forecastquery')
# 予測（MyForecast）を取得
for fc in forecast.list_forecasts()['Forecasts']:
    if fc['ForecastName'] == 'MyForecast':
        break
forecast_arn = fc['ForecastArn']
# 指定したアイテムIDに関する予測値を取得
result = forecast_query.query_forecast(
    ForecastArn=forecast_arn,
    Filters={'item_id': sys.argv[1]})
# 予測値を分位点（P10, P50, P90）ごとに表示
for prediction in result['Forecast']['Predictions']:
    print(prediction+':')
    # タイムスタンプと予測値を表示
    for line in result['Forecast']['Predictions'][prediction]:
        print(line['Timestamp'], line['Value'])
    print()