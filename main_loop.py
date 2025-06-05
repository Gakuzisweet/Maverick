import time
from imu_reader import IMUReader
from orientation_filter import ComplementaryFilter
from pid_controller import PIDController
from pwm_output import PWMOutput

# === Configuration ===
dt = 0.02
kp = 1.2
ki = 0.01
kd = 0.05
alpha = 0.98

# PWM output config
PWM_MIN = 5.0   # 1.0 ms pulse
PWM_MAX = 10.0  # 2.0 ms pulse
MID_DUTY = 7.5  # Neutral throttle

# Initialize modules
imu = IMUReader()
filter = ComplementaryFilter(alpha=alpha)
pid_pitch = PIDController(kp, ki, kd, dt)
pid_roll = PIDController(kp, ki, kd, dt)

# Initialize motors (ESCs or servos)
pitch_motor = PWMOutput(pin=18)  # GPIO 18
roll_motor = PWMOutput(pin=19)   # GPIO 19

# Setpoints
target_pitch = 0.0
target_roll = 0.0

print("✅ Main loop started. Press Ctrl+C to stop.")

try:
    while True:
        imu_data = imu.read()
        accel = imu_data['accel']
        gyro = imu_data['gyro']

        pitch, roll = filter.update(accel, gyro, dt)

        pitch_output = pid_pitch.update(target_pitch, pitch)
        roll_output = pid_roll.update(target_roll, roll)

        # Convert PID outputs to duty cycles (centered around MID_DUTY)
        def map_pid_to_pwm(output):
            scale = 0.05  # tune this sensitivity!
            pwm = MID_DUTY + output * scale
            return max(PWM_MIN, min(PWM_MAX, pwm))

        pitch_pwm = map_pid_to_pwm(pitch_output)
        roll_pwm = map_pid_to_pwm(roll_output)

        pitch_motor.set_duty_cycle(pitch_pwm)
        roll_motor.set_duty_cycle(roll_pwm)

        print(f"Pitch: {pitch:.2f}, Roll: {roll:.2f}")
        print(f"PWM -> Pitch: {pitch_pwm:.2f}%, Roll: {roll_pwm:.2f}%")
        print("-" * 40)

        time.sleep(dt)

except KeyboardInterrupt:
    print("🛑 Stopping motors and exiting...")
    pitch_motor.stop()
    roll_motor.stop()
