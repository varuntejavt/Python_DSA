"""You can use this class to represent how classy someone
or something is.
"Classy" is interchangable with "fancy".
If you add fancy-looking items, you will increase
your "classiness".
Create a function in "Classy" that takes a string as
input and adds it to the "items" list.
Another method should calculate the "classiness"
value based on the items.
The following items have classiness points associated
with them:
"tophat" = 2
"bowtie" = 4
"monocle" = 5
Everything else has 0 points.
Use the test cases below to guide you!"""

class Classy(object):
    def __init__(self):
        self.items = []

    def addItem(self,item):
        (self.items).append(item)
        return self.items

    def getClassiness(self):
        count, count_t, count_b, count_m = 0,0,0,0
        count_t = count +  ((self.items).count('tophat'))*2

        count_b = count + ((self.items).count('bowtie'))*4

        count_m = count + ((self.items).count('monocle'))*5

        totalcount = count_t + count_b + count_m
        return totalcount

# Test cases
me = Classy()

# Should be 0
print me.getClassiness()

me.addItem("tophat")
# Should be 2
print me.getClassiness()

me.addItem("bowtie")
me.addItem("jacket")
me.addItem("monocle")
# Should be 11
print me.getClassiness()

me.addItem("bowtie")
# Should be 15
print me.getClassiness()
