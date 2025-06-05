import RPi.GPIO as GPIO
import time

class PWMOutput:
    def __init__(self, pin, frequency=50):
        self.pin = pin
        self.frequency = frequency  # Typically 50Hz for servos/ESCs
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)
        self.pwm = GPIO.PWM(pin, frequency)
        self.pwm.start(0)

    def set_duty_cycle(self, duty):
        # Clamp duty between 0 and 100 for safety
        duty = max(0, min(100, duty))
        self.pwm.ChangeDutyCycle(duty)

    def stop(self):
        self.pwm.stop()
        GPIO.cleanup(self.pin)
