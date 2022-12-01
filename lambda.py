import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    hash_key=event['path'][1:]
    response_flag = 0
    s3_connect=boto3.client("s3")
    
    response=s3_connect.select_object_content(
        Bucket='hashes-and-plaintext',
        Key='hash_table.csv',
        ExpressionType='SQL',
        Expression=f"Select * From s3object s where s.hash='{hash_key}'",
        InputSerialization={'CSV': {"FileHeaderInfo": "Use"}, 'CompressionType': 'NONE'},
        OutputSerialization={'CSV': {}},
        )
    
    for event in response['Payload']:
        if 'Records' in event:
            records = event['Records']['Payload'].decode('utf-8')
            response_flag = 1
        elif 'Stats' in event:
            statsDetails = event['Stats']['Details']
            print("Stats details bytesScanned: ")
            print(statsDetails['BytesScanned'])
            print("Stats details bytesProcessed: ")
            print(statsDetails['BytesProcessed'])
            print("Stats details bytesReturned: ")
            print(statsDetails['BytesReturned'])
    #print(event['path'][1:])
    if response_flag == 1:
        passwords = records.split(',')
        password=passwords[1].rstrip()
        print(password)
        return{'statusCode': 200, "body": json.dumps({hash_key:password})}
    else:
        return {'statusCode': 404, 'body':''}
    
        