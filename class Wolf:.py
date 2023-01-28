class Wolf:
    # Class variables
    classification = "canine"
    habitat = "forest"
    is_sleeping = False
    # Constructor method with instance variables name and age
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # method that returns the sleep state of the wolf
    def show_sleep_state(self):
        if self.is_sleeping == False:
            return self.name + " is awake"
        else:
            return self.name + " is sleeping"
def main():
    # initialising a wolf object and printing the initial sleep
    # state which is awake
    silver_tooth = Wolf("Silver Tooth", 6)
    print(silver_tooth.show_sleep_state())
    # changing sleep state to sleeping using dot notation and then printing that state
    silver_tooth.is_sleeping = True
    print(silver_tooth.show_sleep_state())
# running main method
main()