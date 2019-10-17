import boto3
import time
import json
## aws creds are stored in ~/.boto
import time

kinesis = boto3.client("kinesis")
shard_id = "shardId-000000000001" #only one shard!
pre_shard_it = kinesis.get_shard_iterator(StreamName="twitter", ShardId=shard_id, ShardIteratorType="LATEST")
shard_it = pre_shard_it["ShardIterator"]
while 1==1:
     out = kinesis.get_records(ShardIterator=shard_it,limit=1)
     #time.sleep(2.0)

     shard_it = out["NextShardIterator"]
     if out['Records'] != []:
         print(out)
     



shard_id2 = "shardId-0000000000002" #only one shard!
pre_shard_it2 = kinesis.get_shard_iterator(StreamName="twitter", ShardId=shard_id2, ShardIteratorType="LATEST")
shard_it2 = pre_shard_it2["ShardIterator"]
while 1==1:
     out = kinesis.get_records(ShardIterator=shard_it2)
     #time.sleep(2.0)
     shard_it2 = out["NextShardIterator"]
     if out['Records'] != []:
         print(out)
     
     
