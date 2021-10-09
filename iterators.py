fruits = ["Apples", "Oranges", "Pears"]

iterFruits = iter(fruits)

print(next(iterFruits))

fruits = ["Apples", "Oranges", "Pears"]
iterFruits = iter(fruits)
print(next(iterFruits))

for i in fruits:
    print(i)
print("\n")
while True:
    try:
        fruit = next(iterFruits)
        print(fruit)
    except StopIteration:
        break



class Example:
    def __iter__(self):
        self.a = 0
        return self
    
    def __next__(self):
        x = self.a
        self.a += 5
        return x

example = Example()
my_iter = iter(example)

print(next(my_iter))
print(next(my_iter))
raise Exception("Hello", "Hello")
print(next(my_iter))
print(next(my_iter))


# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n


# Using for loop
for item in my_gen():
    print(item)