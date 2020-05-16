#include <WiFi.h>

const uint16_t port = 4042;
const char * host = "192.168.4.2";

const char* ssid     = "ESP32-Access-Point";
const char* password = "123456789";

int clockwise_motor = 15;
int anticlockwise_motor = 4;
int top_light = 5;
int bottom_light = 19;
int sensor1 = 12;
int sensor2 = 27;
int sensor3 = 25;

boolean height_flag = false;
boolean clockwise = false;
boolean anticlockwise = false;

int num = 0;

WiFiClient client;

void setup(){

    pinMode(clockwise_motor, OUTPUT);
    pinMode(anticlockwise_motor, OUTPUT);
    pinMode(top_light, OUTPUT);
    pinMode(bottom_light, OUTPUT);
    digitalWrite(clockwise_motor, HIGH);
    digitalWrite(anticlockwise_motor, HIGH);
    digitalWrite(top_light, HIGH);
    digitalWrite(bottom_light, HIGH);
    Serial.begin(115200);
    delay(10);

    Serial.println("Setting AP (Access Point)…");
    WiFi.softAP(ssid, password);
    Serial.print("Waiting for Connections...");

    while(1){
      if (!client.connect(host, port)) {
        Serial.print(".");
      }
      else{
        Serial.println("Connected to hotspot");
        if(client.Connected())
            heigth_listener();
        else
            print("Connection Lost");
      }

   }  
   
}

void heigth_listener(){

  while(1){
    while(client.available() > 0){
      String line = client.readStringUntil('\r');
      Serial.println(line);
 
     if(line == "-3"){
      clockwise = true;
     }
     else if(line == "-2"){
      anticlockwise = true;
     }
     else if(line == "-1"){
      clockwise = false;
      anticlockwise = false;
     }
     else if(line == "0"){
      height_flag = false;
      timer_listener();
     }
     else{
      height_flag = true;
      timer_listener();
     }
     
    }
    if(clockwise == true){
     digitalWrite(clockwise_motor, LOW);
    }
    else{
     digitalWrite(clockwise_motor, HIGH);
    }
    if(anticlockwise == true){
     digitalWrite(anticlockwise_motor, LOW);
    }
    else{
     digitalWrite(anticlockwise_motor, HIGH);
      }

    }  
   
  }
   


void timer_listener(){
 
  while(1){        
       while (client.available() > 0){
        num *= 10;
        num += (client.read() - '0');
        delay(10);    
         }
       if((num == 1)||(num == 2)||(num == 3)||(num == 4)||(num == 5)||(num == 6)||(num == 7)||(num == 8)||(num == 9)||(num == 10)||(num == 15)||(num == 20)||(num == 25)||(num == 30)||(num == 35)||(num == 40)||(num == 45)||(num == 50)||(num == 55)||(num == 60)){
        Serial.println(num);
        int sec = 60*num;
        time_loop(sec);
         }
       else if((num == 65)){
        Serial.println(num);
        num = 0;
        heigth_listener();  
         }
   
      }
 
   }


void time_loop(int count){
 
//    Serial.println(count);
   
 for(int a = 0; a < count; a++){
//   Serial.println("loop3");
//   Serial.println(a);
  if(height_flag == true){
     digitalWrite(top_light, LOW);
     digitalWrite(bottom_light, LOW);
    }
   else{
     digitalWrite(bottom_light, LOW);
    }
  delay(1000);
  int val = digitalRead(sensor1);
 
    while((client.available() > 0) || val == HIGH) {
     
     String line = client.readStringUntil('\r');
      Serial.println(line);
      if(line == "stop"){
       digitalWrite(top_light, HIGH);
       digitalWrite(bottom_light, HIGH);
       num = 0;
       heigth_listener();
      }
      if(val == HIGH){
       client.write("1");
       digitalWrite(top_light, HIGH);
       digitalWrite(bottom_light, HIGH);
       Serial.println("motion...!!");
       num = 0;
       heigth_listener();
      }
      if(line == "hault"){
       digitalWrite(top_light, HIGH);
       digitalWrite(bottom_light, HIGH);
       num = 0;
       int sub = (count - a -2);
       Serial.println(sub);
       halt_loop(sub);
      }
           
    }
     
  }
 
  num = 0;
  digitalWrite(top_light, HIGH);
  digitalWrite(bottom_light, HIGH);
  heigth_listener();
   
}

void halt_loop(int loop_count){

 while(1){

  while(client.available() > 0) {

     String line = client.readStringUntil('\r');
     Serial.println(line);
   if(line == "play"){
       time_loop(loop_count);
        }
   if(line == "stop"){
       digitalWrite(top_light, HIGH);
       digitalWrite(bottom_light, HIGH);
       num = 0;
       heigth_listener();
        }    
     
      }
   
    }
 
  }



void loop(){

}