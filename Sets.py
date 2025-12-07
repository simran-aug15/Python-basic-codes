s={1,23,45,67,89,13,90}
s1={22,42,78,12,68}
print(s)
s.add(234)
print(s)
print("length is: ",len(s))
s.remove(23)
print("set after removing 23 is: ",s)
s.clear()
print("set after clearing is: ",s)
print(s.union(s1))
print(s.intersection(s1))
