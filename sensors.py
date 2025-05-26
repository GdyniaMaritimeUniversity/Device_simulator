import random

def read_temperature():
    return round(random.uniform(18.0, 30.0), 2)

def read_humidity():
    return round(random.uniform(30.0, 90.0), 2)

def read_pressure():
    return round(random.uniform(980, 1050), 2)

def read_light_level():
    return round(random.uniform(100, 1000), 2)
