class superdupercooltryranasourausrex:
    def __init__(self, petname, money, happiness, hunger, clean, sleep):
        self.petname = petname
        self.money = money 
        self.happiness = happiness
        self.hunger = hunger
        self.clean = clean
<<<<<<< HEAD
        self.sleep = sleep

=======
        self.slep = sleep
>>>>>>> f221a747eca4a498b61af9816a90016e4c128357
    def alive(self):
        if self.hunger < 1:
            print ("BRO AINT NO WAY HOW DID U LET YOUR PET DIE U BROKIE")
            return "dead"
        if self.happiness < 1:
            print("YOUR CAT RAN AWAY")
            return "dead"
        if self.clean < 1: 
<<<<<<< HEAD
            print ("your pet has rabies you DIED HAhA")
            return "dead"
        if self.sleep < 1:
=======
            print ("your pet has rabies and bit you so you both DIED HAhA")
            return("dead")
        if self.slep < 1:
>>>>>>> f221a747eca4a498b61af9816a90016e4c128357
            print("You shalln't advance thy day bluddy, your pet needs the sleep")
            return "dead"

    def eat(self):
        if self.money >= 25:
<<<<<<< HEAD
            self.money -= 25
            self.hunger += 15
            self.happiness += 6
            print("you fed your pet")

    def sleep_pet(self):
        self.sleep += 15
        self.hunger -=15
        self.clean -=10
        print("sleeping through the night n\IF YOU KNOW YOU KNOW ")

    def play(self): 
=======
            self.money - 15
            self.hunger + 20
            self.happiness + 6
            print("you fed your pet thumbs up emoji")
    def slp (self):
        if sleep(self): 
            self.slep +=20
            day +=1
            print("sleeping through the night. IF YOU KNOW YOU KNOW HAHAHAHA")
    def play (self): 
>>>>>>> f221a747eca4a498b61af9816a90016e4c128357
        if self.money >= 10:
            self.money -= 10
            self.happiness += 15
            self.hunger -= 5
            self.sleep -= 5
            print("your pet is happy")

    def work(self): 
        self.money += 35
        self.happiness -= 5
        self.hunger -= 5
        self.sleep -= 5
        self.clean -= 5

    def shower(self):
        if self.money >= 5:
            self.money -= 5
            self.clean += 10
            self.happiness += 5
            print("you cleaned your pet")

    def stats(self):
        print("\nHere are your current stats:")
        print("---------------------------")
        print("Robux:", self.money)
        print("\nHunger:", self.hunger)
        print("\nHappiness:", self.happiness)
        print("\nClean:", self.clean)
        print("\nSleep:", self.sleep)
        print("----------------------------")
    def money(self):
        if money >=0:
            print ("get back to work broke boi")

input("Welcome to raise a flopper!!! Press (((enter))) to start\n")

<<<<<<< HEAD
=======

>>>>>>> f221a747eca4a498b61af9816a90016e4c128357
money = 100
hunger = 100
clean = 100
sleep = 100
<<<<<<< HEAD
happiness = 100
name = input("What are you going to name your pet? ")

pet = superdupercooltryranasourausrex(name, money, happiness, hunger, clean, sleep)

while True:
    if pet.alive() == "dead":
        break

    pet.stats()
=======
happiness = 100 
day = 1
input("welcome to raise a flopper!!! Here are yoiur stats. \n press enter to advance")
name = input("what are you going to name your pet")
pet = superdupercooltryranasourausrex(money, happiness, hunger, clean, sleep)

while True:
    if pet.alive() == False:
        print ("your pet died skull emoji")
        break

print("\n what do you want to do?")
print("1. eat")
print("2. play")
print("3. sleep")
print ("4. clean")
print("5. make a youtube video")
>>>>>>> f221a747eca4a498b61af9816a90016e4c128357

    print("\nWhat do you want to do?")
    print("1. eat")
    print("2. play")
    print("3. sleep")
    print("4. shower")
    print("5. work")

    choice = input("Choose: ")

    if choice == "1":
        pet.eat()
    elif choice == "2":
        pet.play()
    elif choice == "3":
        pet.sleep_pet()
    elif choice == "4":
        pet.shower()
    elif choice == "5":
        pet.work()
    else:
        print("choose an option from 1-5 not 6 or 7")
    


# make a "COC" api 
# first we gotta make za troops
# all troops that cost elixr
# 1.barb
# 2.archer
# 3.goblins
# 4.e drag
# 5.e titan
# 6.wizard
# 7.balloon 
# 8.giant
# 9.bombers
# 10.
# Dark elixr troops
# 1.Valxrye
# 2.minion
# 3.golem
# 4.hog rida
# 5.witch 

# 😂😂😂😂😂🤣🤣🤣😁😂🤣🤣😁😂🤣🤣

# # class Calculator():
# #     def add(x, y):
# #         print(x + y)
# #         return x + y

# #     def add_many(numbers):
# #         print(sum(numbers))
# #         return sum(numbers)

# #     def subtract(numbers):
# #         return numbers

# # Calculator.add(5, 67)