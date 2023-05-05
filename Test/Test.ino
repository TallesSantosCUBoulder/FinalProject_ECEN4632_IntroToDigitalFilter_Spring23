void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.println("Hello World");
}

int i = 0;
unsigned long curr = millis();
unsigned long last = 0;
unsigned long delay = 1000;
void loop() {
  // put your main code here, to run repeatedly:
  if( curr - last >= delay ){
    Serial.println(i);
    i++:
  }
}