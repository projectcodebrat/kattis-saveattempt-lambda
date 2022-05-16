import boto3
import json

_BUCKET_NAME = "codebrat-kattis-code";

def lambda_handler(event, context):
    data = json.loads(event['body'])
    
    username = data['username']
    problem_id = data['problem_id']
    language = data['language']
    code = data['code']

    file_name = "Main.{}".format(language)
    s3_path = "{}/{}/".format(username, problem_id) + file_name;

    s3 = boto3.resource("s3")
    s3.Bucket(_BUCKET_NAME).put_object(Key=s3_path, Body=code.encode("utf-8"))
    
    print("submission uploaded")
    
    return make_response(200, "submission successfully saved")

def make_response(status_code, message):
    return {
        'statusCode': status_code,
        'body': json.dumps(message)
    }