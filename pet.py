class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5  # Starting hunger level
        self.energy = 10  # Starting energy level
        self.happiness = 5  # Starting happiness level
        self.tricks = []  # List to store learned tricks

    def eat(self):
        if self.hunger > 0:
            self.hunger = max(0, self.hunger - 3)
            self.happiness = min(10, self.happiness + 1)
            print(f"{self.name} is eating...")
        else:
            print(f"{self.name} is not hungry!")

    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} is sleeping...")

    def play(self):
        if self.energy >= 2:
            self.energy = max(0, self.energy - 2)
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} is playing...")
        else:
            print(f"{self.name} is too tired to play!")

    def get_status(self):
        print(f"{self.name}'s current status:")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Happiness: {self.happiness}")
        print(f"Tricks: {self.tricks}")

    def train(self, trick):
        self.tricks.append(trick)
        print(f"{self.name} has learned a new trick: {trick}!")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows the following tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")