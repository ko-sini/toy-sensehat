from sense_hat import SenseHat

def temperature_str():
    x = round(sense.get_temperature(), 1)
    return f"{x} C"

def humidity_str():
    x = round(sense.get_humidity(), 1)
    return f"{x} %rH"

def pressure_str():
    x = round(sense.get_pressure(), 1)
    return f"{x} mbar"

def show(value: str):
    if value in ["temp", "temperature", "C", "c"]:
        message = temperature_str()
    elif value in ["humidity", "rH", "rh"]:
        message = humidity_str()
    elif value in ["pressure", "mbar"]:
        message = pressure_str()
    else:
        message = " ".join([temperature_str(), humidity_str(), pressure_str()])
    sense.show_message(message)

if __name__ == "__main__":
    sense = SenseHat()
    show("humidity")