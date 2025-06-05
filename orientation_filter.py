import math

class ComplementaryFilter:
    def __init__(self, alpha=0.98):
        self.alpha = alpha
        self.pitch = 0
        self.roll = 0

    def update(self, accel, gyro, dt):
        accel_pitch = math.atan2(accel['y'], math.sqrt(accel['x']**2 + accel['z']**2)) * (180 / math.pi)
        accel_roll = math.atan2(-accel['x'], accel['z']) * (180 / math.pi)

        self.pitch = self.alpha * (self.pitch + gyro['x'] * dt) + (1 - self.alpha) * accel_pitch
        self.roll = self.alpha * (self.roll + gyro['y'] * dt) + (1 - self.alpha) * accel_roll

        return self.pitch, self.roll
