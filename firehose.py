import json
import boto3

session = boto3.Session(profile_name='default')
client = session.client('firehose')


with open("/Users/qiac/Downloads/json1.txt") as json_file:
    observations = json.load(json_file)
    for observation in observations:
        print(observation)
        response = client.put_record(
           DeliveryStreamName='case1',
           Record={
                'Data': json.dumps(observation)
            }
        )
        print(response)