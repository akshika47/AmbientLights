#include <ESP8266WiFi.h>
#include <Adafruit_NeoPixel.h>


//SSID of your network
char ssid[] = ""; //SSID of your Wi-Fi router
char pass[] = ""; //Password of your Wi-Fi router
int delayval = 500; // delay for half a second

int LED = D5;
Adafruit_NeoPixel ring = Adafruit_NeoPixel(12, LED , NEO_GRB + NEO_KHZ800);

void setup()
{
  Serial.begin(115200);
  ring.begin();
  ring.setBrightness(30); //adjust brightness here
  ring.show(); //make the neo pixels show the configuration

  
/*
  //Uncomment the code snipet below to activate the wifi connection
  // Connect to Wi-Fi network
  Serial.println();
  Serial.println();
  Serial.print("Connecting to...");
  Serial.println(ssid);

  WiFi.begin(ssid, pass);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("Wi-Fi connected successfully");
*/
}


void loop () {  
  for(int i=0;i<12;i++){
    Serial.println("Inside the loop");
    // pixels.Color takes RGB values, from 0,0,0 up to 255,255,255
    ring.setPixelColor(i, ring.Color(0,150,0)); // Moderately bright green color.

    ring.show(); // This sends the updated pixel color to the hardware.

    delay(delayval); // Delay for a period of time (in milliseconds).

  }
  }

