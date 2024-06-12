#Author: Tomás de Camino Beck
class Interpreter:
    def __init__(self):
        self.functionDict = {}
         
        
    def addFunction(self,name,f):
        self.functionDict.update({name:f})
        
    def execute(self,commands):
        for com in commands.split(':'):
            try:
                self.functionDict[com][0](self.functionDict[com][1])
            except:
                print('function not found')
