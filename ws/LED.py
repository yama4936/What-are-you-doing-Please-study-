import time
import requests
url2="http://192.168.4.1"
ON=1
OFF=0
for iter in range(1, 11):
    requests.get(url2 + "/control?var=GPIO2&val={}".format(ON))
    print("ON")
    time.sleep(3)
    requests.get(url2 + "/control?var=GPIO2&val={}".format(OFF))
    print("OFF")
    time.sleep(3)