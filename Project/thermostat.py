class ThermostatController:
    def __init__(self, target: float, hysteresis: float):
        self.target = target
        self.hysteresis = hysteresis

def evaluate(self, current_temp: float) -> str:
        if current_temp <= (self.target - self.hysteresis):
            self.current_state = "HEATING"
        elif self.current_state == "HEATING" and current_temp >= self.target:
            self.current_state = "IDLE"
            
        # temp
        elif self.current_state == "IDLE" and current_temp > self.target:
            return "COOLING"
            
        return self.current_state