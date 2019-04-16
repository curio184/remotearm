import time

import Adafruit_PCA9685


class Process:
    """
    サーボモータードライバ(PCA9685)を制御する
    通信方式：I2C
    """

    def __init__(self):
        self._pulse_min = 200  # Min pulse length out of 4096
        self._pulse_max = 600  # Max pulse length out of 4096

        self._pwm = Adafruit_PCA9685.PCA9685()
        self._pwm.set_pwm_freq(60)  # 60 Hz

    def _release(self):
        pass

    def start(self):
        try:
            while True:
                self._pwm.set_pwm(2, 0, self._pulse_min)
                time.sleep(1)
                self._pwm.set_pwm(2, 0, self._pulse_max)
                time.sleep(1)
        except KeyboardInterrupt:
            pass
        self._release()


if __name__ == "__main__":

    p = Process()
    p.start()
