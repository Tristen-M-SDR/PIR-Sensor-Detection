from gpiozero import MotionSensor

pir = MotionSensor(17)

while True:
	pir.wait_for_no_motion()
	print("No Subject Detected.")
	pir.wait_for_motion()
	print("Subject Detected!")
