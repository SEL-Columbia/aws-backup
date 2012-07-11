from os import getenv
from boto.ec2.connection import EC2Connection

AWS_ACCESS_KEY_ID = '[YOUR ACCESS KEY ID]'
AWS_SECRET_ACCESS_KEY = '[YOUR AWS SECRET ACCESS KEY]'
EC2_VOLUME_ID = '[YOUR VOLUME ID]'

print 'Starting backup:\n\tAWS_ACCESS_KEY_ID: %s\n\tAWS_SECRET_ACCESS_KEY: %s' % \
    (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
conn = EC2Connection(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
print 'Connection established... Creating snapshot for volume: %s' % EC2_VOLUME_ID
created = conn.create_snapshot(EC2_VOLUME_ID)
if created:
    print 'Snapshot created.'
else:
    print 'Snapshot creation failed'
print 'Trimming old snapshots.'
conn.trim_snapshots()
print 'Fin.'
