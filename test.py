class superdupercooltryranasourausrex:
    def __init__(self, petname, money, happiness, hunger, clean, sleep):
        self.petname = petname
        self.money = money
        self.happiness = happiness
        self.hunger = hunger
        self.clean = clean
        self.sleep = sleep

    def alive(self):
        if self.hunger < 1:
            print ("BRO AINT NO WAY HOW DID U LET YOUR PET DIE U BROKIE")
            return "dead"
        if self.happiness < 1:
            print("YOUR CAT RAN AWAY")
            return "dead"
        if self.clean < 1:
            print ("your pet has rabies you DIED HAhA")
            return "dead"
        if self.sleep < 1:
            print("You shalln't advance thy day bluddy, your pet needs the sleep")
            return "dead"

    def eat(self):
        if self.money >= 25:
            self.money -= 25
            self.hunger += 15
            self.happiness += 6
            print("you fed your pet")
        else: 
            print("NO MONEY HABIBI go work")

    def sleep_pet(self):
        self.sleep += 15
        self.hunger -=15
        self.clean -=10
        day += 1
        print("sleeping through the night n\IF YOU KNOW YOU KNOW ")

    def play(self):
        if self.money >= 10:
            self.money -= 10
            self.happiness += 15
            self.hunger -= 5
            self.sleep -= 5
            print("your pet is happy")
        else: 
            print("NO MONEY HABIBI go work")

    def work(self):
        self.money += 35
        self.happiness -= 10
        self.hunger -= 10
        self.sleep -= 10
        self.clean -= 6

    def shower(self):
        if self.money >= 5:
            self.money -= 5
            self.clean += 10
            self.happiness += 5
            print("you cleaned your pet")
        else: 
            print("NO MONEY HABIBI go work")

    def stats(self):
        print("\nHere are your current stats:")
        print()
        print("---------------------------")
        print("Robux:", self.money)
        print("\nHunger:", self.hunger)
        print("\nHappiness:", self.happiness)
        print("\nClean:", self.clean)
        print("\nSleep:", self.sleep)
        print("----------------------------")

input("Welcome to raise a flopper!!! Press (((enter))) to start\n")

money = 100
hunger = 100
clean = 100
sleep = 100
happiness = 100
name = input("What are you going to name your pet? ")

pet = superdupercooltryranasourausrex(name, money, happiness, hunger, clean, sleep)

while True:
    if pet.alive() == "dead":
        break

    pet.stats()

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