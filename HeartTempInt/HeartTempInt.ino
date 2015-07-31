#include <Wire.h>
#include <Adafruit_MLX90614.h>

Adafruit_MLX90614 mlx = Adafruit_MLX90614();

int pulsePin = 14;
int blinkPin; //sudo
int pa = 0;

volatile int BPM;
volatile int Signal;
volatile int IBI = 600;
volatile boolean Pulse = false;
volatile boolean QS = false;

float counter = 0;
float average = 0;
float tempArray[10];


void(* resetFunc) (void) = 0;

void setup(){
  Serial.begin(115200);
  mlx.begin();
  interruptSetup();
}

void loop(){
  if(QS==true){
    pa = BPM;
    QS = false;
  }
  else
  {
   
  }
  
  for(int i=0 ; i <= 10; i++){
    tempArray[i] = mlx.readObjectTempC();
    delay(10);
  }
   
   for(int i=0; i < 10; i++)
    {
      average = (average + tempArray[i]);
    }
    average = average/10; 
    
  if(average > 35 && average < 42){
    counter = average;
  }
  else
  {
    
  }
  
  while(BPM > 50 && BPM < 140 && average > 35 && average < 42){
  Serial.print(pa);
  Serial.print(',');
  Serial.println(counter);
  
  if(QS == true){
    pa = BPM;
    QS = false;
  }
  
  temperatureA();
  
}
 
}

/*
void heartRate(){
 if (QS == true){
 return BPM;
 QS = false;
 }
 }
 
 */
 
 void temperatureA(){
     for(int i=0 ; i <= 10; i++){
    tempArray[i] = mlx.readObjectTempC();
    delay(10);
  }
   
   for(int i=0; i < 10; i++)
    {
      average = (average + tempArray[i]);
    }
    average = average/10; 
 }


