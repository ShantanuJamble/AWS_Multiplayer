import boto3
import os


class S3Uploader(object):

    @staticmethod
    def upload_to_s3(bucket, s3_path, local_file_path, region='us-west-1'):
        try:
            s3client = boto3.client('s3', region_name=region)
            s3resource = boto3.resource('s3', region_name=region)
            s3Bucket = s3resource.Bucket(bucket)
            print (bucket,s3_path,local_file_path)
            s3client.upload_file(local_file_path, bucket, s3_path)
        except Exception as e:
            raise Exception(str(e))
