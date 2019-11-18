from DataExtractor import *
from s3Downloader import *
from S3Uploader import *
import datetime
import json


def lambda_handler(event, context):
    bucket = 'logs-gamelift'
    download_location = "D:/PycharmProjects/GameLift_Monitor/"
    s3_prefix = 'Gamelift/AWSLogs/136816550245/CloudTrail/'
    aws_region = 'us-east-1'
    date = datetime.date.today()
    print(date.day, date.month, date.year)
    date = '2019/11/09/'
    s3_download_file_path = s3_prefix + aws_region+ '/' + date
    s3_upload_path = 'cleaned_data'
    S3Downloader.Downloadfiles(bucket=bucket, folder_path=s3_download_file_path, local_path=download_location)
    DataExtractor.extract(download_location+s3_download_file_path)
    S3Uploader.upload_to_s3(bucket=bucket,s3_path=s3_upload_path+'/test.csv',local_file_path=os.path.join('test.csv'))
    print('Done done done')


lambda_handler('','')