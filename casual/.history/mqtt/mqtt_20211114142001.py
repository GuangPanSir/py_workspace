import paho.mqtt.client as mqtt

BrokerHost = '183.230.40.39'  # OneNET使用TCP方式连接时的主机地址
BrokerPort = 6002  # OneNET使用TCP方式连接时的主机端口号

DeviceId = '854474207'  # 设备ID
ProductId = '469019'  # 产品ID
APIKey = "VKVzokuBOIpKimqfdL710PsUKxk="  # 可以是设备单独的APIKey，也可以是产品的MasterAPIKey


# 连接结果
def on_connect(client, userdata, flags, rc):
    if rc != 0:
        print("连接失败:" + mqtt.connack_string(rc))
        return
    print("连接成功")


# 从服务器接收发布消息时的回调
def on_message(client, userdata, msg):
    print("***** 接收到消息 *****")
    print(msg.topic + ":" + msg.payload.decode("utf-8"))


# 当broker响应订阅请求时被调用
def on_subscribe(client, userdata, mid, granted_qos):
    client.subscribe("/mysmartHome/pub", 2)


# 消息发送回调
def on_publish(client, userdata, mid):
    print("[on_publish] mid:" + str(mid))


def main():
    mqtt_broker_host = BrokerHost
    mqtt_broker_port = BrokerPort
    mqtt_user_name = ProductId
    mqtt_password = APIKey
    mqtt_client_id = DeviceId
    client = mqtt.Client(client_id=mqtt_client_id, protocol=mqtt.MQTTv311)
    client.on_connect = on_connect
    print("1")
    client.on_publish = on_publish
    print("2")
    client.on_subscribe = on_subscribe
    print("3")
    client.on_message = on_message
    print("4")
    client.username_pw_set(username=mqtt_user_name, password=mqtt_password)
    client.connect(host=mqtt_broker_host,
                    port=mqtt_broker_port,
                    keepalive=60)
    client.loop_forever()


if __name__ == "__main__":
    main()
