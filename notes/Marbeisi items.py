class Items(object):

    def __init__(self):
        self.name = name
        self.health = 100
        self.armor = 100
        self.inventory = 10
        self.energy = 100
        self.health_kit_inventory = 50

        class Weapons(Items):
            def __init__(self, damage):
                super(Weapons, self).__init__(name)
                self.damage = damage
                self.inventory = []
                if health <= damage:
                    print("There is damage done!")

            def baseballbat(self):
                self.damage -= 15
                self.inventory += 5
                print("You have swinged the bat!")
                answer = input("Do you want to pick this up?")
                print("You have answer %s , you have picked this item up!" % answer)
                if answer.lower() in ['no']:
                    print("item is not picked up!")

            def pitchfork(self):
                self.damage -= 20
                self.inventory += 10
                print("you hav picked up the pitchfork!")
                answer = input("Do you want to pick this up?")
                print("You have answer %s , you have picked this item up!" % answer)
                if answer.lower() in ['no']:
                    print("item is not picked up!")

            def hammer(self):
                self.damage -= 10
                self.inventory += 4
                print("you have used the hammer!")
                answer = input("Do you want to pick this up?")
                print("You have answer %s , you have picked this item up!" % answer)
                if answer.lower() in ['no']:
                    print("item is not picked up!")

            def sword(self):
                self.dmage -= 20
                self.inventory += 7
                print("You have used your sword")
                answer = input("Do you want to pick this up?")
                print("You have answer %s , you have picked this item up!" % answer)
                if answer.lower() in ['no']:
                    print("item is not picked up!")

            def axe(self):
                self.damage -= 15
            answer = input("Do you want to pick this up?")
            print("You have answer %s , you have picked this item up!" % answer)
            if answer.lower() in ['no']:
                print("item is not picked up!")

        class Tools(Items):
            def __init__(self, inventory):
                super(Tools, self).__init__(name)
                self.inventory = inventory

            def nails(self):
                self.inventory += 1
                print("This has been added to your inventory!")

            def matches(self):
                self.inventory += 3
                print("This has been added to your inventory!")

            def key(self):
                self.inventory += 1
                print("This has been added to your inventory!")

        class Energy(energy):
            def __init__(self, energy):
                super(Energy, self).__init__(name)
                self.energy = energy

            def food(self):
                self.energy = energy

            def chickennuggets(self):
                self.energy += 5
                print("Your energy has been boosted up!")

            def energydrinks(self):
                self.energy += 10
                print("Your energy has been boosted up!")

        class HealthKit(healthkit, health):
            def __init__(self):
                super(HealthKit, self).__init__(name)
                self.health_Kit_Inventory = 50

            def bandages(self):
                self.health_Kit_Inventory += 2
                print("Your health kit has more stuff now!")
                print("You can use any of this anytime!")

            def medicine(self):
                self.health_Kit_Inventory += 5
                print("Your health kit has more stuff now!")
                print("You can use any of this anytime!")

            def anesthetic(self):
                self.health_Kit_Inventory += 5
                self.health += 5
                print("Your health kit has more stuff now!")
                print("You can use any of this anytime!")

            def scissors(self):
                self.health_Kit_Inventory += 2
                print("Your health kit has more stuff now!")
                print("You can use any of this anytime!")

            class Electronics(electronics, on=True, off=False):
                def __init__(self):
                    super(Electronics, self).__init__(name)
                    self.on = True
                    self.off = False

                def microwave(self):
                    self.on = True
                    print("The flashlight is on!")
                    self.off = False
                    print("The flashlight is off!")

                def flashlight(self):
                    self.on = True
                    print("The flashlight is on!")
                    self.off = False
                    print("The flashlight is off!")

            class Armor(armor, protection):
                def __init__(self):
                    super(Armor, self).__init__(name)
                    self.protection = protection

                def helmet(self):
                    self.protection = protection
                    self.damage -= 5
                    self.health -= 5
                    print("Some damage was done.")

                def chestplate(self):
                    self.protection = protection
                    self.damage -= 5
                    self.health -= 5
                    print("Some damage was done.")

                def shield(self):
                    self.protection = protection
                    self.damage -= 5
                    self.health -= 5
                    print("Some damage was done.")

                if armor >= damage:
                    print("No damage is done")
                elif damage >= armor:
                    print("There is %s damage done! " % damage)
