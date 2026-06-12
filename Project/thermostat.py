class ThermostatController:
    def __init__(self, target: float, hysteresis: float):
        self.target = target
        self.hysteresis = hysteresis

    def evaluate(self, current_temp: float) -> str:
        if current_temp < self.target:
            return "HEATING"
        elif current_temp > self.target:
            return "COOLING"
        return "IDLE"