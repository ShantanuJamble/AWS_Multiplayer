import boto3
import os


class S3Downloader(object):

    @staticmethod
    def GetFileList(bucket, folder_path, region='us-west-1'):
        file_list = []
        try:
            s3resource = boto3.resource('s3', region_name=region)
            s3Bucket = s3resource.Bucket(bucket)
            for obj in s3Bucket.objects.filter(Prefix=folder_path):
                file_list.append(obj.key)
            print(file_list)
            return file_list
        except Exception as e:
            raise Exception(str(e))

    @staticmethod
    def Downloadfiles(bucket, folder_path, local_path, region="us-west-1"):

        s3client = boto3.client('s3', region_name=region)
        s3resource = boto3.resource('s3', region_name=region)
        try:

            files_list = S3Downloader.GetFileList(bucket, folder_path, region)
            paginator = s3client.get_paginator('list_objects')
            # folder_data = s3resource.Object(bucket, folder_path).load()
            for result in paginator.paginate(Bucket=bucket, Delimiter='/', Prefix=folder_path):
                if result.get('CommonPrefixes') is not None:
                    print(result.get('CommonPrefixes'))
                    for subdir in result.get('CommonPrefixes'):
                        S3Downloader.Downloadfile(s3client, s3resource, local_path, subdir.get('Prefix'))
                if result.get('Contents') is not None:
                    for file in result.get('Contents'):
                        if not os.path.exists(os.path.dirname(local_path + os.sep + file.get('Key'))):
                            os.makedirs(os.path.dirname(local_path + os.sep + file.get('Key')))
                        print(os.path.dirname(file.get('Key')))
                        s3resource.meta.client.download_file(bucket, file.get('Key'),
                                                             local_path + os.sep + file.get('Key'))

            print("File found")
        except Exception as e:
            print(str(e))


'''if __name__ == "__main__":
    bucket = 'logs-gamelift'
    # file_path = 'Gamelift/AWSLogs/136816550245/CloudTrail/us-east-1/2019/11/09/136816550245_CloudTrail_us-east-1_20191109T2050Z_3LClu2QyVluXwhlq.json.gz'
    file_path = 'Gamelift/AWSLogs/136816550245/CloudTrail/us-east-1/2019/11/09/'
    local_path = "D:/PycharmProjects/GameLift_Monitor/downloads"
    S3Downloader.Downloadfile(bucket=bucket, folder_path=file_path, local_path=local_path)
'''