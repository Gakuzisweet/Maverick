from mpu6050 import mpu6050

class IMUReader:
    def __init__(self, address=0x68):
        self.sensor = mpu6050(address)

    def read(self):
        accel = self.sensor.get_accel_data()
        gyro = self.sensor.get_gyro_data()
        return {
            'accel': accel,
            'gyro': gyro
        }
