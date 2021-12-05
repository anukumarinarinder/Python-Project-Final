import random

class Story:
    def getInput(self):
        name = input("Enter a name: ")
        gender = input("Enter the gender: ")
        if gender.lower() == "male":
            pronoun1 = "he"
            pronoun2 = "his"
            pronoun3 = "him"
        elif gender.lower() == "female":
            pronoun1 = "she"
            pronoun2 = "her"
            pronoun3 = "her"
        place = input("Enter a place: ")
        object = input("Enter an object: ")
        person = input("Enter another name: ")
        animal = input("Name any animal: ")
        return name, place, object, person, animal, pronoun1, pronoun2, pronoun3

    def makeStory(self):
        choice = random.randint(1,4)
        name, place, object, person, animal, pronoun1, pronoun2, pronoun3 = self.getInput()
        story1 = name + " was going to visit " + person + ", who lives in " + place + " where he saw a cute " + animal + ".  " + name + " was so impressed that now the " + animal + " will go with " + name + " and will live in the same house. And now the " + animal + " loves to play with the " + object + "."
        story2 = name + " was chilling at home in " + place  + ". There pronoun1 saw one animal in trouble, pronoun1 was too busy that pronoun1 did not help it, so pronoun1 walked away. Days passed by, but one day nam" + name + "e got stuck in some serious problem, but there was noone to help " + pronoun2 + ", in such situation " + pronoun1 + " realized that even " + pronoun1 + " left that " + animal + " all alone in that situation. " + pronoun1 + " got to know how it is like to left all alone."
        story3  = "There was once a person named " + name + ". " + pronoun1 + " had a pet " + animal + ". On one bright day " + pronoun1 + " went for a walk with " + pronoun2 + " pet animal. There " + pronoun1 + " saw an injured bird, " + pronoun1 + " picked up the bird and helped it. " + pronoun1 + " then decided to adopt the bird, brought it home took care of it and bought a cage for it. But soon " + pronoun1 + " realized that the bird was not happy so " + pronoun1 + " decided to set the bird free. " + pronoun1 + " then went to place and released the bird, because nobody likes to live in a cage."
        story4 = "There once a child named " + name + " liven in place. " + pronoun1 + " always used to joke on people of " + place + ". One day pronoun1 was in serious trouble but sue to pronoun1's habbit of joking noone believed " + pronoun2 + ". So, " + pronoun1 + " was left all alone."
        if choice == 1:
            return story1
        elif choice == 2:
            return story2
        elif choice == 3:
            return story3
        elif choice == 4:
            return story4

    
    def printStory(self):
        story = self.makeStory()
        print(story)



obj = Story()
storyFinal = obj.printStory()
