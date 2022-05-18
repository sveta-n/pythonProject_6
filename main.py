class Animal:
    def voice(self):
        pass


class Dog(Animal):
    def voice(self):
        print('гав')


class Cat(Animal):
    def voice(self):
        print('мяу')


class Mouse(Animal):
    def voice(self):
        print('пи-пи-пи')


hachiko = Dog()
hachiko.voice()
tom = Cat()
tom.voice()
jerry = Mouse()
jerry.voice()