import random

def read_temperature():
    if random.random() < 0.05:
        return round(random.uniform(51.0, 60.0), 2)
    return round(random.uniform(18.0, 30.0), 2)

def read_humidity():
    if random.random() < 0.05:
        return round(random.uniform(91.0, 100.0), 2)
    return round(random.uniform(30.0, 90.0), 2)

def read_pressure():
    if random.random() < 0.05:
        return round(random.uniform(1051, 1070), 2)
    return round(random.uniform(980, 1050), 2)
