tilin = ["Inicio", "Organizacion", "Resistecia", "Consumacion"]
a = int(input("Select a number between 0 to 3:"))
print(tilin[:a])
print(len(tilin))

#List Methods
leaders = []
leaders.append("Miguel Hidalgo y Costilla")
leaders.append("Vicente Guerrero")
#leaders.extend(tilin) //Mix list together
leaders.insert(1,"Jose Maria Morelos")
#leaders.remove("Vicente Guerrero") //Delete first mach of specific items
leaders.append("Agustin de Iturbide")
#leaders.pop(1)//Is the same that remove but using index
#leaders.clear()//Delete all the arguments of the list
print(leaders.index("Miguel Hidalgo y Costilla"))
print(leaders.count("Vicente Guerrero"))
print(leaders.sort())
#leaders.reverse() //The terms but in the reverse orden
new_leaders = leaders.copy()

print(leaders)
print(new_leaders)