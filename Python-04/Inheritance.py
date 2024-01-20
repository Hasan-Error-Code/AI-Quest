class Phone:
    def Call(self):
        print("You can do Call")
    def Message(self):
        print("You can sent Message")
class Samsung(Phone):
    def Photo(self):
        print("You can take photo")

p = Samsung()
p.Call()
p.Message()
p.Photo()