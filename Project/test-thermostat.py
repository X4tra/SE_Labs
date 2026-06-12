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

    def test_heating_remains_active_within_hysteresis_range(self):
        controller = ThermostatController(target=20.0, hysteresis=1.5)
        
        # 1 Trigger Heating by dropping temp
        controller.evaluate(current_temp=18.0) 
        
        # 2 Temp recovers slightly to 19.0C within safety window
        # It should stay HEATING to avoid rapid compressor cycling
        state = controller.evaluate(current_temp=19.0)
        self.assertEqual(state, "HEATING")

    def test_cooling_remains_active_within_hysteresis_range(self):
        controller = ThermostatController(target=20.0, hysteresis=1.5)
        
        # 1 Trigger Cooling by rising temp
        controller.evaluate(current_temp=22.0) 
        
        # 2 Temperature drops marginally to 21.0°C within safety window
        # It should stay in a COOLING state
        state = controller.evaluate(current_temp=21.0)
        self.assertEqual(state, "COOLING")

if __name__ == '__main__':
    unittest.main()