class Car:
    brand = "Toyota Kenya"
    def __init__ (self,model,reg):
        self.model=model
        self.reg=reg
    def identity(self):
        return f'My car is  {self.model} number plate {self.reg} from {self.brand}'