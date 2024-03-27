class Fruits:
    def __init__(self, name: str):
        self._name = name # to make name private

    # def get_name(self):
    #     return self._name
    
    # def set_name(self, new_name: str):
    #     self._name = new_name
        
    @property
    def fruit_name(self):
        print(f"{self._name} was accessed.")
        return self._name

    @fruit_name.setter
    def fruit_name(self, value):
        print(f"{self._name} is now {value}")
        self._name = value

    @fruit_name.deleter
    def fruit_name(self):
        print(f"{self._name} was deleted")
        del self._name


if __name__ == '__main__':
    fruit1 = Fruits('Banana')
    fruit2 = Fruits('Grapes')
    # print(fruit1._name)
    # fruit1.set_name('Orange')
    # print(fruit1.get_name())


    ############################# easier way
    print(fruit1.fruit_name) 
    fruit1.fruit_name = 'Apple' # setter
    del fruit1.fruit_name # deleter
    print(fruit2.fruit_name) 
    fruit2.fruit_name = 'Vine'
    del fruit2.fruit_name


