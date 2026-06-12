class ThermostatController:
    def __init__(self, target: float, hysteresis: float):
        self.target = target
        self.hysteresis = hysteresis
        self.current_state = "IDLE"

    def evaluate(self, current_temp: float) -> str:
        is_too_cold = current_temp <= (self.target - self.hysteresis)
        is_too_hot = current_temp >= (self.target + self.hysteresis)
        target_reached_from_below = current_temp >= self.target
        target_reached_from_above = current_temp <= self.target

        if self.current_state == "HEATING" and target_reached_from_below:
            self.current_state = "IDLE"
        elif self.current_state == "COOLING" and target_reached_from_above:
            self.current_state = "IDLE"
        elif is_too_cold:
            self.current_state = "HEATING"
        elif is_too_hot:
            self.current_state = "COOLING"

        return self.current_state