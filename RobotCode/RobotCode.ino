#include <RedBot.h>

RedBotMotors motors;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()) {
    String str = Serial.readString();
    int hold = str.toInt();
    switch(hold){
      case -1:
        motors.leftMotor(60);
        motors.rightMotor(60);
        delay(1000);
        motors.brake();
        break;
      case 1:
        motors.leftMotor(-60);
        motors.rightMotor(-60);
        delay(1000);
        motors.brake();
        break;
      default:
        motors.brake();
        break;
    }
  }
}
