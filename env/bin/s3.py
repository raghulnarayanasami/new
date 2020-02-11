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
    s3.Object(w,'apache1.conf').upload_file(Filename='apache.conf')

    print (' \n\n\n The new bucket created :', w)
#For Python3
x = input('Enter your access key:')
y = input('Enter your secret key:')
z = input('Enter your existing  bucket name to list contents:')
w = input ('Enter a new bucket name to get created:')
boto3connection(x,y,z,w)

