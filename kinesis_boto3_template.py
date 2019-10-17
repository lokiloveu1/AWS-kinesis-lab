import boto3
import testdata
import json

#connect to your kinesis(must have configured aws account information before))
client = boto3.client('kinesis')

#describe your stream limit
describe_limits = client.describe_limits()

#list all your streams
list_streams = client.list_streams(
    Limit=123
)

#list all your shards in specify stream
list_shards = client.list_shards(
    StreamName='your-stream-name',
    MaxResults=123
)

#describe your specify stream
describe_stream = client.describe_stream(
    StreamName='your-stream-name',
    Limit=123,
    ExclusiveStartShardId='string'
)

# put single record into your stream
put_record1 = client.put_record(
    StreamName='your-stream-name',
    Data='my-data',
    PartitionKey='string'
    
)

#get your shard iterator
shard_iterator = client.get_shard_iterator(
    StreamName='your-stream-name',
    ShardId='shardId-000000000000',
    ShardIteratorType='LATEST'
)

#get your records from specify shard(must get your shard iterator first)
get_records = client.get_records(
    ShardIterator='AAAAAAAAAAHYE4bkRBjVB7T0RauYS0sGfvmHmzuCz1JsRtaY+hqglGKZybxYFvwYN+IOPYOFAmcR/+9i5Bq9bAys0Kpv0xDkpJtjgJQUcKm7mZn/Cr5KoMq20luF7s3u/moluLnpQAVqxBBSVDpETo9IgASFF3Fv7W9synVHC912RaNiOsd8ZMpLlXfu9OiG2IEC3+2viOEALA8DME06dzqLPHr+8kQJ5')

#print('get_records:',get_records)


