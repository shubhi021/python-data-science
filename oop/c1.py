from audioop import tomono


class Cat:
    breed = None
    gender= None
    fur_color=  None
    age = None
    wieght = None
    hieght = None
    is_tamed = None

    def eat (self,food='catfood'):#the default food will be catfood if the food details are not mentioned.
        print(f'🐈 is eating{food}') 

    def play(self):
        print('cat is playing')

    def sleep(self):
        print('cat is sleeping')    

billu = Cat() #constructor calling
tom = Cat()
bagadbilla = Cat()

billu.breed = 'persian'
billu.wieght = 2
billu.age = 2
billu.fur_color = 'white'
billu.hieght = 1
billu.is_tamed = True
billu.gender = 'M'


tom.breed = 'street cat'
tom.wieght = 1.5
tom.age = 100
tom.fur_color = 'grey'
tom.hieght = 1.1
tom.is_tamed = True
tom.gender = 'M'

bagadbilla.breed = 'wild cat'
bagadbilla.wieght = 2
bagadbilla.age = 21
bagadbilla.fur_color = 'black'
bagadbilla.hieght = 1.5
bagadbilla.is_tamed = False
bagadbilla.gender = 'M'

print('Billu details')
print('breed:',billu.breed)
print('gender:',billu.gender)
print('age:',billu.age)
print('wieght:',billu.wieght)
print('hieght:',billu.hieght)
print('color:',billu.fur_color)
print('pet:','yes' if billu.is_tamed else 'no')
billu.sleep()
billu.eat()
billu.play()

print('Tom details')
print('breed:',tom.breed)
print('gender:',tom.gender)
print('age:',tom.age)
print('wieght:',tom.wieght)
print('hieght:',tom.hieght)
print('color:',tom.fur_color)
print('pet:','yes' if  tom.is_tamed else 'no')
tom.sleep()
tom.play()
tom.sleep()

print('Bagadbilla details')
print('breed:',bagadbilla.breed)
print('gender:',bagadbilla.gender)
print('age:',bagadbilla.age)
print('wieght:',bagadbilla.wieght)
print('hieght:',bagadbilla.hieght)
print('color:',bagadbilla.fur_color)
print('pet:','yes' if  bagadbilla.is_tamed else 'no')
bagadbilla.sleep()
bagadbilla.eat()
bagadbilla.play()
bagadbilla.sleep()