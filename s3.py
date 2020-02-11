import boto3

def boto3connection(access_key,secret_key,bucketname,w):
    print ('----------------------------------------------')
    host='https://aos.tcsecp.com'
    s3=boto3.resource('s3',aws_access_key_id=access_key,
aws_secret_access_key=secret_key, endpoint_url=host,)

    bucket=s3.Bucket(bucketname)
    print (' \n Contents of  ',bucketname)
    for obj in bucket.objects.filter():
        print('{0}:{1}'.format(bucket.name, obj.key))
    s3.create_bucket(Bucket=w)
    s3.Object(w,'apache1.conf').upload_file(Filename='/root/demoproject/runit.py')

    print (' \n\n\n The new bucket created :', w)
#For Python3
x = '47cd575d659d468aa5aa3f7a4cfa8a89'
y = 'a87b5287abb7484683e81f78c1c2cbf9'
z = 'anew3'
w = input ('Enter a new bucket name to get created:')
boto3connection(x,y,z,w)
