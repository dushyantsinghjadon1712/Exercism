"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    product = temperature * neutrons_emitted
    if(temperature < 800 and neutrons_emitted > 500 and product < 500000):
        return True
    return False


def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage * current
    efficiency = (generated_power/theoretical_max_power) * 100
    if(efficiency >= 80):
        return "green"
    elif(efficiency < 80 and efficiency >= 60):
        return "orange"
    elif(efficiency < 60 and efficiency >= 30):
        return "red"
    return "black"


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    if((temperature * neutrons_produced_per_second) < 90/100 * threshold):
        return "LOW"
    elif((temperature * neutrons_produced_per_second) <= 110/100 * threshold ):
        return "NORMAL"
    else:
        return "DANGER"
