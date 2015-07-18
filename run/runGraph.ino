#include <Wire.h>
#include <Adafruit_MLX90614.h>

int lightPin = 1;  //define a pin for Photo resistor
float a = 0; //a references the light value detected by the photoresistor

Adafruit_MLX90614 mlx = Adafruit_MLX90614();

void(* resetFunc) (void) = 0; //used for reset 

void setup()
{
  Serial.begin(9600); 
  mlx.begin();  
//  interruptSetup(); 
}



void loop()
{
  a = mlx.readObjectTempC();
  if(a > 34 && a < 44){
    Serial.println(a);
  }
  else
  {
  }
  
    delay(50);
    


  resetFunc();
}








