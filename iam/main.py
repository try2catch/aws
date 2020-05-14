import boto3

client = boto3.client('iam')
access_keys = client.list_access_keys().get('AccessKeyMetadata')

final_dict = {}
for keys in access_keys:
    key = keys.get('AccessKeyId')
    response = client.get_access_key_last_used(
        AccessKeyId=key
    )
    final_dict.update({"key": key, "LastUsed": response['AccessKeyLastUsed']['LastUsedDate']})
    print(final_dict)
