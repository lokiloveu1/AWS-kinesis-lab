import boto3
from faker import Faker
from loguru import logger
import random
from datetime import datetime
import json
import time


fake = Faker()

def generate_visit(fraud_ip_list, fraud_ip_prob, fraud_ssn_list, fraud_ssn_prob):
    ret = {
        'applicant': random.randint(100000000,800000000),
        'ip_address': fake.ipv4(),
        'ssn': fake.ssn(),
        'product': random.choice(['credit_card', 'personal_loan', 'checking', 'savings']),
        'ts': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    if random.random() < fraud_ip_prob:
        ret['ip_address'] = random.choice(fraud_ip_list)
    if random.random() < fraud_ssn_prob:
        ret['ssn'] = random.choice(fraud_ssn_list)
    return ret

STREAM_NAME = "twitter2"
# make up some fraud ips and ssns
FRAUD_IPS = ['1.1.1.1','2.2.2.2','3.3.3.3', '4.4.4.4']
FRAUD_SSN = ['666-12-3456','666-23-4567', '666-34-5678', '666-45-6789']
fraud_ssn_prob = 0.5 # one in a thousand simulated apps have fraudulent ssn
fraud_ip_prob = 0.5 # one in one hundred apps come from a fraud ip

def generate(stream_name, kinesis_client):
    while True:
        time.sleep(5)
        data = generate_visit(FRAUD_IPS, fraud_ip_prob, FRAUD_SSN, fraud_ssn_prob)
        logger.info(data)
        response = kinesis_client.put_record(
            StreamName = stream_name,
            Data = json.dumps(data),
            PartitionKey="shard1"
        )
       # logger.info(response)

if __name__ == '__main__':
    generate(STREAM_NAME, boto3.client('twitter2', region_name='ap-southeast-2'))
