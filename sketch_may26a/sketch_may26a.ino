#include <WiFi.h>
#include "esp_wifi.h"

const uint16_t port = 4042;
const char * host;

const char* ssid     = "ESP32-Access-Point";
const char* password = "123456789";

int top_light = 27;
int bottom_light = 14;
int sensor1 = 4;
//byte sensor2 = 4;
//byte sensor3 = 5;

boolean height_flag = false;
boolean clockwise = false;
boolean anticlockwise = false;

int num = 0;
int checker;
unsigned long j = 0;
unsigned long k = 0;
int seconds;

int driverPUL = 21;    // PUL- pin
int driverDIR = 19;    // DIR- pin

WiFiClient client;

void setup(){

    pinMode(driverPUL, OUTPUT);
    pinMode(driverDIR, OUTPUT);
    pinMode(top_light, OUTPUT);
    pinMode(bottom_light, OUTPUT);
//    pinMode(sensor1, INPUT);
//    pinMode(sensor2, INPUT);
//    pinMode(sensor3, INPUT);
   
    digitalWrite(driverDIR,HIGH);
    digitalWrite(driverPUL,HIGH);
    digitalWrite(top_light, HIGH);
    digitalWrite(bottom_light, HIGH);
   
    Serial.begin(115200);


    Serial.println("Setting AP (Access Point)…");
    WiFi.softAP(ssid, password);
    Serial.print("Waiting for Connections...");

    while(1){
       
      while(!(client.connected())){
       connection();
      }
      while((client.connected())){
       heigth_listener();
      }

   }  
   
}

void connection() {

  while(1){
   
    wifi_sta_list_t wifi_sta_list;
    tcpip_adapter_sta_list_t adapter_sta_list;
   
    memset(&wifi_sta_list, 0, sizeof(wifi_sta_list));
    memset(&adapter_sta_list, 0, sizeof(adapter_sta_list));
   
    esp_wifi_ap_get_sta_list(&wifi_sta_list);
    tcpip_adapter_get_sta_list(&wifi_sta_list, &adapter_sta_list);
   
    for (int i = 0; i < adapter_sta_list.num; i++) {
   
      tcpip_adapter_sta_info_t station = adapter_sta_list.sta[i];
   
      Serial.print("\nIP: ");  
      Serial.println(ip4addr_ntoa(&(station.ip)));
      host = ip4addr_ntoa(&(station.ip));
      if (client.connect(host, port)) {
       return;
      }    
    }
   
    Serial.println("-----------");
    delay(500);
   
  }
}

void heigth_listener(){
     
  while(1){

       k++;
       Serial.println(k);
       
     checker = client.write(1);
     if(checker == 0){
      connection();
     }
//        Serial.println("loop1");
    while(client.available() > 0){
      String line = client.readStringUntil('\r');
      Serial.println(line);
     if(line == "-3"){
      anticlockwise = true;
     }
     else if(line == "-2"){      
      clockwise = true;
     }
     else if(line == "-1"){
      clockwise = false;
      anticlockwise = false;
     }
     else if(line == "0"){
      height_flag = false;
      Serial.println(height_flag);
      timer_listener();
     }
     else if(line == "5"){
      height_flag = true;
      Serial.println(height_flag);
      timer_listener();
     }
     
    }
    if(clockwise == true){
      digitalWrite(driverDIR,LOW);
      delayMicroseconds(2.5);
      digitalWrite(driverPUL,HIGH);
      delayMicroseconds(300);
      digitalWrite(driverPUL,LOW);
      delayMicroseconds(300);
    }
    else{
     digitalWrite(driverPUL, LOW);
    }
    if(anticlockwise == true){
     digitalWrite(driverDIR,HIGH);
     delayMicroseconds(2.5);
     digitalWrite(driverPUL,HIGH);
     delayMicroseconds(300);
     digitalWrite(driverPUL,LOW);
     delayMicroseconds(300);
    }
    else{
     digitalWrite(driverPUL, LOW);
      }

    }  
   
  }
   


void timer_listener(){
 
  while(1){
       
       j++;
//       Serial.println(j);
       delay(10);
       if(j == 68500){
        j = 0;
        heigth_listener();
       }
       
       while (client.available() > 0){
        num *= 10;
        num += (client.read() - '0');
        delay(10);    
         }
       if((num == 1)||(num == 2)||(num == 3)||(num == 4)||(num == 5)||(num == 6)||(num == 7)||(num == 8)||(num == 9)||(num == 10)||(num == 15)||(num == 20)||(num == 25)||(num == 30)||(num == 35)||(num == 40)||(num == 45)||(num == 50)||(num == 55)||(num == 60)){
        j = 0;
        Serial.print("next int type num = ");
        Serial.println(num);
        seconds = (240 * num);
        Serial.println(seconds);
        time_loop(seconds);
         }
       else if((num == 65)){
        j = 0;
        Serial.println(num);
        num = 0;
        heigth_listener();  
         }
   
      }
 
   }


void time_loop(int count){
 
    Serial.println(count);

 for(int a = count-1; a >= 0; a--){
//   Serial.println("loop3");
   Serial.println(a/4);
  if(height_flag == true){
     digitalWrite(top_light, LOW);
     digitalWrite(bottom_light, LOW);
    }
   else{
     digitalWrite(bottom_light, LOW);
    }
  delay(250);
 
   int val = digitalRead(sensor1);

        if(val  == HIGH) {
         client.write("1");
         digitalWrite(top_light, HIGH);
         digitalWrite(bottom_light, HIGH);
         Serial.println("motion...!!");
         num = 0;
         heigth_listener();
      }
 
    while((client.available() > 0)) {
     
     String line = client.readStringUntil('\r');
      Serial.println(line);
      if(line == "s"){
       digitalWrite(top_light, HIGH);
       digitalWrite(bottom_light, HIGH);
       num = 0;
       heigth_listener();
      }
      if(line == "h"){
       digitalWrite(top_light, HIGH);
       digitalWrite(bottom_light, HIGH);
       num = 0;
       int sub = a;
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
   if(line == "p"){
       time_loop(loop_count);
        }
   if(line == "s"){
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
