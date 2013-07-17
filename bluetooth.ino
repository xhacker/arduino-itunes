#define PIN_LED 13
#define PIN_BUTTON_PREV 8
#define PIN_BUTTON_PLAY 9
#define PIN_BUTTON_NEXT 10
#define PIN_SPIN_VOLUME 2

#define BTN_PRESS_DELAY 300

void setup()
{
    Serial.begin(9600);
    pinMode(PIN_LED, OUTPUT);
    pinMode(PIN_BUTTON_PREV, INPUT);
    pinMode(PIN_BUTTON_PLAY, INPUT);
    pinMode(PIN_BUTTON_NEXT, INPUT);
}

int prevVolume = 0;

int changed(int current, int prev)
{
    int delta = abs(current - prev);
    if (prev > 80)
    {
        return delta > 2;
    }
    else if (prev > 50)
    {
        return delta > 5;
    }
    else if (prev > 30)
    {
        return delta > 7;
    }
    else
    {
        return delta > 10;
    }
}

void loop()
{
    int prevState = digitalRead(PIN_BUTTON_PREV);
    int playState = digitalRead(PIN_BUTTON_PLAY);
    int nextState = digitalRead(PIN_BUTTON_NEXT);

    if (prevState == HIGH)
    {     
        Serial.println("PREV");
        digitalWrite(PIN_LED, HIGH);
        delay(BTN_PRESS_DELAY);
    }
    else if (playState == HIGH)
    {     
        Serial.println("PLAY");
        digitalWrite(PIN_LED, HIGH);
        delay(BTN_PRESS_DELAY);
    }
    else if (nextState == HIGH)
    {     
        Serial.println("NEXT");
        digitalWrite(PIN_LED, HIGH);
        delay(BTN_PRESS_DELAY);
    }
    else
    {
        digitalWrite(PIN_LED, LOW);
    }

    int curVolume = map(analogRead(PIN_SPIN_VOLUME), 0, 1023, 0, 100);
    if (changed(curVolume, prevVolume))
    {
        prevVolume = curVolume;
        Serial.println(curVolume);
    }

    // Serial.println("BT is good.");
    char val = Serial.read();
    if (val == '@')
    {
        digitalWrite(PIN_LED, HIGH);
        delay(BTN_PRESS_DELAY);
        digitalWrite(PIN_LED, LOW);
        delay(BTN_PRESS_DELAY);
        Serial.println("Have you mooed today?");
    }
}
