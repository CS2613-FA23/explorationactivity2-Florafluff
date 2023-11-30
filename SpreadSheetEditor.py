import pandas as pd
import sys
import matplotlib.pyplot as plt
plt.close("all")

def ADDC(df, listIn, name):
    newdf = pd.DataFrame(listIn, columns=[name])
    newdf.index = indexArray
    return pd.concat([df, newdf], axis=1)

def ADDR(df, listIn):
    newdf = pd.DataFrame([listIn], columns=list(df.columns))
    return pd.concat([df, newdf], ignore_index=True)

def REMC(df, name):
    try:
        return df.drop(name, axis=1)
    except KeyError:
        print("Invalid Column Name")
        return df

def REMR(df, row):
    try:
        df = df.drop(row)
        for i in range(len(indexArray)):
            if(indexArray[i] == row):
                indexArray.pop(i)
                break
        df.index = indexArray
        return df
    except KeyError:
        print("Invalid Row Name")
        return df
    
def PLOT(df, gType, titleName):
    plt.figure()
    if(gType == "line"):
        df.plot(title=titleName)
    else:
        df.plot(kind=gType, title=titleName)

name = input("Enter your spreadsheet's file name: ")
try:
    df = pd.read_csv(name)
except FileNotFoundError:
    print("Invalid file name")
    sys.exit()
    
try:
    indexList = df.pop("rowName")
    indexArray = []
    for i in range(indexList.shape[0]):
        indexArray.append(indexList[i])
    df.index = indexArray
except KeyError:
    print("Please include a column named \"rowName\" at the start of the file")
    sys.exit()

print(df.to_string())
done = False
columnName = ""
rowName = ""
newList = []
temp = 0
opened = False
print("\nCommand list:\n"
          + "ADDC: adds a column to the spreadsheet.\n"
          + "ADDR: adds a row to the spreadsheet.\n"
          + "REMC: removes a column from the spreadsheet\n"
          + "REMR: removes a row from the spreadsheet\n"
          + "DONE: finalizes all operations.")
while(done==False):
    command = input("Input command: ")
    if(command=="ADDC"):
        columnName = input("Enter the name of the column: ")
        for i in range(df.shape[0]):
            temp = input("Enter value for row " + str(i) + ": ")
            newList.append(float(temp))
        df = ADDC(df, newList, columnName)
        newList = []
    elif(command=="ADDR"):
        rowName = input("Enter the name of the row: ")
        for i in range(df.shape[1]):
            temp = input("Enter value for column " + str(i) + ": ")
            newList.append(float(temp))
        df = ADDR(df, newList)
        indexArray.append(rowName)
        df.index = indexArray
        newList = []
    elif(command=="REMC"):
        columnName = input("Enter the name of the column to delete: ")
        df = REMC(df, columnName)
    elif(command=="REMR"):
        columnName = input("Enter the name of the row to delete: ")
        df = REMR(df, columnName)
    elif(command=="DONE"):
        done = True
    else:
        print("Invalid command")
    
    if(done!=True):
        print(df.to_string())

print("Do you want to export the spreadsheet?")
output = input("\"CSV\": export as csv file\n\"EXCEL\": export as excel file\n\"NO\": don't export\n")

if(output!="NO"):
    fileName = input("Input name for new file (don't include file extension): ")


valid = False
while(valid == False):
    if(output == "CSV"):
        try:
            f = open(fileName + ".csv", "x")
            valid = True
            opened = True
        except FileExistsError:
            fileName = input("File name already exists, enter a new one: ")
    elif(output == "EXCEL"):
        try:
            f = open(fileName + ".xlsx", "x")
            valid = True
            opened = True
        except FileExistsError:
            fileName = input("File name already exists, enter a new one: ")
    elif(output == "NO"):
            valid = True
    else:
        output = input("Please input a valid command: ")
    
if(output == "CSV"):
    df.to_csv(fileName + ".csv")
elif(output == "EXCEL"):
    df.to_excel(fileName + ".xlsx")

print("Do you wish to plot the spreadsheet on a graph?")
command = input("\"LINE\" plot the spreadsheet in a line graph\n\"BAR\": plot the spreadsheet in a bar graph\n\"BOX\": plot the spreadsheet in a box graph\n\"HIST\": plot the spreadsheet in a histogram\n\"AREA\": plot the spreadsheet in a area graph\n\"NO\": don't plot the spreadsheet\n")

if(command!="NO"):
    graphName = input("Input the title of the graph:")

valid = False
while(valid == False):
    if(command == "LINE" or command == "BAR" or command == "BOX" or command == "HIST" or command == "AREA"):
        PLOT(df, command.lower(), graphName)
        valid = True
    elif(command == "NO"):
        valid = True
    else:
        command = input("Please input a valid command: ")
        
if(opened == True):
    f.close()