from collections import Counter
from collections import defaultdict

import countEachElementOccurensInoutFun

numbers = [1, 2, 3, 1, 3, 4]

# Step 1: Input module
countEachElementOccurensInoutFun.countEachElementOccurens(numbers)

print("Logic to print the count of items")

# Method 1: Using if-else and dictonories
def logicOccurenceUsingdictoniries():
    print("Using dictionaries (if-else)")
    count = {}
    for item in numbers:
        if item in count:
            count[item] += 1
        else:
            count[item] = 1
    print(count)

# Method 2: Using get()
def logicOccurenceUsingGet():
    print("Using get() method")
    occurence = {}
    for element in numbers:
        occurence[element] = occurence.get(element, 0) + 1
    print(occurence)

#Method 3: Using collections.Counter
def collectionsCounters():
    print("Using collections.Counter")
    counter=Counter(numbers)
    print(counter)

#Method 4: Using list counters
def UsingListCounters():
    print("Using lists.Counter")
    numbers1={}
    for num in numbers:
        numbers1[num] =  numbers.count(num)

    print(numbers1)

#Method 5: Using defaultdict
def defaultdictionaries():
    print("Using defaultdict")
    count1 = defaultdict(int)
    for items in numbers:
     count1[items] += 1
    print(dict(count1))

#Using List Comprehension + set()
def usinglistComprehe():
    print("Using list comprehension")
    count2 = {item2: numbers.count(item2) for item2 in set(numbers)}
    print(count2)


# Function calls
logicOccurenceUsingdictoniries()
logicOccurenceUsingGet()
collectionsCounters()
UsingListCounters()
defaultdictionaries()
usinglistComprehe()