# WE NEED TO AUTOMATE THE TESTING !!!
# WE WILL WRITE A CLASS THAT TAKES ALL THE OCURRENCES AND GIVE IT INTO A LIST 

class TestAutomata:

    @staticmethod
    def getExpectedReps(fileName, itemName):

        expectedReps = []

        try:
            file = open(fileName, "r")

        except FileNotFoundError:
            print("can't open the specified file")

        else:
            hasStarted = False
            for line in file:
                line = line.strip()
                if line == "-------- day 1 --------": hasStarted = True
                if hasStarted:
                    if itemName in line:
                        expectedReps.append(line)
            file.close()

        return expectedReps

# print(TestAutomata.getExpectedReps("stdout.gr", "Aged Brie"))
# print(TestAutomata.getExpectedReps("stdout.gr", "Conjured"))
# print(TestAutomata.getExpectedReps("stdout.gr", "+5"))
# print(TestAutomata.getExpectedReps("stdout.gr", "Elixir"))

# NEED TO TAKE ONLY THE DESIRED ONES
# print(TestAutomata.getExpectedReps("stdout.gr", "Backstage passes"))
# print(TestAutomata.getExpectedReps("stdout.gr", "Sulfuras"))
