int LED_SET_1 = 13; 
int LED_SET_2 = 12;
int LED_SET_3 = 11;
int LED_SET_4 = 10;
//numbers at the end are the outpins

void setup() {
  //tell what our pinvar is doing physically
pinMode(LED_SET_1, OUTPUT);
pinMode(LED_SET_2, OUTPUT);
pinMode(LED_SET_3, OUTPUT);
pinMode(LED_SET_4, OUTPUT);
}

void loop() {
  //high is on low is off
  //delay is in ms
digitalWrite(LED_SET_1, HIGH);
delay(60);
digitalWrite(LED_SET_1, LOW);
digitalWrite(LED_SET_2, HIGH);
delay(100);
digitalWrite(LED_SET_3, HIGH);
delay(150);
digitalWrite(LED_SET_2, LOW);
digitalWrite(LED_SET_4, HIGH);
delay(50);
digitalWrite(LED_SET_2, LOW);
digitalWrite(LED_SET_3, LOW);
delay(70);
digitalWrite(LED_SET_4, LOW);
delay(10);
}
