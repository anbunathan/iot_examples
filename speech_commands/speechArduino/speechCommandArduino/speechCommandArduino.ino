//Board used = Roboindia blink board

#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#include <DHT.h>

const char* ssid = "TP-Link_8700";
const char* password = "iotapp8266";

const char* mqtt_server = "digitran-mqtt.tk";

const char *mqtt_user = "snyhhyzw";
const char *mqtt_pass = "LpZK32PEBN5q";

//#include <dht.h>
// DHT11 Sensor Data Pin
#define DHTPIN    D5
#define DHTTYPE DHT11   // DHT 11
#define dht_apin D5

// Initialize DHT Sensor
DHT dht( DHTPIN, DHTTYPE);

//dht DHT;

WiFiClient espClient;
PubSubClient client(espClient);
long lastMsg = 0;
char msg[50];
int value = 0;

// Relay (Loads) Pin
#define RELAY1    D1
#define RELAY2    D2
#define RELAY3    D6
#define RELAY4    D4

void setup_wifi() {
  delay(100);
  // We start by connecting to a WiFi network
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  randomSeed(micros());

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");
  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }
  Serial.println();

  // Relay1 (Load1) Topic
  if ( strcmp(topic, "command") == 0 )
  {
    // Serial.println("Load1");
    //    if ((char)payload[0] == '1')
    String msgIN = "";
    for (int i = 0; i < length; i++)
    {
      msgIN += (char)payload[i];
    }
    String msgString = msgIN;
    Serial.println(msgString);
    
    if ( msgString == "go" )
    {
      digitalWrite( RELAY1, HIGH);
      Serial.print("command: ");
      Serial.println("go");
    }
    else if ( msgString == "stop")
    {
      digitalWrite( RELAY1, LOW);
      Serial.print("command: ");
      Serial.println("stop");
    }
  }
}

void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Create a random client ID
    String clientId = "ESP8266Client-";
    clientId += String(random(0xffff), HEX);
    // Attempt to connect
    //    if (client.connect(clientId.c_str(), mqtt_user, mqtt_pass)) {
    if (client.connect(clientId.c_str())) {
      Serial.println("connected");
      // Once connected, publish an announcement...
      client.publish("outTopic", "hello world");
      // ... and resubscribe
      //      client.subscribe("inTopic");
      client.subscribe("command");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}

void setup() {
  pinMode(BUILTIN_LED, OUTPUT);     // Initialize the BUILTIN_LED pin as an output
  // Initialize Relay's Pins as Output
  pinMode(RELAY1, OUTPUT );
  pinMode(RELAY2, OUTPUT );
  pinMode(RELAY3, OUTPUT );
  pinMode(RELAY4, OUTPUT );
  // Turn-Off all relays
  digitalWrite( RELAY1, LOW);
  digitalWrite( RELAY2, LOW);
  digitalWrite( RELAY3, LOW);
  digitalWrite( RELAY4, LOW);
  Serial.begin(115200);
  setup_wifi();
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);
  reconnect();
}

void loop() {

  if (!client.connected()) {
    reconnect();
  }

  client.loop();

  //  DHT.read11(dht_apin);
  //  int h = DHT.humidity;
  //  int t = DHT.temperature;
  // Read Humidity
  // Read Humidity
  float h = dht.readHumidity();
  // Read temperature as Celsius (the default)
  float t = dht.readTemperature();

  if ( isnan(h) || isnan(t) || t > 100.00)
  {
    // Don't do anything, if data is invalid
    //    Serial.println("DHT11 data in invalid");
  }
  else
  {
    uint8_t temp = (uint8_t)(t);
    uint8_t humid = (uint8_t)(h);

    delay(1000);
    String hh = String(humid);
    String msg = String(temp);

    Serial.print("Publish message: ");
    Serial.println(msg);

    uint8_t numt = temp;
    char cstr[16];
    itoa(numt, cstr, 10);

    uint8_t numh = humid;
    char cshr[16];
    itoa(numh, cshr, 10);

    delay(1500);
    client.publish("dht", cstr);
    client.publish("bmp", cshr);
  }



  //  long now = millis();
  //  if (now - lastMsg > 2000) {
  //        lastMsg = now;
  //        ++value;
  //        snprintf (msg, 75, "hello world #%ld", value);
  //        Serial.print("Publish message: ");
  //        Serial.println(msg);
  //        client.publish("dht", msg);
  //    }


}
