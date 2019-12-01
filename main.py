# Import


#Parse
Text = []
with open("input.txt") as In:
    for i in In:
        if i[len(i)-1] == "\n":
            i = i[0:len(i)-1]
        i = i.split(" ")
        Text.append(i) 