from importDataServiceContract import ServiceContract
from importDataSystem import System
from importDataHardware import Hardware
from importDataSoftware import Software
from importDataOption import Option

lowerbound = 1
higherbound = 50
accountList = ['xxxxx']

sc = ServiceContract(lowerbound, higherbound, 'sheep_obj_servicecontract__c', accountList)
sc.makeData()
sc.writeCsv()

sys = System(lowerbound, higherbound, 'sheep_obj_system__c', accountList)
sys.makeData()
sys.writeCsv()

hard = Hardware(lowerbound, higherbound, 'sheep_obj_hardware__c', accountList)
hard.makeData()
hard.writeCsv()

soft = Software(lowerbound, higherbound, 'sheep_obj_software__c', accountList)
soft.makeData()
soft.writeCsv()

opt = Option(lowerbound, higherbound, 'sheep_obj_option__c', accountList)
opt.makeData()
opt.writeCsv()