import random

class Story:
    def getInput(self):
        name = input("Enter a name: ")
        place = input("Enter a place: ")
        object = input("Enter an object: ")
        person = input("Enter another name: ")
        animal = input("Name any animal: ")
        return name, place, object, person, animal

    def makeStory(self):
        choice = random.randint(1,2)
        name, place, object, person, animal = self.getInput()
        story1 = name + " was going to visit " + person + ", who lives in " + place + " where he saw a cute " + animal + ".  " + name + " was so impressed that now the " + animal + " will go with " + name + " and will live in the same house. And now the " + animal + " loves to play with the " + object + "."
        story2 = name + " was chilling at home in " + place + " and while playing with " + object+ "."
        if choice == 1:
            return story1
        elif choice == 2:
            return story2
    
    def printStory(self):
        story = self.makeStory()
        print(story)



obj = Story()
storyFinal = obj.printStory()
