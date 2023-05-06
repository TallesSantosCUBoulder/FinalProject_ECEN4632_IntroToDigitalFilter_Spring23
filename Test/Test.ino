void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.println("Hello World");
}

int angle = 0;
unsigned long curr = millis();
unsigned long last = 0;
unsigned long timeDelay = 100;

void loop() {
  // put your main code here, to run repeatedly:
  if( (curr - last) >= timeDelay ){
    last = millis();
    Serial.println(sin(angle * M_PI / 180));
    angle++;
  }
  curr = millis();
}