import random
import csv

class Software:
    def __init__(self, lowerBound, higherBound, csvFileName, accountList):
        self.lowerBound = lowerBound
        self.higherBound = higherBound
        self.fieldList = ['Name','sheep_sel_status__c','sheep_ref_relatedBusinessPartner__c','sheep_sel_sourceType__c','external_key__c','sc_external_key','sys_external_key','hard_external_key','soft_external_key']
        self.dictList = []
        self. csvFileName = csvFileName
        self.accountList = accountList
    
    def makeData(self):
        lowerBound = self.lowerBound
        higherBound = self.higherBound

        for acc in self.accountList:
            singleItemMap = {}
            for i in range(lowerBound, higherBound+1):

                parent = random.randint(1, 4)
                for filedName in self.fieldList:
                    if(filedName == 'Name'):
                        value = 'Test Soft '+str(i)
                    elif(filedName == 'sheep_sel_status__c'):
                        value = '導入待ち'
                    elif(filedName == 'sheep_ref_relatedBusinessPartner__c'):
                        value = acc
                    elif(filedName == 'sheep_sel_sourceType__c'):
                        value = 'Import'
                    elif(filedName == 'external_key__c'):
                        value = str(i)
                    else:
                        if(parent == 1):
                            if(filedName == 'sc_external_key'):
                                value = random.randint(lowerBound, higherBound)
                            else:
                                value = ''
                        elif(parent == 2):
                            if(filedName == 'sys_external_key'):
                                value = random.randint(lowerBound, higherBound)
                            else:
                                value = ''
                        elif(parent == 3):
                            if(filedName == 'hard_external_key'):
                                value = random.randint(lowerBound, higherBound)
                            else:
                                value = ''
                        elif(parent == 4):
                            if(filedName == 'soft_external_key'):
                                value = random.randint(lowerBound, higherBound)
                                try:
                                    if(singleItemMap[i]==True):
                                        value = ''
                                except:
                                    pass
                                if(value!=''):
                                    singleItemMap[value]=True
                            else:
                                value = ''


                    try:
                        self.dictList[i-1][filedName]= value
                    except:
                        self.dictList.append({filedName:value})

            lowerBound = higherBound + 1
            higherBound = 2 * higherBound

    def writeCsv(self):
        with open(str(self.csvFileName)+'.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.fieldList)

            writer.writeheader()
            writer.writerows(self.dictList)
