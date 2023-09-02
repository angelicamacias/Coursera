
The python style fuidelines recommedn that class name should start wiht a capital letter. ---> Apple
```python
>>> class Apple:
        color = ""
        flavor = ""

>>>jonagold = Apple()
>>>jonagold.color = "red"
>>>jonagold.flavor = "sweet"
>>>print(jonagold.color)
red
>>>print(jonagold.flavor)
sweet
```
## Dot notation
Lets you access any of the abilities the object might (called methods) or information it might store (called attributes) 

## Classes an objects in detail 
We can use the type() function to figure out what class a variable or value belongs to. For example, type(" ") tells us that this is a string class. The only attribute in this case is the string value, but there are a bunch of methods associated with the class. We've seen the upper() method, which returns the string in all uppercase, as well as isnumeric() which returns a boolean telling us whether or not the string is a number. You can use the dir() function to print all the attributes and methods of an object. Each string is an instance of the string class, having the same methods of the parent class. Since the content of the string is different, the methods will return different values. You can also use the help() function on an object, which will return the documentation for the corresponding class. This will show all the methods for the class, along with parameters the methods receive, types of return values, and a description of the methods.

### Instances variables
Varibles that have different values for different instances of the same class are called instance variables. 


```python
class Piglet: 
        name = "piglet"
        def speak(self):
                print("Oink! I'm {}! Oink!".format(self.name))

hamlet = Piglet()
hamlet.name = "Hamlet"
hamlet.speak()
--output--> Oink! I'm Hamlet! Oink!

petunia = Piglet()
petunia.name = "Petunia"
petunia.speak()
--output--> Oink! I'm Petunia! Oink!

```

exampel 2

```python 
class Piglet: 
        years = 0
        def pig_years(self):
                return self.years * 18

petunia = Piglet()
petunia.years = 2
print(petunia.pig_years())
```
```python
class Dog:
        years = 0
        def dog_years(self):
                return self.years * 7
fido=Dog()
fido.years=3
print(fido.dog_years())
```

## What is a Method? 

Calling methods on objects executes functions that operate on attributes of a specific instance of the class. This means that calling a method on a list, for example, only modifies that instance of a list, and not all lists globally. We can define methods within a class by creating functions inside the class definition. These instance methods can take a parameter called self which represents the instance the method is being executed on. This will allow you to access attributes of the instance using dot notation, like self.name, which will access the name attribute of that specific instance of the class object. When you have variables that contain different values for different instances, these are called instance variables.

## Constructor method

```python 
class Apple: 
        def __init__(self, color, flavor):
                self.color = color
                self.flavor = flavor
jonagold = Apple("red", "sweet")
print(jonagold.color)
--output--> red
```

```python
class Person:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        # Should return "hi, my name is " followed by the name of the Person.
        return ("hi, my name is {}".format(self.name))

# Create a new instance with a name of your choice
some_person = Person("Gris") 
# Call the greeting method
print(some_person.greeting())

--output--> hi, my name is Gris
```

## HELP
```python
class Person:
  def __init__(self, name):
    self.name = name
  def greeting(self):
    """Outputs a message with the name of the person"""
    print("Hello! My name is {name}.".format(name=self.name)) 

help(Person.greeting)
```
## Inheritance

This allows us to reduce code dupliaction by generalizing our code

```python 

class Fruit: 
        def __init__(self, color, flavor):
                self.color = color
                self.flavor = flavor

class Apple(Fruit):
        pass

class Grape(Fruit):
        pass

granny_smith = Apple("green", "tart")
carnelian = Grape("purple", "sweet")

print(granny_smith.flavor)
--output--> tart

print(carnelian.color)
--output--> purple
```

### Composition 

 use of the code in the other classes by calling their methods. 


 Always initialize mutable attributes in the constructor. 

 You can have a situation where two different classes are related, but there is no inheritance going on. This is referred to as composition -- where one class makes use of code contained in another class. For example, imagine we have a Package class which represents a software package. It contains attributes about the software package, like name, version, and size. We also have a Repository class which represents all the packages available for installation. While there’s no inheritance relationship between the two classes, they are related. The Repository class will contain a dictionary or list of Packages that are contained in the repository. 

 ```python
 >>> class Repository:
...      def __init__(self):
...          self.packages = {}
...      def add_package(self, package):
...          self.packages[package.name] = package
...      def total_size(self):
...          result = 0
...          for package in self.packages.values():
...              result += package.size
...          return result
```
In the constructor method, we initialize the packages dictionary, which will contain the package objects available in this repository instance. We initialize the dictionary in the constructor to ensure that every instance of the Repository class has its own dictionary.

We then define the add_package method, which takes a Package object as a parameter, and then adds it to our dictionary, using the package name attribute as the key.

Finally, we define a total_size method which computes the total size of all packages contained in our repository. This method iterates through the values in our repository dictionary and adds together the size attributes from each package object contained in the dictionary, returning the total at the end. In this example, we’re making use of Package attributes within our Repository class. We’re also calling the values() method on our packages dictionary instance. Composition allows us to use objects as attributes, as well as access all their attributes and methods.

## Modules

Used to organize functions, classes, and other data together in a structured way 