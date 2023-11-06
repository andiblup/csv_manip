
from csv import reader, writer
from sys import exc_info

thisFolder = './'

# create output file            # ! IMPORTANT ANPASSBAR
finalCsvFileName = 'endProduct' # TODO: OUTPUT NAME
givenCSVFileName = 'data'       # TODO: INPUT NAME
csvEnding = '.csv'



exists = False
commaCount = 0
commaCountList = []

#endProd = open(thisFolder + finalCsvFileName + csvEnding, 'x')
endProdList = []   

# try open it, if not create it
try:
    f = open(thisFolder + finalCsvFileName + csvEnding, 'r')
    f.close()
    exists = True
except exc_info()[0]:
    open(thisFolder + finalCsvFileName + csvEnding, 'x')
    
# if default name exists: create default + incrementing number
if exists:
    with open(thisFolder + finalCsvFileName + csvEnding, 'r') as file:
        newFileName = ""
        counter = 2
        name_is_not_available = True
        old_name = finalCsvFileName
        while(name_is_not_available):
            try:
                f = open(thisFolder + finalCsvFileName + str(counter) + csvEnding, 'r')
                f.close()
                counter += 1
            except exc_info()[0]:
                name_is_not_available = False
                newFileName = finalCsvFileName + str(counter)
                
        with open(thisFolder + newFileName + csvEnding, 'x') as f:
            f.close()
            finalCsvFileName = newFileName
        
with open(thisFolder + givenCSVFileName + csvEnding) as file:
    csv_reader = reader(file)
    # row is a list
    for row in csv_reader:
        #print(row)
        commaCount = 0
        for element in row:
            endProdList.append(element.split(';'))
            #print(type(endProdList[-1])) // list
            commaCount = len(endProdList[-1])
            
        #endProdList.append("\n")
        commaCountList.append(commaCount)
        #print(endProdList)

with open(thisFolder + finalCsvFileName + csvEnding, 'w') as file:
    csv_writer = writer(file)
    locCounter = 0
    elemCounter = 0
    iter = 0
    #print(endProdList)
    for element in endProdList:
        print(element)
        for part in element:
            
            if elemCounter == commaCountList[iter]:  
                elemCounter = 0
                iter += 1
                file.write("\n")
            
            file.write(part + ", ")
            locCounter +=1
            elemCounter += 1
        """    
        if element[0] != '' or element[0] != '\n' or locCounter != len(endProdList):
            if(element[0].startswith(' ') or element[0].startswith('\\s+')):
                file.write(element[0][1:len(element[0])] + ", ")
                locCounter += 1
                elemCounter += 1
            else:
                file.write(element[0]+ ", ")
                locCounter +=1
                elemCounter += 1
                """