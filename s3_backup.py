import boto3

def boto3connection(access_key,secret_key,bucketname):
    print ('----------------------------------------------')
    host='https://aos.tcsecp.com'
    s3=boto3.resource('s3',aws_access_key_id=access_key,aws_secret_access_key=secret_key, endpoint_url=host,)
    buckets = s3.Bucket(bucketname)

    for i in buckets.objects.all():
        print(i)
    bucket_list = s3.buckets.all()
    for j in bucket_list:
        print(j.name)
 
x = '47cd575d659d468aa5aa3f7a4cfa8a89'
y = 'a87b5287abb7484683e81f78c1c2cbf9'
z = 'anew3'
#w = input ('Enter a new bucket name to get created:')
boto3connection(x,y,z)
