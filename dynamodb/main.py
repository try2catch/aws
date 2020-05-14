import sys

import boto3
from botocore.exceptions import ClientError

db = boto3.resource('dynamodb')
table = db.Table('<Table Name>')
row = {'country': 'Haryana', 'active_cases': 10}

try:
    response = table.put_item(Item=row, ConditionExpression='attribute_not_exists(country)')
    print('Data insert successfully.')
except ClientError as e:
    if e.response['Error']['Code'] == 'ConditionalCheckFailedException':
        print('Duplicate Data')
    else:
        print(e)
        sys.exit(1)
except Exception as e:
    print(e)
    sys.exit(1)
