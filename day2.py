input = open("input2.txt").readlines()

lines = []
for i in input:
    lines.append(i.strip('\n'))

# part 1
#

j = 0

for line in lines:
    args,string = line.split(": ")
    minmax,letter = args.split(" ")
    minimaal, maximaal = minmax.split("-")
    
    count = string.count(letter)
    
    if int(minimaal) <= count <= int(maximaal):
        j += 1    
        
print(j)


#part 2
#

m = 0

for line in lines:
    args,string = line.split(": ") # args is x-y z, string is wachtwoord
    pos,letter = args.split(" ") # minmax is x-y, letter is z
    pos1, pos2 = pos.split("-") #minimaal is x, maximaal is y
    
    posx = int(pos1) - 1
    posy = int(pos2) - 1
 

    if string[posx : posx + 1] == letter and string[posy : posy + 1] == letter:
        pass
    elif string[posx : posx + 1] == letter or string[posy : posy + 1] == letter:
        m += 1
        
print(m)



