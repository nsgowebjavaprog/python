# Set = {} ---> unorder, immuteable, no-duplication

friuts = {"a", "b", "c", "v", "s", "r"}
print(friuts)

friuts.add("asas")
friuts.remove("a")
print(friuts)

friuts.pop()
friuts.clear()
print(friuts)

'''
{'r', 'a', 'v', 'c', 's', 'b'}
{'r', 'asas', 'v', 'c', 's', 'b'}
set()
'''