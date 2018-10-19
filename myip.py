#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import sys
from urllib.request import urlopen
import paho.mqtt.publish as publish

urls = [
    'https://icanhazip.com'
    , 'http://smart-ip.net/myip'
    , 'http://ip.42.pl/raw'
]

def main():
    connOK = True
    while (connOK):
        try:
            url = urls[0]
            ip = urlopen(url, timeout=3).read().decode('utf-8')
            print("{}: {}".format(url, ip))
            # publish.single(topic="{}{}".format(prefix, msg.topic)
            #                , payload=msg.payload
            #                , qos=msg.qos
            #                , retain=msg.retain
            #                , hostname=cfg["consumer"]["mqtt"]["hostname"]
            #                , port=cfg["consumer"]["mqtt"]["port"]
            #                , client_id=cfg["consumer"]["mqtt"]["client_id"]
            #                , keepalive=7
            #                )
            #myIp = re.compile('(\d{1,3}\.){3}\d{1,3}').search(res.text).group()
            #if myIp != "":
            #   print(myIp)
            time.sleep(10)
        except:
            type, value, traceback = sys.exc_info()
            print("Exception: {}".format(value))
            time.sleep(1)


if __name__ == '__main__':
    try:
        print('-----------------------------------------------')
        main()
    except (SystemExit, KeyboardInterrupt):
        print('-----------------------------------------------')
    except:
        type, value, traceback = sys.exc_info()
        print("Exception: {}".format(value))
