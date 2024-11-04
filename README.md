1. Install Mosquitto:
> brew install mosquitto

2. After installation, you can start the Mosquitto service:
> brew services start mosquitto

3. Install Paho MQTT library for Python:
> pip3 install paho-mqtt

4. Execute publisher:
> python3 temp_sensor.py

5. Execute subscriber:
> python3 temp_display.py
