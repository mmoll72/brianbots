import pybullet as p
import time

SLEEP_TIME = 1 / 120

physicsClient = p.connect(p.GUI)

for i in range(1000):
        p.stepSimulation()
        time.sleep(SLEEP_TIME)
        print(i)

p.disconnect()
