import fbconsole

fbconsole.AUTH_SCOPE = ['publish_stream', 'publish_checkins']
fbconsole.authenticate()

import os

for dirname, dirnames, filenames in os.walk('./pics/'):
   # print path to all filenames.
    for filename in filenames:
        picname = os.path.join(dirname, filename)
        print picname
        response = fbconsole.post('/me/photos', {'source':open(picname)})
        print response
        picid = response['id']
        tag = fbconsole.post('/'+picid+'/tags', {'to':'USER-ID-HERE', 'x':'0', 'y':'0'})
