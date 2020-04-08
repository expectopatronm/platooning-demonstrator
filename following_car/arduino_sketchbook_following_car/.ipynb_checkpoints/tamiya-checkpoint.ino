#include <Adafruit_NeoPixel.h>
#include <LiquidCrystal_I2C.h>
#include <Servo.h>
#include <Speed.h>
#include <PID_v1.h>

#define NUMPIXELS 12

#define MEASURE_PIN_LEFT 8
#define MEASURE_PIN_RIGHT 13

#define NUMBER_MAGNETS_LEFT 8
#define NUMBER_MAGNETS_RIGHT 8

#define RADIUS_TYRE 0.042

#define LIGHTRING_PIN 7

#define EMA_WEIGHT 0.2

Servo steering_servo; 
Servo throttle_servo;
Servo pan_servo; 
Servo tilt_servo;

const byte numChars = 20;
char receivedChars[numChars];   
char tempChars[numChars];
boolean newData = false;

int steering_value = 0;
int throttle_value = 0;
int pan_value = 0;
int tilt_value = 0;
float speed_value = 0;

int zero_steering = 90;
int zero_throttle = 92;
int zero_pan = 90;
int zero_tilt = 20;

char buffer[20];
static char outstr[20];

LiquidCrystal_I2C lcd(0x27, 20, 4);

Adafruit_NeoPixel pixels = Adafruit_NeoPixel(NUMPIXELS, LIGHTRING_PIN, NEO_RGB + NEO_KHZ800);
Speed mySpeed(RADIUS_TYRE, MEASURE_PIN_LEFT, NUMBER_MAGNETS_LEFT, MEASURE_PIN_RIGHT, NUMBER_MAGNETS_RIGHT);

void receive_with_end_marker() {
    static byte ndx = 0;
    char endMarker = '*';
    char rc;
   
    if (Serial.available() > 0) {
        rc = Serial.read();

        if (rc != endMarker) {
            receivedChars[ndx] = rc;
            ndx++;
            if (ndx >= numChars) {
                ndx = numChars - 1;
            }
        }
        else {
            receivedChars[ndx] = '\0'; 
            ndx = 0;
            newData = true;
        }
    }
}

void execute_stuff() {
    if (newData == true) {
        
        strcpy(tempChars, receivedChars);
        
        char * strtokIndx;
 
        strtokIndx = strtok(tempChars, ",");
        steering_value = atoi(strtokIndx);    
        strtokIndx = strtok(NULL, ",");
        throttle_value = atoi(strtokIndx); 
        strtokIndx = strtok(NULL, ",");
        pan_value = atoi(strtokIndx); 
        strtokIndx = strtok(NULL, "*");
        tilt_value = atoi(strtokIndx); 
                               
        mySpeed.calcSpeed();
        speed_value = mySpeed._speed;
                    
        steering_servo.write(steering_value);
        throttle_servo.write(throttle_value);
        pan_servo.write(pan_value);
        tilt_servo.write(tilt_value);
        
        dtostrf(speed_value, 4, 2, outstr);    
        lcd.setCursor(0, 1);
        sprintf(buffer,"%s S:%3d T:%3d ", outstr, steering_value, throttle_value);
        lcd.print(buffer);

        newData = false;
    }
}

void setup() {
    Serial.begin(57600);
       
    lcd.init();
    lcd.backlight();
    lcd.print("Me, Jetson. You?"); 
    
    steering_servo.attach(9);
    throttle_servo.attach(10);
    pan_servo.attach(11);
    tilt_servo.attach(12);
    steering_servo.write(zero_steering);
    throttle_servo.write(zero_throttle);
    pan_servo.write(zero_pan);
    tilt_servo.write(zero_tilt);
        
    pixels.begin();
    for(int i = 0; i < NUMPIXELS; i++){
        pixels.setPixelColor(i, pixels.Color(255, 0, 255)); 
    }
    pixels.setBrightness(10);
    pixels.show();     
}

void loop() {
    receive_with_end_marker();
    execute_stuff();   
}



