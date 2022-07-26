#include <ThingSpeak.h>
#include <DHT.h>

#define channel=
DHT dht(12, DHT11);
void setup() {
  // put your setup code here, to run once:
dht.begin();
Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
float temp=dht.readTemperature();
float hum=dht.readHumidity();
if(isnan(temp)||isnan(hum)){
  return;
}
Serial.print("#");
Serial.print(",");
Serial.print(hum);
Serial.print(",");
Serial.print(temp);
Serial.print(",");
Serial.println("~");
}
