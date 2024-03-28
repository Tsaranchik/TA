def printInfo(state, operation, operand1, operand2, error_code, result):
    print(state)
    print(operation)
    print(operand1)
    print(operand2)
    print(error_code)
    print(result)
    print("\n")
    

printInfo("S0 (000)", "00", "0"*16, "0"*16, "000" + ": No errors", "0"*16)

file = open("operands.txt", "r")

data = file.readline().split(" ")

bin_chars = ["0", "1"]
temp_str = "".join(data)

printInfo("S1 (001)", "00", "0"*16, "0"*16, "000" + ": No errors", "0"*16)

if not all(char in bin_chars for char in temp_str) or temp_str == "":
    error_code = "001"
    
    printInfo("S0 (000)", "00", "0"*16, "0"*16, error_code + ": Uncorrect characters in file", "0"*16)
    
    exit()

operation = data[0]

printInfo("S2 (010)", operation, "0"*16, "0"*16, "000" + ": No errors", "0"*16)

if operation != "11" and operation != "00":
    error_code = "010"
    
    printInfo("S0 (000)", operation, "0"*16, "0"*16, error_code + ": Unknown operation", "0"*16)

    exit()

if len(data[1]) != 16 or len(data[2]) != 16:
    error_code = "011"
    
    printInfo("S0 (000)", operation, "0"*16, "0"*16, error_code + ": Uncorrect operands length", "0"*16)
    
    exit()
    
operand1 = int(data[1], 2)
operand2 = int(data[2], 2)

printInfo("S3 (011)", operation, bin(operand1)[2:], bin(operand2)[2:], "000" ": No errors", "0"*16)

if operand2 == 0 and operation == "11":
    error_code = "100"
    
    printInfo("S0 (000)", operation, bin(operand1)[2:], bin(operand2)[2:], error_code + ": Substract on zero", "0"*16)

    exit()

if operation == "11":
    res = bin(operand1 // operand2)[2:]
    
    printInfo("S4 (100)", operation, bin(operand1)[2:], bin(operand2)[2:], "000" + ": No errors", "0"*16)
    
    if len(res) < 16:
        res = "0" * (16 - len(res) ) + res
    
    printInfo("S5 (101)", operation, bin(operand1)[2:], bin(operand2)[2:], "000" + ": No errors", res) 
    
    printInfo("S0 (000)", operation, bin(operand1)[2:], bin(operand2)[2:], "000" + ": No errors", res) 
    
    exit()

if operation == "00":
    res = bin(operand1 * operand2)[2:]
    
    printInfo("S6 (110)", operation, bin(operand1)[2:], bin(operand2)[2:], "000" + ": No errors", "0"*16)
    
    if len(res) > 16:
        error_code = "101"
        
        printInfo("S0 (000)", operation, bin(operand1)[2:], bin(operand2)[2:], error_code + ": Bit overflow", "0"*16)

        exit()
    
    if len(res) < 16:
        res = "0" * (16 - len(res)) + res
    
    printInfo("S7 (111)", operation, bin(operand1)[2:], bin(operand2)[2:], "000" + ": No errors", res)
    
    printInfo("S0 (000)", operation, bin(operand1)[2:], bin(operand2)[2:], "000" + ": No errors", res)
    
    exit()