# Lets go back to your group of friends

# We defined three friends in that lesson:

dillon_age = 12
kaden_age = 13
sarah_age = 11

# But what if you wanted each person to have more attributes?
# Like a hometown, school, name, etc
# You would have continued this pattern and done this:

dillon_name = 'dillon'
kaden_name = 'kaden'
sarah_name = 'sarah'

# But if you keep adding more attributes or people, this can get complicated really quickly

dillon_birthplace = 'Pasadena'
kaden_birthplace = 'Eagle Rock'
sarah_birthplace = 'Albambra'

dillon_school = 'USC'
kaden_school = 'Harvard'
sarah_school = 'Boston University'

# As you can see, this can get very complex very quickly

# What if there was a way to package this all up so you can create as many people as you want?

# This is where classes come in
# Classes are blueprints for creating objects

# To define a class, you write something like:

class Person:

# Now that you have this class, how do you add the attributes such as a name?

# This is a job for the Constructor

# The Constructor constructs an object.
# For instance, if you wanted to create another person named Dave, you would be constructing this person.

# Constructors are written as so:
  def __init__(self, name, age, birthplace, school):
    self.name = name
    self.age = age
    self.birthplace = birthplace
    self.school = school

  # Let's break this down:
  # __init__ is what constructors are always called
  # inside the parenthesis, all attributes of the person are listed
  # such as name, age, birthplace, and school
  # self is also always included at the moment
  # For now it doesn't matter why you write self.name = name, just make sure to always do this when defining these attributes

# Now that you have this constructor, you can go ahead and create people!

john = Person('John', 19, 'Pasadena', 'USC')
mary = Person('Mary', 21, 'Eagle Rock', 'Harvard')
calvin = Person('Calvin', 20, 'Alhambra', 'Boston University')

# See how much easier that is?

# But you can do other things within classes too!

# Remember that function we created last time for someone's birthday passing?

# Inside of the class, we can add it by doing this!:

def birthday(self):
  self.age = self.age + 1

