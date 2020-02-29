/*
 * mySE arduino simulation.
 * This code is purely simulated and may not work on an real Arduino.
 * This code requires the right arduino circuit to work.
 * This code is under an MIT license.
 * +-= Project URL =-+
 * https://arthurdw.github.io/mySE/
 * https://github.com/Arthurdw/mySE
 */

// #include <string>

// Our server url:
/* string local_url = "http://127.0.0.1:5000/",
       server_secret = "mySecureServerPassword",
       mail = "mail@mail.mail"; */

// Basic var declaration:
int pirInput = 2;
int ldrInput = 4;
int detectionIndicator = 7;
int pirState = LOW;

void setup()
{
  	Serial.begin(9600);
  	Serial.println("Setting up arduino.");
	pinMode(pirInput, INPUT);
	pinMode(ldrInput, INPUT);
	pinMode(detectionIndicator, OUTPUT);
  	Serial.println("Succesfully setup the arduino.");
  	/* Serial.println("Server info:");
  	Serial.println("Server URL: " + local_url);
  	Serial.println("Server secret: " + server_secret);
  	Serial.println("Running on the account synced with this email: " + mail); */
}

void loop()
{
  if (digitalRead(pirInput) == HIGH) {
    digitalWrite(detectionIndicator, HIGH);
    if (pirState == LOW) {
    	Serial.println("Motion detected.");
    	/* Serial.println("Creating a log...");
      	// Create a log to the server here.
        bool light = analogRead(ldrInput) > 700 ? true : false;
    	Serial.println("Sending a log request.");
      	// Send the log request here.
    	Serial.println("Created a log request."); */
      	pirState = HIGH;
    }
  } else {
    digitalWrite(detectionIndicator, LOW);
    if (pirState == HIGH){
    	Serial.println("Motion stopped.");
      	pirState = LOW;
    }
  }
  delay(10);
}