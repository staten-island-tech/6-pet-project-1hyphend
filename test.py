class superdupercooltryranasourausrex:
    def __init__ (self, petname, money, happiness, hunger, clean, sleep):
        self.petname = petname
        self.money = money 
        self.happiness = happiness
        self.hunger = hunger
        self.clean = clean
        self.sleep = sleep
    def alive(self):
        if self.hunger < 1:
            print ("BRO AINT NO WAY HOW DID U LET YOUR PET DIE U BROKIE")
            return ("dead")
        if self.happiness < 1:
            print("YOUR CAT RAN AWAY")
            return("dead")
        if self.clean < 1: 
            print ("your pet has rabies and bit you so you both DIED HAhA")
            return("dead")
        if self.sleep < 1:
            print("You shalln't advance thy day bluddy, your pet needs the sleep")
            return("dead")
    def eat (self):
        if self.money >= 25:
            self.money - 15
            self.hunger + 20
            self.happiness + 6
            print("you fed your pet thumbs up emoji")
    def sleep (self):
        if sleep(self): 
            self.sleep +=20
            day +=1
            print("sleeping through the night. IF YOU KNOW YOU KNOW HAHAHAHA")
    def play (self): 
        if self.money >= 10:
            self.money - 10 
            self.happiness +15
            self.hunger - 5
            self.sleep - 5
            print("your pet is so happy")
    def work(self): 
        self.money + 35
        self.happiness - 5
        self.hunger - 5
        self.sleep - 5
        self.clean - 5
    def shower (self):
        if self.clean >= 10:
            self.money - 5
            self.clean + 10
            self.happiness +5
            print("you have cleaned your pet")
    def stats(self):
        print ("\n heres your current stat")
        print ("You have this much robux:", self.money)
        print("You have this much hungry:", self.hunger)
        print("You have this mich happyness", self.happiness)
        print("Youhave this much clean", self.clean)
        print("You have this much sleep:", self.sleep)
    


input("welcome to raise a flopper!!! Here are yoiur stats. \n press enter to advance")
money = 100
hunger = 100
clean = 100
sleep = 100
happiness = 100 
day = 1

name = input("what are you going to name your pet")
pet = superdupercooltryranasourausrex(money, happiness, hunger, clean, sleep)
while True:
    if pet.alive() == False:
        print ("your pet died skull emoji")
        break

print("\n what do you want to do?")
print("1. ear")
print("2. play")
print("3. sleep")
print ("4. clean")
print("5. make a youtube video")

choice = input("choose: ")

if choice == "1":
    pet.eat
if choice == "2":
    pet.play
if choice == "3":
    pet.sleep
if choice == "4":
    pet. clean
if choice == "5":
    pet.work
else:
    print ("you have to choose an option from 1 to 4")




#     HOW DO I DO THIS BRUH 
#     WoRK ON YHIS TOMOMOROW MORNING 
    


# class human(superdupercooltryranasourausrex):

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