int lowestPin = A3;
int lowerPin = A4;
int higherPin = A5;
int highestPin = A6;
int potPin = A1;
int ledPin = A2;
//Low values when light detected, high values when light not detected 
void setup() {
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
}
 
void loop() {
  int potValue = analogRead(potPin);
  int lowestValue = analogRead(lowestPin) > 512; //remember to flip these back
  int lowerValue = analogRead(lowerPin) > 512;
  int higherValue = analogRead(higherPin) > 512;
  int highestValue = analogRead(highestPin) > 512;
  if (potValue < 300) {
    Serial.println((1<<4) | (lowestValue<<3) | (lowerValue<<2) | (higherValue<<1) | (highestValue));
  }
  if (potValue > 300 && potValue < 700) {
    Serial.println((1<<5) | (lowestValue<<3) | (lowerValue<<2) | (higherValue<<1) | (highestValue));
  }
  if (potValue > 700 && potValue < 900) {
    Serial.println((1<<6) | (lowestValue<<3) | (lowerValue<<2) | (higherValue<<1) | (highestValue));
  }
  if (potValue > 900) {
    Serial.println((1<<7) | (lowestValue<<3) | (lowerValue<<2) | (higherValue<<1) | (highestValue));
  }
  analogWrite(ledPin, 0);
}
