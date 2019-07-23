void setup() {
	Serial.begin(9600);
	Serial.println("setup completed!");
}

void loop() {
	Serial.print("We are ");
	Serial.println(" looping now!");

	delay(100);
}
