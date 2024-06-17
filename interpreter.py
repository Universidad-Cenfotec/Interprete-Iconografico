'''
***************************************************
  Universidad CENFOTEC invierte tiempo y recursos en el desarrollo de 
  contenidos Open Source. Apoye las actividades de la Universidad,
  y cualqueir modificación compártala de forma abierta

  Desarrollado por Tomás de Camino Beck
  MIT license, all text above must be included in any redistribution
 ****************************************************
'''

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
