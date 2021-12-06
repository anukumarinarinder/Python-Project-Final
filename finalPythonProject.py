# importing random library for choice
import random

# defining class story
class Story:
    # function to get input from user
    def getInput(self):
        name = input("Enter a name: ")
        gender = input("Enter the gender: ")
        # logic for gender
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

    # method for making stories
    def makeStory(self):
        # Getting a random number for choice
        choice = random.randint(1,6)
        name, place, object, person, animal, pronoun1, pronoun2, pronoun3 = self.getInput()
        # appending dynamic data into the stories
        story1 = name + " was going to visit " + person + ", who lives in " + place + " where he saw a cute " + animal + ".  " + name + " was so impressed that now the " + animal + " will go with " + name + " and will live in the same house. And now the " + animal + " loves to play with the " + object + "."
        story2 = name + " was chilling at home in " + place  + ". There pronoun1 saw one animal in trouble, pronoun1 was too busy that pronoun1 did not help it, so pronoun1 walked away. Days passed by, but one day nam" + name + "e got stuck in some serious problem, but there was noone to help " + pronoun2 + ", in such situation " + pronoun1 + " realized that even " + pronoun1 + " left that " + animal + " all alone in that situation. " + pronoun1 + " got to know how it is like to left all alone."
        story3  = "There was once a person named " + name + ". " + pronoun1 + " had a pet " + animal + ". On one bright day " + pronoun1 + " went for a walk with " + pronoun2 + " pet animal. There " + pronoun1 + " saw an injured bird, " + pronoun1 + " picked up the bird and helped it. " + pronoun1 + " then decided to adopt the bird, brought it home took care of it and bought a cage for it. But soon " + pronoun1 + " realized that the bird was not happy so " + pronoun1 + " decided to set the bird free. " + pronoun1 + " then went to place and released the bird, because nobody likes to live in a cage."
        story4 = "There once a child named " + name + " liven in place. " + pronoun1 + " always used to joke on people of " + place + ". One day " + pronoun1 + " was in serious trouble but sue to pronoun1's habbit of joking noone believed " + pronoun2 + ". So, " + pronoun1 + " was left all alone."
        story5 = "Once there was an old person named " + name + ", " + pronoun1 + " lived in a small town called " + place + " with " + pronoun2 + " pet " + animal + ". One day when " + pronoun1 + " woke up " + pronoun1 + " could not find " + pronoun2 + " pet. " + pronoun1 + " checked all over the place but could not find anything. Suddenly " + pronoun1 + " woke up from sleep and realized that it was just a dream. " + pronoun1 + " quickly called " + pronoun2 + " pet and gave it a hug."
        story6 = "Long time ago, there was a lion named " + name + ". " + pronoun1 + " lived with " + pronoun2 + " family - two baby lions. But because of deforestation, " + name + " could not feed " + pronoun2 + " children properly. Days passed by and the two babies grew up, but not so well. One day " + person + ", a businessman saw their condition and could not resist to help them. Not only " + person + " helped them but also bought the whole forest and made it green again."
        if choice == 1:
            return story1
        elif choice == 2:
            return story2
        elif choice == 3:
            return story3
        elif choice == 4:
            return story4
        elif choice == 5:
            return story5
        elif choice == 6:
            return story6

    # method to print the final story
    def printStory(self):
        story = self.makeStory()
        print(story)


# object of the class
obj = Story()

# calling method for printing out the story
storyFinal = obj.printStory()
