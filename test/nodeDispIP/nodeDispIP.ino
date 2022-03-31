/*
 * This firmware is titled nodeDispIP and is written for the Swarmchain project.
 * Written By: N0M4D15
 * Date: 02nd November 2021
 */
#include <ESP8266WiFi.h>

WiFiClient client;
WiFiServer server(80);

const char* ssid = "YOUR SSID";
const char* password = "YOUR PASSWORD";

void setup()
{
  Serial.begin(115200);
  connectWiFi();
  server.begin();
}

void loop()
{
}

void connectWiFi()
{
  Serial.println("Connecting to WiFi");
  WiFi.begin(ssid, password);
  while ((!(WiFi.status() == WL_CONNECTED)))
  {
    delay(300);
    Serial.print("..");
  }
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("NodeMCU Bot Local IP is : ");
  Serial.print((WiFi.localIP()));
}
