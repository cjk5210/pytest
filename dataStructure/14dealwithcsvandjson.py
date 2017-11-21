import json
def analysisStringToJson():
    stringOfJsonData='{"name":"Zophie","isCat":true,"miceCaught":0,"felineIQ":null}'
    jsonDataAsPythonValue=json.loads(stringOfJsonData)
    print(str(jsonDataAsPythonValue))
    print(type(jsonDataAsPythonValue))
#analysisStringToJson()

def convertDictToJson():
    pythonValue={'isCat':True,'miceCaught':0,'name':'Zophie','feilineIQ':None}
    print(type(pythonValue))
    stringOfJsonData=json.dumps(pythonValue)
    print(type(stringOfJsonData))
    print(stringOfJsonData)
#convertDictToJson()
