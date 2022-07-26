import time
import matplotlib.pyplot as plt
import serial
import urllib.request
import json
ard = serial.Serial("COM5", 9600)
hu, te = [], []
try:
    while True:
        if ard.inWaiting() > 0:
            data = list(ard.readline().decode('utf-8').split(','))
            humidity = data[1]
            temperature = data[2]
            api = "https://api.thingspeak.com/update?api_key=FO28QEWLOFYBS04G&"
            final = api + "field1=" + humidity + "&field2=" + temperature
            f = urllib.request.urlopen(final)
            print(f)
            time.sleep(5)
except KeyboardInterrupt as k:
    api = "https://api.thingspeak.com/channels/1812090/fields/1.json?api_key=QKL4W4BNA82UJ8U4&results=2"
    api1 = "https://api.thingspeak.com/channels/1812090/fields/1.json?api_key=QKL4W4BNA82UJ8U4&results="
    api2 = "https://api.thingspeak.com/channels/1812090/fields/2.json?api_key=QKL4W4BNA82UJ8U4&results="
    f = urllib.request.urlopen(api)
    data1 = json.loads(f.read().decode('utf-8'))
    feeds = data1["channel"]["last_entry_id"]
    f = urllib.request.urlopen(api1 + str(feeds))
    f_temp = urllib.request.urlopen(api2 + str(feeds))
    data1 = json.loads(f.read().decode('utf-8'))["feeds"]
    data2 = json.loads(f_temp.read().decode('utf-8'))["feeds"]
    for i in range(feeds):
        hu.append(data1[i]['field1'])
        te.append(data2[i]['field2'])
    x = [i+1 for i in range(feeds)]
    plt.subplot(1, 2, 1)
    plt.plot(x, te)
    plt.ylabel("temperature")
    plt.subplot(1, 2, 2)
    plt.plot(x, hu)
    plt.ylabel("humidity")
    plt.title("DHT11 readings")
    plt.show()