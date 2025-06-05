# Maverick
Maverick is a Python-based drone flight controller built on a Raspberry Pi Zero 2 W. It performs real-time orientation estimation using an IMU (MPU6050), applies a complementary filter for sensor fusion, stabilizes the drone using a PID controller, and outputs PWM signals to drive servos or ESCs. This project is designed to simulate and eventually control a 5" drone, with future expansions including GPS navigation, AI-based object tracking, and telemetry.

Features

- Real-time sensor fusion using a complementary filter
- PID control for pitch/roll stabilization 
- PWM output generation for SG90 servo or ESC simulation
- Modular and testable codebase
- Mock mode to test without physical hardware
- Designed for expandability (GPS, AI, magnetometer, telemetry)

Folder Structure
- LICENSE
- README
- pid_controller.py
- imu_reader.py
- orientation_filter.py
- pwm_output.py
- main_loop.py

License

MIT License — see LICENSE file for details.

Author

Built by Mohamednur — 2nd year Electrical Engineering student passionate about embedded systems, autonomous systems, and real-time control.

Feel free to fork, star, and contribute!
