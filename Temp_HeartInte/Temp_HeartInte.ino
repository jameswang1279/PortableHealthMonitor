#include <Wire.h>
#include <Adafruit_MLX90614.h>

int pulsePin = 14;                 // Pulse Sensor purple wire connected to analog pin 0
int blinkPin = 7;               // pin to blink led at each beat

int fadePin = 5;                  // sudo code
int fadeRate = 0;                 // sudo code
int b = 0;


// these variables are volatile because they are used during the interrupt service routine!
volatile int BPM;                   // used to hold the pulse rate
volatile int Signal;                // holds the incoming raw data
volatile int IBI = 600;             // holds the time between beats, the Inter-Beat Interval
volatile boolean Pulse = false;     // true when pulse wave is high, false when it's low
volatile boolean QS = false;        // becomes true when Arduoino finds a beat.
int lightPin = 1;  //define a pin for Photo resistor
int a = 0; //a references the light value detected by the photoresistor
int initi[10];
int counter = 0;

float average = 0;
float tempArray[30];
Adafruit_MLX90614 mlx = Adafruit_MLX90614();

void(* resetFunc) (void) = 0; //used for reset 

void setup(){

  pinMode(blinkPin,OUTPUT);         // pin that will blink to your heartbeat!
  pinMode(fadePin,OUTPUT);          // pin that will fade to your heartbeat!
  Serial.begin(115200);             // we agree to talk fast!
  interruptSetup();                 // sets up to read Pulse Sensor signal every 2mS
  mlx.begin();  
}



void loop(){
  
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
  }
  else
  {
    //LEAVE EMPTY
  }


    
  if (QS == true){                       // Quantified Self flag is true when arduino finds a heartbeat
        fadeRate = 255;                  // Set 'fadeRate' Variable to 255 to fade LED with pulse
b = BPM;
     }
 
  ledFadeToBeat();
 
  delay(20);                             //  take a break
  
  Serial.print(average);
  Serial.print(',');
  Serial.println(b);
}








void ledFadeToBeat(){
    fadeRate -= 10;                         //  set LED fade value
    fadeRate = constrain(fadeRate,0,255);   //  keep LED fade value from going into negative numbers!
    analogWrite(fadePin,fadeRate);          //  fade LED
  }


void sendDataToProcessing(char symbol, int data ){
    //Serial.print(symbol);                // symbol prefix tells Processing what type of data is coming
   // Serial.println(data);                // the data to send culminating in a carriage return
  }
