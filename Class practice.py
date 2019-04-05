#class Vehicle(object):
    
    #base_sale_price = 0
    
    #def __init__(self, miles, sold_on):
        #self.miles = miles
        #self.sold_on = sold_on
        
    #def sale_price(self):
        #if self.sold_on:
            #return 0.0
        #else:
            #return 5000.0 * self.wheels
        
    #def purchase_price(self):
        #if not self.sold_on:
            #return 0.0
        #else:
            #return base_sale_price - (self.miles/10)
        
#class Car(Vehicle):
    
    #base_sale_price = 8000
    #wheels = 4
    
#class Truck(Vehicle):
    
    #base_sale_price = 10000
    #wheels = 4
    
#class Motorcycle(Vehicle):
    
    #base_sale_price = 5000
    #wheels = 2
    
#car1 = Car(1000, False)

#print(car1.sale_price())


#class Animal(object):
    
    #def __init__(self, name, start_pos):
        #self.name = name
        #self.start_pos = start_pos
        
    #def walk(self):
        #speed = 10 * self.legs
        #end_pos = self.start_pos + speed
        #return end_pos
        
#class Dog(Animal):
    
    #legs = 4
    #species = 'dog'
    
#class Chicken(Animal):
    
    #legs = 2
    #species = 'Chicken'
    
#class Centipied(Animal):
    
    #legs = 100
    #species = 'centipied'
    
#dog1 = Dog('Rover', 20)

#eugh = Centipied('Bert', 19)

#print(eugh.walk())

class Armour(object):
    
    def __init__(self, health, damage_removed, name, armour_health, damage_done):
        self.health = health
        self.damage_off = damage_off
        self.name = name
        self.armour_health = armour_health
        self.damage_done = damage_done
        
    def block(self):
        self.damage_done -= self.damage_off
        self.health -= self.damage_done
        