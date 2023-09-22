import boto3
import time
import os
import json


handler_name = "cc_project"
ip_bucket = "cc-paas-inputs"
op_bucket = "cc-project-csv-files"
region = 'us-east-1'
access_key = '#############'
secret_key = '#############'
videos = {}
csv_files = {}



aws_lambda = boto3.client("lambda", region_name=region, aws_access_key_id=access_key,
                             aws_secret_access_key=secret_key)
s3 = boto3.client("s3", region_name=region, aws_access_key_id=access_key,
                         aws_secret_access_key=secret_key)


def trigger_lambda():
    input_file_list = s3.list_objects_v2(Bucket=ip_bucket)
    if input_file_list['KeyCount'] > 0:
        for file in input_file_list['Contents']:
            key = file['Key']
            if key not in videos:
                videos[key] = "present"
                event = {"Records": [{"s3": {"bucket": {"name": ip_bucket},"object":{"key": key}}}]}
                response = aws_lambda.invoke(
                    FunctionName=handler_name,
                    InvocationType='Event',
                    Payload=json.dumps(event),
                )

                print("Lambda function is triggered for file "+key)


def download_csv():
    output_file_list = s3.list_objects_v2(Bucket=op_bucket)

    if output_file_list['KeyCount'] > 0:
        for csv_file in output_file_list['Contents']:
            key = csv_file['Key']
            if key not in csv_files:
                csv_files[key] = "present"
                s3.download_file(op_bucket, key, 'results/'+key)
                print("csv file downloaded for "+key)

def main():
    while True:
        trigger_lambda()
        download_csv()
        time.sleep(2)


if __name__ == "__main__":
    main()
