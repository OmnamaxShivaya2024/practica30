class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self,owner,model,engine_rower, color):
        self.owner= owner
        self.__module=model
        self.__engine_rower = engine_rower
        self.__color = color

    def get_model(self):
        print(f"модель:{self.__module}")

    def get_horsepower(self):
        print(f"мощность двигателя:{self.__engine_rower}")

    def get_color (self):
        print(f"цвет:{self.__color}")

    def print_info (self):
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print(f"Владелец:{self.owner}")

    def set_color (self,new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color= new_color
        else:
            print(f"нельзя сменить цвет на {new_color}")


pass
class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1= Sedan("Fedos","Toyota Mark II",500, "blue")
vehicle1.print_info()
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
vehicle1.print_info()






