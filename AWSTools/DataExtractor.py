import pandas as pd
import boto3
import botocore
import json
import gzip
import os


class DataExtractor(object):

    @staticmethod
    def read_file(file_path):
        print(file_path)
        with gzip.open(file_path, 'rb') as f:
            file_content = f.read()
            # print(type(file_content.Str))
            data = json.loads(file_content)
            data = data['Records']
            records = list()
            for d in data:
                record = dict()
                record['eventTime'] = d['eventTime']
                record['eventName'] = d['eventName']
                record['awsRegion'] = d['awsRegion']
                record['sourceIPAddress'] = d['sourceIPAddress']
                record['userAgent'] = d['userAgent']
                record['eventType'] = d['eventType']
                record['requestID'] = d['requestID']
                record['eventID'] = d['eventID']
                record['userIdentity-type'] = d['userIdentity']['type']
                record['userIdentity-accessKeyId'] = d['userIdentity']['accessKeyId']
                if 'invokedBy' in d['userIdentity'].keys():
                    record['userIdentity-invokedBy'] = d['userIdentity']['invokedBy']
                else:
                    record['userIdentity-invokedBy'] = None
                if 'sessionContext' in d['userIdentity'].keys():
                    record['userIdentity-sessionContext'] = d['userIdentity']['sessionContext']
                else:
                    record['userIdentity-sessionContext'] = None
                records.append(record)
            print (len(records))
            return records
            # df = pd.DataFrame(records)
            # print (df.head(5))
            # df.to_csv('test.csv',index = False)

    @staticmethod
    def extract(folder_path):
        file_list = os.listdir(folder_path)
        count = 0
        df_test = None
        for f in file_list:
            if df_test is None:
                print("New df")
                df_test = pd.DataFrame(DataExtractor.read_file(folder_path + f))
            else:
                print("Appending df")
                df_tmp = pd.DataFrame(DataExtractor.read_file(folder_path + f))
                df_test = df_test.append(df_tmp, ignore_index=True)
        print(df_test.count())
        df_test.to_csv('test.csv', index=False)

if __name__ == "__main__":
    DataExtractor.getfilelist(
        "D:/PycharmProjects/GameLift_Monitor/downloads/Gamelift/AWSLogs/136816550245/CloudTrail/us-east-1/2019/11/09/")
