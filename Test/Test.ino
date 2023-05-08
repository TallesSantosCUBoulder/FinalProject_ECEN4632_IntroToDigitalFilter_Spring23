void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

int angle = 0;
unsigned long curr = millis();
unsigned long last = 0;
unsigned long timeDelay = 3;

void loop() {
  // put your main code here, to run repeatedly:
  if( (curr - last) >= timeDelay ){
    last = millis();
    Serial.println(10 * sin(angle * M_PI / 180));
    angle++;
    if(angle >= 180)
      angle = 0;
  }
  curr = millis();
}