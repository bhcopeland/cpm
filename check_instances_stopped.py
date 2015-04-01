import sys
import datetime
from boto import ec2

region='us-east-1'
access_key=''
secret_key=''

if __name__ == '__main__':


    try:
        conn = ec2.connect_to_region (region, 
                                      aws_access_key_id=access_key, 
                                      aws_secret_access_key=secret_key)
        reserves = conn.get_all_instances (instance_ids=sys.argv[1:])
    except Exception, e:
        sys.stderr.write ('Could not connect to region: %s. Exception: %s\n' % (region, e))
        sys.exit (-1)

    stopped = False
    for reserve in reserves:
        for instance in reserve.instances:
            if instance.state in [u'stopped', u'stopping', u'shutting-down']:
                sys.stderr.write ('Instance %s is in status %s\n' % (instance.id, instance.state))
                stopped = True



    if stopped:
        sys.exit (1)
    else:
        sys.exit (0)
                

