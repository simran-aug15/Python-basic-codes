marks={"Simran":100,
       "Samar":56,
       "Raman":13,
       "Akash":89}
print("The items are: ",marks.items())
print("The keys are: ",marks.keys())
print("The value are: ",marks.values())
a=marks.update({"Simran":98})
print("Marks after updating is: ",marks)
b=marks.pop("Raman",13)
print("Marks after popping is: ",marks)
c=marks.popitem()
print("marks after pop is: ",marks)