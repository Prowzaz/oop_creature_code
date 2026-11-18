class Creature:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def attack(self, target):
        if not self.is_alive():
            print(f"{self.name} cannot attack because it is defeated.")
            return

        print(f"{self.name} attacks {target.name} for {self.attack_power} damage!")
        target.hp = max(0, target.hp - self.attack_power)

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return f"{self.name} (HP: {self.hp})"

    

class FireCreature(Creature):
    def __init__(self, name, hp, attack_power, fire_level=0):
        super().__init__(name, hp, attack_power)
        self.fire_level = max(0, min(100, fire_level))

    def emit_fire(self, new_fire_level):
        self.fire_level = max(0, min(100, new_fire_level))
        print(f"{self.name} emits fire at level {self.fire_level}.")

    def attack(self, target):
        if not self.is_alive():
            print(f"{self.name} cannot attack because it is defeated.")
            return

        bonus = self.fire_level // 10
        damage = self.attack_power + bonus
        print(f"{self.name} blasts {target.name} with fire (level {self.fire_level})!")
        print(f"Total damage: {self.attack_power} + {bonus} fire bonus = {damage}")
        target.hp = max(0, target.hp - damage)
        print(f"{target.name} HP is now {target.hp}")



if __name__ == "__main__":
    print("=== Creature Class Tests ===\n")

    # Test 1: Initialization
    goblin = Creature("Goblin", 30, 5)
    print("Test 1: Initialization")
    print(goblin)  # Expected: Goblin (HP: 30)
    print()

    # Test 2: Basic attack
    wolf = Creature("Wolf", 40, 10)
    sheep = Creature("Sheep", 25, 3)
    print("Test 2: Wolf attacks Sheep")
    wolf.attack(sheep)
    print(f"Sheep HP should now be 15 → Actual: {sheep.hp}")
    print()

    # Test 3: HP does not go below zero
    dragon = Creature("Dragonling", 50, 100)
    mouse = Creature("Mouse", 20, 1)
    print("Test 3: Dragonling overkills Mouse")
    dragon.attack(mouse)
    print(f"Mouse HP should now be 0 → Actual: {mouse.hp}")
    print()

    # Test 4: is_alive()
    slime = Creature("Slime", 10, 2)
    print("Test 4: Slime alive?")
    print("Slime should be alive →", slime.is_alive())
    slime.hp = 0
    print("Slime should NOT be alive →", slime.is_alive())
    print()

    # Test 5: Dead creature cannot attack
    ghost = Creature("Ghost", 0, 10)
    knight = Creature("Knight", 50, 7)
    print("Test 5: Ghost tries to attack Knight")
    ghost.attack(knight)
    print(f"Knight HP should remain 50 → Actual: {knight.hp}")
    print()

    # Test 6: Multiple attacks
    print("Test 6: Goblin attacks Slime twice")
    slime.hp = 10
    goblin.attack(slime)
    goblin.attack(slime)
    print(f"Slime should be at HP 0 → Actual: {slime.hp}")
    print()

    # Test 7: Fire Creature ATK with Fire Bonus
    print("Test 7: Fire Imp attacks Practice Dummy with fire")
    imp = FireCreature("Fire Imp", 40, 6)
    imp.emit_fire(150)
    print(f"Fire level should be capped at 100 → Actual: {imp.fire_level}")
    imp.emit_fire(50)
    dummy = Creature("Practice Dummy", 40, 0)
    imp.attack(dummy)
    print(f"Dummy HP should be 29 → Actual: {dummy.hp}")
    print()

    
    print("=== Tests Completed ===")
    print()