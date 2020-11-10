import copy as cp

#local
import GraphGenerator as gg
gg=gg.GraphGenerator()

class DataProcess():
    def __init__(self):
        self.rawData=None
        self.calcData=None
        self.outputData=None
        self.outputDataHistory=list()
        self.fileNameHistory=list()

    #core func
    def setFileRawData(self,fr):
        arry=None
        arry=[line.split() for line in fr]
        arry=arry[2:-1]
        arry=[[float(num) for num in line] for line in arry]
        self.rawData=cp.deepcopy(arry)
        self.calcData=cp.deepcopy(arry)
        # self.outputData=cp.deepcopy(arry)
    def setFileName(self,name):
        self.fileNameHistory.append(name)

    def createOutputData(self):
        self.outputDataHistory.append(self.calcData)
        arry=[" ".join(map(str,line)) for line in self.calcData]
        arry='\n'.join(map(str,arry))
        self.outputData=arry

    def getOutputData(self):
        return self.outputData

    #start
    def startUnitChangeForCalcProgram(self):
        self.unitChangeForCalcProgram()
        self.createOutputData()

    def startCalcIonSatCurrent(self):
        self.calcIonSatCurrent()
        self.createOutputData()

    def showGraph(self):

        plot_x=[line[0] for line in self.calcData]
        plot_y=[line[1] for line in self.calcData]
        gg.makeSimpleGraph(plot_x,plot_y)

    def showAllGraph(self):

        gg.makeAllGraph(self.outputDataHistory,self.fileNameHistory)

    #func
    def unitChangeForCalcProgram(self):
        #[[V,μA],[]...] => [[V,mA],[]...]
        self.calcData= [[line[0],line[1]*1000] for line in self.calcData]

    def calcIonSatCurrent(self):
        # for line in self.calcData:
        #     [x,y]=line
        #     if(x<0):

        #         self.calcData.append([x,y*1000])
            

        self.calcData= [[line[0],line[1]*1000] for line in self.calcData if line[0]<0]

