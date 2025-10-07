import boto3, sys, configparser

config = configparser.ConfigParser()
config.read('config.ini')

aws_access = config['AWS']['access_key']
aws_secret = config['AWS']['secret_key']
bucket_name = config['AWS']['bucket']

file_path = sys.argv[1]

s3 = boto3.client('s3', aws_access_key_id=aws_access,
                  aws_secret_access_key=aws_secret)

try:
    s3.upload_file(file_path, bucket_name, file_path.split('/')[-1])
    print("UPLOAD_SUCCESS")
except Exception as e:
    print("UPLOAD_FAIL", e)