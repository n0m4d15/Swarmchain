/*
   This firmware is titled nodeFirmwareV0.1 for the Swarmchain prototype
   Written By: N0M4D15
   Date: 02nd November 2021
*/

#include <ESP8266WiFi.h>
WiFiClient client;
WiFiServer server(80);

const char* ssid = "YOUR SSID";
const char* password = "YOUR PASSWORD";

String  data = "";

int LMF = 2;     // GPIO2(D4) -> IN3
int RMF = 15;   // GPIO15(D8) -> IN1
int LMB = 0;    // GPIO0(D3) -> IN4
int RMB = 13;  // GPIO13(D7) -> IN2
int RME = 14;       // GPIO14(D5) -> Motor-A Enable
int LME = 12;        // GPIO12(D6) -> Motor-B Enable

void setup()
{
  pinMode(LMF, OUTPUT);
  pinMode(RMF, OUTPUT);
  pinMode(LMB, OUTPUT);
  pinMode(RMB, OUTPUT);
  pinMode(LME, OUTPUT);
  pinMode(RME, OUTPUT);
  server.begin();
}

void loop()
{
  client = server.available();
  if (!client) return;
  data = checkClient ();

  if (data == "fwd") MotorForward();
  else if (data == "bwd") MotorBackward();
  else if (data == "lft") TurnLeft();
  else if (data == "rgt") TurnRight();
  else if (data == "stp") MotorStop();
}

String checkClient (void)
{
  while (!client.available()) delay(1);
  String request = client.readStringUntil('\r');
  request.remove(0, 5);
  request.remove(request.length() - 9, 9);
  return request;
}

void MotorForward(void)
{
  digitalWrite(LME, HIGH);
  digitalWrite(RME, HIGH);
  digitalWrite(LMF, HIGH);
  digitalWrite(RMF, HIGH);
  digitalWrite(LMB, LOW);
  digitalWrite(RMB, LOW);
}

void MotorBackward(void)
{
  digitalWrite(LME, HIGH);
  digitalWrite(RME, HIGH);
  digitalWrite(LMB, HIGH);
  digitalWrite(RMB, HIGH);
  digitalWrite(LMF, LOW);
  digitalWrite(RMF, LOW);
}

void TurnLeft(void)
{
  digitalWrite(LME, HIGH);
  digitalWrite(RME, HIGH);
  digitalWrite(LMF, LOW);
  digitalWrite(RMF, HIGH);
  digitalWrite(RMB, LOW);
  digitalWrite(LMB, HIGH);
}

void TurnRight(void)
{
  digitalWrite(LME, HIGH);
  digitalWrite(RME, HIGH);
  digitalWrite(LMF, HIGH);
  digitalWrite(RMF, LOW);
  digitalWrite(RMB, HIGH);
  digitalWrite(LMB, LOW);
}

void MotorStop(void)
{
  digitalWrite(LME, LOW);
  digitalWrite(RME, LOW);
  digitalWrite(LMF, LOW);
  digitalWrite(LMB, LOW);
  digitalWrite(RMF, LOW);
  digitalWrite(RMB, LOW);
}
