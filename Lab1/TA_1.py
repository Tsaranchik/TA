#y1
print("S0 -> ", end="")
with open("code.txt", "r") as file:
    #y2
    data = file.readlines()
    
    #y3  new_data = []
    #x1  for item in data:
    #  y4, y5 new_data.extend(item.strip("\n"))
    #y6 data = new_data
    print("S1 -> ", end="")
    data = [item.strip("\n") for item in data]
#y7
file.close()

#y8
with open("code2.txt", "w") as file:
    #y9
    count = 0
    #x2
    for line in data:
        print("S2 -> ", end="")
        #x3
        if "for" in line:
            break
        #y10
        file.write(line + "\n")
        #y11
        count += 1
    #y12
    dataLen = len(data)
    
    #y3 new_data = []
    #x4 for idx in range(cout, dataLen):
    #   y13 new_data = data[idx]
    #y6 data = new_data
    print("S3 -> ", end="")
    data = [data[idx] for idx in range(count, dataLen)]
    #x5
    print("S4 -> ", end="")
    if len(data) == 0:
        #y8
        file.close
        #y14
        print("S0", end="")
        exit()
    #y15, y16, y17
    line = data[0]
    data.pop(0)
    line = line.strip()

    #y18, y19
    line = line[5:-3]
    innerFor = line.split(";")
    
    #y20, y21, y22
    cycleVar = innerFor[0].strip()
    cycleCondition = innerFor[1].strip()
    cycleIncrement = innerFor[2].strip()
    
    #y23, y24
    file.write("\t" + cycleVar + ";\n")
    file.write("label:\n")
    
    #y9, y25
    count = 0
    stack = "{"
    #x6
    for line in data:
        print("S5 -> ", end="")

        #x7, y26
        if "{" in line:
            stack += "{"
        
        #x8, y27
        print("S6 -> ", end="")
        if "}" in line:
            stack = stack[:-1]
            
        #x9, y28, y29, y30, y31, y32, y33, y34
        print("S7 -> ", end="")
        if line.strip() == "}" and stack == "":
            lessStr = f"if ({cycleCondition} - 1)" + " {"
            moreStr = f"if ({cycleCondition} + 1)" + " {"
            labelCondition = lessStr if "<" in cycleCondition else moreStr
            file.write("\t" + labelCondition + "\n")
            file.write("\t\t" + cycleIncrement + ";\n")
            file.write("\t\t" + "goto label;" + "\n")
            file.write("\t" + "}" + "\n")
            break
        
        #y35, y36, y11
        modifiedLine = line.replace(" ", "", 4)
        file.write(modifiedLine + "\n")
        count += 1
    #y12
    print("S8 -> ", end="")
    dataLen = len(data)
    
    #y3 new_data = []
    #x10 for idx in range(cout, dataLen):
    #   y13 new_data = data[idx]
    #y6 data = new_data
    print("S9 -> ", end="")
    data = [data[idx] for idx in range(count + 1, dataLen)]
    
    #x11, y10
    for line in data:
        print("S10 -> ", end="")
        file.write(line + "\n")
        
#y7        
file.close()
print("S0", end="")
        
        
    
    
        
        
            
        
        
        
        
        
    

    
    
        
        
            
        
        
    
    
    