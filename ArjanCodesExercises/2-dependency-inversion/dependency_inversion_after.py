from abc import ABC,abstractmethod
"""
    Remove the dependency of power switch on lightbulb in order to do that 
    we are going to need a concept called an abstract class.

    Dependency Inversion helps you seperate components it helps you reduce coupling in your code.
"""
class Switchable(ABC):
    """
        Instead of having two classes that are directly coupled. We now decoupled them through
        an interface in this case called Switchable.
    """
    def turn_on(self):
        pass
    def turn_off(self):
        pass

class LightBulb(Switchable):
    def turn_on(self):
        print("LightBulb: turned on...")

    def turn_off(self):
        print("LightBulb: turned off...")

class Fan(Switchable):
    def turn_on(self):
        print("Fan: turned on...")

    def turn_off(self):
        print("Fan: turned off...")

class ElectricPowerSwitch:
    def __init__(self, s: Switchable):
        self.client = s
        self.on = False

    def press(self):
        if self.on:
            self.client.turn_off()
            self.on = False
        else:
            self.client.turn_on()
            self.on = True
            
l = LightBulb()
f = Fan()
switch = ElectricPowerSwitch(l)
switch.press()
switch.press()
switch = ElectricPowerSwitch(f)
switch.press()
switch.press()