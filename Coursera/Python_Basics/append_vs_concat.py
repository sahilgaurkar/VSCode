origlist = [45, 32, 88]
print("origlist:", origlist)
print("The ID:", id(origlist))

newlist = origlist + ["cat"]
print("new list:", newlist)
print("The ID:", id(newlist))

origlist.append("cat")
print("origlist:", origlist)
print("The ID:", id(origlist))


