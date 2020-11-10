import pandas as pd
import numpy as np
from numpy import random as rand


def create_white_image(total_track_time):
    time = []
    prev_location = rand.randint(300)
    x_location = []
    velocity = 25
    acceleration = 5
    for t in np.arange(0, total_track_time * 4 / 5, 0.5):
        time.append(t)
        acceleration = acceleration + rand.randint(10) * rand.rand() + 5
        velocity = velocity + acceleration
        x = prev_location + velocity
        x_location.append(x)
        prev_location = x
        print(prev_location)
    last_time = time[len(time) - 1]
    print(len(time))
    print(len(x_location))
    while prev_location > 0:
        last_time = last_time + 0.5
        time.append(last_time)
        acceleration = acceleration - rand.randint(20) * rand.rand() - 5
        velocity = velocity + acceleration
        x = prev_location + velocity
        x_location.append(x)
        prev_location = x
        print("prev_location", prev_location)
    print(len(time))
    print(len(x_location))
    df = pd.DataFrame(data={"time": time, "location": x_location})
    df.to_csv("D:\\locations.csv", sep=',', index=False)


create_white_image(700)