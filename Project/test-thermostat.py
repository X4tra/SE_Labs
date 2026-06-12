import unittest
from thermostat import ThermostatController

class TestThermostatController(unittest.TestCase):
    def test_heating_mode_triggered_when_cold(self):    
        controller = ThermostatController(target=20.0, hysteresis=1.0)
        state = controller.evaluate(current_temp=18.0)
        self.assertEqual(state, "HEATING")

    def test_cooling_mode_triggered_when_hot(self):
        controller = ThermostatController(target=20.0, hysteresis=1.0)
        state = controller.evaluate(current_temp=23.0)
        self.assertEqual(state, "COOLING")

if __name__ == '__main__':
    unittest.main()