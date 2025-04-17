import boto3
from botocore.exceptions import BotoCoreError, ClientError
from django.conf import settings


def generate_presigned_url(bucket_name, key, expiration=3600):
    try:
        s3_client = boto3.client(
            "s3",
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            region_name=settings.AWS_REGION,
        )

        return s3_client.generate_presigned_url(
            "get_object",
            Params={"Bucket": bucket_name, "Key": key},
            ExpiresIn=expiration,
        )
    except (BotoCoreError, ClientError) as e:
        print(f"Error generating presigned URL: {e}")
        return None
