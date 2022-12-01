def listToInt(reading: list)-> int:
    value = "".join([str(number) for number in reading])
    value = int(value,2)
    return value

def findGasNum(isCO2: bool, lines: list) -> int:
    gas = lines.copy()

    index = 0
    while len(gas) != 1 and index != len(gas[0]):
        print('gas',len(gas))
        print('index',index)
        gas0 = []
        gas1 = []
        for entry in gas:
            if entry[index] == '0':
                gas0.append(entry)
            else:
                gas1.append(entry)
        if not isCO2:
            if gas1 is not None and len(gas1)>=len(gas0):
                gas = gas1.copy()
            else:
                gas = gas0.copy()
        else:
            if gas0 is not None and len(gas1)>=len(gas0):
                gas = gas0.copy()
            else:
                gas = gas1.copy()
        print('gas',gas)
        index+=1
    print(gas)
    return(listToInt(gas[0]))

f = open("2021/3/3_input.txt", "r")
lines = f.read().splitlines()
print(lines[0][0])
print('CO2CO2CO2CO2')
CO2level = findGasNum(1, lines)
print('O2O2O2O2O2O2')
O2level = findGasNum(0, lines)

print(CO2level,O2level)
print(CO2level*O2level)