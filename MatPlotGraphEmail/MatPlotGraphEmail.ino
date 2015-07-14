#include <Wire.h>
#include <Adafruit_MLX90614.h>

int lightPin = 1;  //define a pin for Photo resistor
int a = 0; //a references the light value detected by the photoresistor
int initi[10];
int counter = 0;

float average = 0;
int tempArray[30];
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
  a = analogRead(lightPin);   //determine initialization phase
  for(int i=0; i <= 10; i++){
    initi[i] = a ;
    delay(50);
    a = analogRead(lightPin);
  }

  if(initi[1] - initi[10] > 80){ //determine initialization

    //Serial.println("Device Initialized..."); UNCOMMENT FOR FINAL
    //Serial.println(" "); UNCOMMENT FOR FINAL
    //Serial.println("Measuring Temperature"); UNCOMMENT FOR FINAL

    for(int i=0; i <= 30; i++){
      tempArray[i] = mlx.readObjectTempC(); 
      delay(30);
    }


    delay(100);
    for(int i=0; i < 30; i++)
    {
      average = (average + tempArray[i]);
    }
    average = average/30; //Do exponential regression and error analysis

    Serial.println(average);
    delay(100); //data graphing


  }
  else
  {
    //LEAVE EMPTY
  }

  resetFunc();
}








