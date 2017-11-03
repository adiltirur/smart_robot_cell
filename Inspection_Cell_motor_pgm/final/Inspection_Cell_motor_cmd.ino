int pul = 50;
int steps = 5;
int angle;
int rotate = 0;
void setup()
{

  pinMode(pul, OUTPUT);
  Serial.begin(9600);
  Serial.println("Start!");

}
void loop()
{

  if (Serial.available() > 0)
  {

    angle = Serial.parseInt();
    rotate = angle * steps;
    for (int i = 0; i <= rotate; i++)
    {
      digitalWrite(pul, HIGH);
      digitalWrite(13, HIGH);
      delay(1);
      digitalWrite(13, LOW);
      digitalWrite(pul, LOW);
      delay(1);
    }
  }

}

