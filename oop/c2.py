class Cat:
    def  __init__(self,breed,fur_color,gender='F',age =1,w=1,h=1,is_tamed= True):
        self.breed = breed
        self.fur_color = fur_color
        self.gender = gender
        self.weight = w
        self.age = age
        self.height = h
        self.is_tamed = is_tamed

    def eat (self,food='catfood'):#the default food will be catfood if the food details are not mentioned.
        print(f'🐈 is eating{food}') 

    def play(self):
        print('cat is playing')

    def sleep(self):
        print('cat is sleeping')

    def info(self):
        print('---'*15)#optional design
        print(f'Breed:{self.breed}')
        print(f'Age:{self.age}year')
        print(f'Weight:{self.weight}Kg')
        print(f'Height:{self.height}ft')
        print(f'Gender:{self.gender}')
        print(f'Color:{self.fur_color}') 
        print(f'Tamed:{self.is_tamed}')  
        print('---'*15) #optional design

tom = Cat('street cat','grey',age = 100,gender ='M')
soni = Cat('house cat','brown',age= 3)
snowbell= Cat('Persian', 'white',age= 3,w=3)
spike = Cat ('Jungle cat','black',age= 2,w=.9,h= 1.1) 

print("TOM")
tom.info()
tom.eat('jerry')

print("SNOWBELL")
snowbell.info()
snowbell.eat('stuart')