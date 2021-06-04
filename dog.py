class Dog:
    nationality="Kenyan"
    def __init__ (self, color,breed,height):
        self.color= color
        self.breed= breed
        self.height= height
    def pet(self):
        return f'The dog is a {self.color}, {self.breed} which is {self.height} tall'