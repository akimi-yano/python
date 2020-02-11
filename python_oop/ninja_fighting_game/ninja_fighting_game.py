# Exciting Game by Aki, Ashley, Greg, Lucie 
class Ninja:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = None 
        self.food = None
        self.skill = None

    def displayStats(self):
        print(self.name+"'s Stats:")
        print("Health:", self.health)
        if self.weapon is not None:
            print("Weapon Damage:",self.weapon.damage)
        return self

    def displayInventory(self):
        print(self.name+"'s Inventory:")
        if self.weapon is not None:
            print("Weapon:", self.weapon.type)
        else:
            print("You have no weapon")
        if self.food is not None:
            print("Food:", self.food.type)
        else:
            print("You have no food")    
        if self.skill is not None:
            print("Skill:", self.skill.type)
        else:
            print("You have no skill")
        return self

    def pickUpWeapon(self, weaponType):
        if self.weapon is not None:
           print(f"{self.name} drops a {self.weapon.type}")
        self.weapon = Weapon(weaponType)   
        print(f"{self.name} picks up a {self.weapon.type}")
        return self

    def pickUpSkill(self,skillType):
        if self.skill is not None:
           print(f"{self.name} forgets {self.skill.type}")
        self.skill = Skill(skillType)
        print(f"{self.name} learns {self.skill.type}")
        return self    

    def fight(self,otherNinja):
        print("You started a fight with",otherNinja.name)
        if self.weapon is not None:
            if self.skill is not None:
                if self.skill.type == "power up":
                    otherNinja.health -= (self.weapon.damage + 20) 
                    print("You used your", self.weapon.type,"and",self.skill.type+".",otherNinja.name,"loses",(self.weapon.damage + 20),"health points.")
                else:
                    otherNinja.health -= self.weapon.damage 
                    print("You used your", self.weapon.type+".",otherNinja.name,"loses",self.weapon.damage,"health points.")
                if otherNinja.skill is not None:
                    if otherNinja.health <=0 and otherNinja.skill.type !="cheat death":
                        print(otherNinja.name,"is DEAD!")
                    elif otherNinja.health <=0:
                        otherNinja.health = 1
                        otherNinja.skill = None
                        print(otherNinja.name,"used cheat death skill, and revived with 1 health point.")
                elif otherNinja.health <=0:
                    print(otherNinja.name,"is DEAD!")
            else:
                otherNinja.health -= self.weapon.damage 
                print("You used your", self.weapon.type+".",otherNinja.name,"loses",self.weapon.damage,"health points.")
                if otherNinja.skill is not None:
                    if otherNinja.health <=0 and otherNinja.skill.type !="cheat death":
                        print(otherNinja.name,"is DEAD!")
                    elif otherNinja.health <=0:
                        otherNinja.health = 1
                        otherNinja.skill = None
                        print(otherNinja.name,"used cheat death skill, and revived with 1 health point.")
                elif otherNinja.health <=0:
                    print(otherNinja.name,"is DEAD!")
        elif otherNinja.weapon is not None:
            if self.skill is not None:
                if self.skill.type == "cheat death":
                    self.health = 1
                    self.skill = None
                    print("You used cheat death skill, and revived with 1 health point.")
                else:
                    self.health = 0
                    print("You are DEAD!")
            else:
                self.health = 0
                print("You are DEAD!")
        else:
            self.health -= 20
            otherNinja.health -=20
            print("You got into a fist fight, both of you received -20 damage. You deserved this...")
            if self.health <= 0 and self.skill is not None:
                if self.skill.type == "cheat death":
                    self.health = 1
                    self.skill = None
                    print("You used cheat death skill, and revived with 1 health point.")
                else:
                    self.health = 0
                    print("You are DEAD!")
            elif self.health <= 0:
                self.health = 0
                print("You are DEAD!")

            if otherNinja.health <= 0 and otherNinja.skill is not None:
                if otherNinja.skill.type == "cheat death":
                    otherNinja.health = 1
                    otherNinja.skill = None
                    print(otherNinja.name,"used cheat death skill, and revived with 1 health point.")
                else:
                    otherNinja.health = 0
                    print(otherNinja.name,"is DEAD!")
            elif otherNinja.health <= 0:
                otherNinja.health = 0
                print(otherNinja.name,"is DEAD!")
        return self

    def pickUpFood(self,foodType):
        if self.food is not None:
           print(f"{self.name} drops a {self.food.type}")
        self.food = Food(foodType)
        print(f"{self.name} picks up a {self.food.type}")
        return self

    def eatFood(self):
        if self.food is not None:
            print("You ate your",self.food.type)
            self.health += self.food.heal_damage
            if self.food.heal_damage > 0:
                print("You recovered",self.food.heal_damage,"health points!")
            else:
                print("HAHAHAHAHA,tricked you, the apple is poisonous! You lose",self.food.heal_damage,"health points!!!")
                if self.health <= 0 and self.skill is not None:
                    if self.skill.type == "cheat death":
                        self.health = 1
                        print("You used cheat death skill, and revived with 1 health point.")
                    else:
                        self.health = 0
                        print("You are DEAD!")
                elif self.health <= 0:
                    self.health = 0
                    print("You are DEAD!")
            self.food = None
        else:
            print("You do not have any food!")
        return self



class Weapon:
    def __init__(self, weaponType):
        damage = {"katana":25,"shuriken":15,"axe":30}
        self.type = weaponType
        self.damage = damage[weaponType] #tested: pass!
    
class Food:
    def __init__(self, foodType):
        heal_damage = {"strawberry":10,"pizza":20,"takoyaki":8,"shiny apple":-50}
        self.type = foodType
        self.heal_damage = heal_damage[foodType]      

class Skill:
    def __init__(self, skillType):
        self.type = skillType


#skills: "power up", "cheat death"
#weapon:Katana, Shuriken, Axe
#food: strawberry, pizza, takoyaki, **SHINY APPLE** :D 

kikomo = Ninja("Kikomo")
bakamo = Ninja("Bakamo")

#actions: 
# pick up a weapon
# pick up food
# learn a skill
# eat food
# fight

#anytime:
# show stats
# show inventory

bakamo.displayStats()
bakamo.displayInventory()
bakamo.pickUpFood("shiny apple")
kikomo.pickUpWeapon("shuriken")
bakamo.pickUpFood("pizza")
kikomo.pickUpSkill("cheat death")
kikomo.displayInventory()
bakamo.pickUpWeapon("axe")
kikomo.fight(bakamo)
bakamo.displayStats()
bakamo.pickUpSkill("power up")
kikomo.displayInventory()
kikomo.pickUpWeapon("katana")
bakamo.fight(kikomo)
kikomo.displayStats()
kikomo.pickUpFood("takoyaki")
bakamo.eatFood()
bakamo.displayStats()
kikomo.eatFood()
kikomo.displayInventory()
bakamo.fight(kikomo)
bakamo.fight(kikomo)
kikomo.displayInventory().displayStats() 
kikomo.pickUpFood("shiny apple")
kikomo.eatFood().displayStats()





