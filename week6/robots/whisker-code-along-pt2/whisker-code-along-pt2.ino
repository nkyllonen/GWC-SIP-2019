// declare where we've plugged in the whiskers
int leftWhisker = 5;
int rightWhisker = 7;

void setup() {
  // put your setup code here, to run once:
  
  // opening up serial port for writing
  Serial.begin(9600);

  // declare digital pins as INPUT
  pinMode(leftWhisker, INPUT);
  pinMode(rightWhisker, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:

  // get information from whisker sensor
  int leftWhiskerValue = digitalRead(leftWhisker);
  int rightWhiskerValue = digitalRead(rightWhisker);

//  // output information
//  Serial.print("Left: ");
//  Serial.print(leftWhiskerValue);
//  Serial.print("  Right: ");
//  Serial.println(rightWhiskerValue);

  if (leftWhiskerValue == 0 && rightWhiskerValue == 0) {
    Serial.println("Left and Right pressed!");
  }
  else if (leftWhiskerValue == 0) {
    Serial.print("Left pressed!");
  }
  else if (rightWhiskerValue == 0) {
    Serial.print("Right pressed!");
  }
  else {
    Serial.print("No whiskers pressed!");
  }

  // remember to delay so that we don't overfill the buffer
  delay(100);
} 
