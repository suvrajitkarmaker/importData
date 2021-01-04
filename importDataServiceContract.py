import random
import csv
class ServiceContract:
    def __init__(self, lowerBound, higherBound, csvFileName, accountList):
        self.lowerBound = lowerBound
        self.higherBound = higherBound
        self.fieldList = ['Name','sheep_sel_status__c','sheep_ref_relatedBusinessPartner__c','sheep_sel_sourceType__c','external_key__c']
        self.dictList = []
        self. csvFileName = csvFileName
        self.accountList = accountList
    
    def makeData(self):

        for acc in self.accountList:
            for i in range(self.lowerBound, self.higherBound+1):

                for filedName in self.fieldList:
                    if(filedName == 'Name'):
                        value = 'Test Sc '+str(i)
                    elif(filedName == 'sheep_sel_status__c'):
                        value = '導入待ち'
                    elif(filedName == 'sheep_ref_relatedBusinessPartner__c'):
                        value = acc
                    elif(filedName == 'sheep_sel_sourceType__c'):
                        value = 'Import'
                    elif(filedName == 'external_key__c'):
                        value = str(i)

                    try:
                        self.dictList[i-1][filedName]= value
                    except:
                        self.dictList.append({filedName:value})

    def writeCsv(self):
        with open(str(self.csvFileName)+'.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.fieldList)

            writer.writeheader()
            writer.writerows(self.dictList)
