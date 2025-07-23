# PIR-Sensor-Detection
The following repository allows for simple detection using PIR Sensor.

## Start off by plugging in the PIR Sensor to the Raspberry Pi to the following pins:

| Name | Pin # | Pin name   |
|:------:|:-------:|:------------:|
| GND    | Any     |  Any Ground  |
| Data   | 11      | GPIO17     |
| 5..12V | 2       | 5V         |



<img width="1772" height="1112" alt="image" src="https://github.com/user-attachments/assets/fe87ea9f-f590-4bff-9e3e-26b6392bb6bb" />

## Setting up the RFID-RC522

**Step 1:** Download and navigate to the files using the following command:
<pre>
  cd Downloads/
  git clone https://github.com/Tristen-M-SDR/PIR-Sensor-Detection
  cd PIR-Sensor-Detection
</pre>

**Step 2:** Run the PIR Sensor using the following command:

<pre>
  sudo python3 IR.py
</pre>
