import json

class ConfigHandler():
    def __init__(self):
        self.hostSerialNo = ""
        self.mqttBroker = ""
        self.mqttPort = 1883
        self.nfc = False
        self.nfcTopic = ""

    def read_json(self):
        with open('config.json') as json_data:
            data = json.load(json_data)
            self.hostSerialNo = data['HostSerialNo']
            self.mqttBroker = data['MQTT_broker']
            self.mqttPort = data['MQTT_port']
            self.nfc = data['NFC']
            self.nfcTopic = data['NFC_topic']

    def get_hostSerialNo(self):
        return self.hostSerialNo

    def get_mqttBroker(self):
        return self.mqttBroker

    def get_mqttPort(self):
        return self.mqttPort

    def get_nfc(self):
        return self.nfc

    def get_nfcTopic(self):
        return self.nfcTopic
