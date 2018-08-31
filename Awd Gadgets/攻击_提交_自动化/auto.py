import os
import requests
f=open("./flags","r")

while(1):
    flag=f.readline()
    print flag
    if flag=="":
	break
    if len(flag)==61:
        flag=flag.strip('\n')
        cmd='''curl http://172.16.200.20:9000/submit_flag/ -d/ -d "flag={}&token=xkS9nxNNshMyRxT7T36naYaFRxWgJyryJKVyGyXb7TGT6yVc9BhvFMhY3DHrJV9hCUtmjMFsSHd"'''.format(flag)
        os.system(cmd)


