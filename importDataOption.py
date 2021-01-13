import random
import csv

class Option:
    def __init__(self, lowerBound, higherBound, csvFileName, accountList):
        self.lowerBound = lowerBound
        self.higherBound = higherBound
        self.fieldList = ['Name','sheep_ref_InstallLocAddress__c','sheep_sel_sourceType__c','external_key__c','sheep_ref_topServiceContractName__c','sheep_ref_hostSystem__c','sheep_ref_topHardwareName__c','sheep_ref_topSoftwareName__c','sheep_txt_parentObjectExternalKey__c','sheep_txt_parentObjectName__c']
        self.fieldMap = {'sheep_ref_topServiceContractName__c':'Service Contract', 'sheep_ref_hostSystem__c':'System','sheep_ref_topHardwareName__c':'Hardware','sheep_ref_topSoftwareName__c':'Software'}
        self.dictList = []
        self. csvFileName = csvFileName
        self.accountList = accountList
    
    def makeData(self):
        lowerBound = self.lowerBound
        higherBound = self.higherBound
        for acc in self.accountList:
            for i in range(lowerBound, higherBound+1):

                parent = random.randint(1, 4)
                for filedName in self.fieldList:
                    if(filedName == 'Name'):
                        value = 'Test Opt '+str(i)
                    elif(filedName == 'sheep_sel_status__c'):
                        value = '導入待ち'
                    elif(filedName == 'sheep_ref_InstallLocAddress__c'):
                        value = acc
                    elif(filedName == 'sheep_sel_sourceType__c'):
                        value = 'Import'
                    elif(filedName == 'external_key__c'):
                        value = str(i)
                    else:
                        if(parent == 1):
                            if(filedName == 'sheep_ref_topServiceContractName__c'):
                                value = random.randint(lowerBound, higherBound)
                                finalParentValue = value
                                finalParentType = 'sheep_ref_topServiceContractName__c'
                            else:
                                value = ''
                        elif(parent == 2):
                            if(filedName == 'sheep_ref_hostSystem__c'):
                                value = random.randint(lowerBound, higherBound)
                                finalParentValue = value
                                finalParentType = 'sheep_ref_hostSystem__c'
                            else:
                                value = ''
                        elif(parent == 3):
                            if(filedName == 'sheep_ref_topHardwareName__c'):
                                value = random.randint(lowerBound, higherBound)
                                finalParentValue = value
                                finalParentType = 'sheep_ref_topHardwareName__c'
                            else:
                                value = ''
                        elif(parent == 4):
                            if(filedName == 'sheep_ref_topSoftwareName__c'):
                                value = random.randint(lowerBound, higherBound)
                                finalParentValue = value
                                finalParentType = 'sheep_ref_topSoftwareName__c'
                            else:
                                value = ''


                    try:
                        self.dictList[i-1][filedName]= value
                    except:
                        self.dictList.append({filedName:value})
                if(finalParentValue==''):
                    continue
                try:
                    self.dictList[i-1]['sheep_txt_parentObjectExternalKey__c']= finalParentValue
                except:
                    self.dictList.append({'sheep_txt_parentObjectExternalKey__c':finalParentValue})
                
                try:
                    self.dictList[i-1]['sheep_txt_parentObjectName__c']= self.fieldMap[finalParentType]
                except:
                    self.dictList.append({'sheep_txt_parentObjectName__c':self.fieldMap[finalParentType]})
            
            lowerBound = higherBound + 1
            higherBound = 2 * higherBound
            
    def writeCsv(self):
        with open(str(self.csvFileName)+'.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.fieldList)

            writer.writeheader()
            writer.writerows(self.dictList)
