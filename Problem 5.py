#Alex Flores
#November 16, 2023

class character:
    def __init__(self, nickname, weapons, weaknesses):
        self.nickname = nickname
        self.weapons = weapons
        self.weaknesses = weaknesses
    def get_model(self):
        return self.nickname
    def get_year(self):
        return self.weapons
    def get_color(self):
        return self. weaknesses
    def profile(self):
        return self.nickname, self.weapons, self. weaknesses
player1 = character('','','')
player1.nickname = 'Dragon Slayer'
player1.weapons = ['pan', 'paper', 'idea', 'rope', 'groceries']
player1.weaknesses = ['slow']
for item in player1.weapons:
    print("Item: ", item)
for debuff in player1.weaknesses:
    print("Debuff: ", debuff)

def can_perform_task(self, task_items, task_debuffs):
    for item in task_items:
        if item not in self.weapons:
            return False
    for debuff in task_debuffs:
        if debuff in self.weaknesses:
            return False
    return True
player1 = character("Dragon Slayer", ["pan", "paper", "idea", "rope", "groceries"], ["slow"])

task1 = {
    "items": ["rope", "coat", "first_aid_kit"],
    "debuffs": ["slow"],}
task2 = {
    "items": ["pan", "groceries"],
    "debuffs": ["small"],}
task3 = {
    "items": ["pen", "paper", "idea"],
    "debuffs": ["confusion"],}

can_perform_task1 = (task1["items"], task1["debuffs"])
can_perform_task2 = (task2["items"], task2["debuffs"])
can_perform_task3 = (task3["items"], task3["debuffs"])

print("Can perform task 1:", can_perform_task1)
print("Can perform task 2:", can_perform_task2)
print("Can perform task 3:", can_perform_task3)
