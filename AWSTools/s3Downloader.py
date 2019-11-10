import boto3
import botocore
import pandas as pd
import json
import os


class S3Downloader(object):


    @staticmethod
    def GetFileList(bucket,folder_path,region= 'us-west-1'):
        file_list = []
        try:
            s3resource = boto3.resource('s3', region_name=region)
            s3Bucket = s3resource.Bucketx(bucket)
            for obj in  s3Bucket.objects.filter(Prefix=folder_path):
                file_list.append(obj.key)
            print (file_list)
        except Exception as e:
            raise Exception(str(e))


    @staticmethod
    def Downloadfile(bucket, file_path, region="us-west-1"):

        s33client = boto3.client('s3', region_name=region)
        s3resource = boto3.resource('s3', region_name=region)
        try:
            folder = s3resource.Object(bucket, file_path).load()
            print("File found")
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] == "404":
                exists = False
            else:
                raise


if __name__ == "__main__":
    bucket = 'logs-gamelift'
    #file_path = 'Gamelift/AWSLogs/136816550245/CloudTrail/us-east-1/2019/11/09/136816550245_CloudTrail_us-east-1_20191109T2050Z_3LClu2QyVluXwhlq.json.gz'
    file_path = 'Gamelift/AWSLogs/136816550245/CloudTrail/us-east-1/2019/11/09/'
    test = S3Downloader.GetFileList(bucket=bucket, folder_path=file_path)
