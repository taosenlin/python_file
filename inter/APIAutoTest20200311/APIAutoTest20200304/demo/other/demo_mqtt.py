import paho.mqtt.client as mqtt
import json
import time

HOST = "127.0.0.1" #服务器IP
PORT = 1883  #端口
client_id = "xxxxx"  # 没有就不写，此处部分内容用xxx代替原内容，下同


#消息
def on_message(client, userdata, msg):
    print("主题:"+msg.topic+" 消息:"+str(msg.payload.decode('utf-8')))

#订阅主题
def on_subscribe(client, userdata, mid, granted_qos):
    print("订阅qos = %d" % granted_qos)

#连接
def on_connect(client, userdata, flags, rc):
    print("连接状态码："+str(rc))
    client.subscribe("data/receive")         # 订阅消息

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("端口连接 %s" % rc)

data = {
    "type":2,
    "timestamp": time.time(),
    "messageId":"xxxx-xxxx-xxxx-xxxx",
    "command":"xx/recommend",
    "data":{
        "openId":"xxxx",
        "appId":"xxxx",
        "recommendType":"temRecommend"
    }
}
param = json.dumps(data)
client = mqtt.Client(client_id)
client.username_pw_set("xxxxxx", "xxxxxx")
client.on_connect = on_connect
client.on_message = on_message
client.on_subscribe = on_subscribe
client.on_disconnect = on_disconnect
client.connect(HOST, PORT, 60)
client.publish("data/send", payload=param, qos=0)     # 发送消息
client.loop_forever()
