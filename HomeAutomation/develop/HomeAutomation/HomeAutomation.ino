/*
 * HomeAutomation
 * This sketch will subscribe the packets for turning on and off the relays.
 * This project uses CloudMQTT Server as MQTT Broker
 */
#include <DHT.h>
#include <DHT_U.h>
#include <ESP8266WiFi.h>
#include <PubSubClient.h>

// DHT11 Sensor Data Pin
#define DHTPIN    D5
// DHT Sensor Type
#define DHTTYPE DHT11   // DHT 11
//#define DHTTYPE DHT22   // DHT 22
//#define DHTTYPE DHT21   // DHT 21

// Relay (Loads) Pin
#define RELAY1    D1
#define RELAY2    D2
#define RELAY3    D6
#define RELAY4    D4

// Initialize DHT Sensor
DHT dht( DHTPIN, DHTTYPE);

// Update these Information
const char* ssid = "Tenda_Router";                    // WiFi Name
const char* password = "iotapp8266";            // WiFi Password
const char* mqtt_server = "m12.cloudmqtt.com";  // MQTT Server Name
const int mqtt_port = 14761;                    // MQTT Server Port
const char* user_name = "hhoixidh";             // MQTT Server Instance User Name
const char* mqtt_pswd = "jo8yv8O0-9bm";         // MQTT Server Instance Password

WiFiClient espClient;
PubSubClient client(espClient);
uint32_t lastMsg = 0;
#define MSG_BUFFER_LEN  10u
char msg[MSG_BUFFER_LEN];

// Setup WiFi Connection
void setup_wifi()
{
  delay(10);
  // We start by connecting to a WiFi network
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

// Callback Function
void callback(char* topic, byte* payload, uint16_t length)
{
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");
  for (uint16_t i = 0; i < length; i++)
  {
    Serial.print((char)payload[i], HEX);
  }
  Serial.println();

  // Check which topic we have received and based on that take action
  // led topic
  if( strcmp(topic,"led") == 0 )
  {
    // Switch on the LED if an 1 was received as first character
    if ((char)payload[0] == '1') 
    {
      digitalWrite(BUILTIN_LED, LOW);   // Turn the LED on
    }
    else 
    {
      digitalWrite(BUILTIN_LED, HIGH);  // Turn the LED off
    }
  }
  // Relay1 (Load1) Topic
  if( strcmp(topic, "load1") == 0 )
  {
    // Serial.println("Load1");
    if ((char)payload[0] == '1') 
    {
      digitalWrite( RELAY1, HIGH);
    }
    else
    {
      digitalWrite( RELAY1, LOW);
    }
  }
  
  // Relay2 (Load2) Topic
  if( strcmp(topic, "load2") == 0 )
  {
    // Serial.println("Load2");
    if ((char)payload[0] == '1') 
    {
      digitalWrite( RELAY2, HIGH);
    }
    else
    {
      digitalWrite( RELAY2, LOW);
    }
  }  
  // Relay3 (Load3) Topic
  if( strcmp(topic, "load3") == 0 )
  {
    // Serial.println("Load3");
    if ((char)payload[0] == '1') 
    {
      digitalWrite( RELAY3, HIGH);
    }
    else
    {
      digitalWrite( RELAY3, LOW);
    }
  }
  // Relay4 (Load4) Topic
  if( strcmp(topic, "load4") == 0 )
  {
    // Serial.println("Load4");
    if ((char)payload[0] == '1') 
    {
      digitalWrite( RELAY4, HIGH);
    }
    else
    {
      digitalWrite( RELAY4, LOW);
    }
  }
}

// Reconnect with Server Function
void reconnect() 
{
  // Loop until we're reconnected
  while (!client.connected()) 
  {
    Serial.print("Attempting CloudMQTT connection...");
    // Create a random client ID
    // String clientId = "ESP8266Client-";
    // clientId += String(random(0xffff), HEX);
    String clientId = "iotapp8266";
    Serial.print("Client Id:  ");
    Serial.println(clientId);
    // Attempt to connect
    // if (client.connect(clientId.c_str())) 
    if ( client.connect(clientId.c_str(), user_name, mqtt_pswd) )  
    {
      Serial.println("connected");
      // Once connected, publish an announcement...
      // client.publish("Broadcast", "Connected with MQTT Server");
      // ... and resubscribe (Topic is "LED", to control the on board LED)
      client.subscribe("led/#");
      // subscribe to load topics also.
      client.subscribe("load1/#");
      client.subscribe("load2/#");
      client.subscribe("load3/#");
      client.subscribe("load4/#");
    }
    else
    {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}

void setup() 
{
  pinMode(BUILTIN_LED, OUTPUT);     // Initialize the BUILTIN_LED pin as an output
  digitalWrite(BUILTIN_LED, HIGH);  // Turn-Off Led
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
  // Intiialize Serial Communication for Debug Messages
  Serial.begin(115200);
  // Setup NodeMcu with WiFi
  setup_wifi();
  client.setServer(mqtt_server, mqtt_port);
  client.setCallback(callback);
}

void loop() 
{
  if (!client.connected()) 
  {
    reconnect();
  }
  client.loop();

  uint32_t now = millis();
  // Publish Message After another 15 seconds
  if (now - lastMsg > 15000u)
  {
    lastMsg = now;
    // Read Humidity
    float h = dht.readHumidity();
    // Read temperature as Celsius (the default)
    float t = dht.readTemperature();
    // Check if any reads failed
    if( isnan(h) || isnan(t) )
    {
      // Don't do anything, if data is invalid
      Serial.println("DHT11 data in invalid");
    }
    else
    {
      uint8_t temp = (uint8_t)(t);
      uint8_t humid= (uint8_t)(h);
      snprintf(msg, MSG_BUFFER_LEN,"%02d,%02d", temp, humid);
      Serial.print("Publish message:  ");
      Serial.println(msg);
      client.publish("home", msg);
    }
  }
}
