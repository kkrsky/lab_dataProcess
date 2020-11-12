import copy as cp
import numpy as np

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

        #plasma parameter
        self.floatVolt=None

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
        self.createOutputData()
        return self.outputData

    #start
    def startUnitChangeForCalcProgram(self):
        self.unitChangeForCalcProgram()

    def startCalcIonSatCurrent(self):
        self.calcIonSatCurrent()
        

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
        dic={"data":self.calcData,"calcData":None,"deltaData":list(),"data_underFloatVolt":list()}

        # data_under0V=None

        # dataDict["data_under0V"]= [[line[0],line[1]*1000] for line in dataDict["data"] if line[0]<0]
        # data_delta= [[line[0],line[1]*1000] for line in data_under0V if line[0]<0]
        # self.calcData=data_under0V

        dic["data_underFloatVolt"]= [[line[0],line[1]*1000] for line in self.calcData if line[0]<0]
        plot_x= [line[0] for line in dic["data_underFloatVolt"]]
        plot_y= [line[1] for line in dic["data_underFloatVolt"]]
        plot_x_delta=np.diff(plot_x,n=1)
        plot_y_delta=np.diff(plot_y,n=1)
        # plot_y=plot_y_delta/plot_x_delta
        insertLength=len(plot_x_delta)

        for i in range(insertLength):
            # dic["deltaData"][i].insert(i,[plot_x[i],plot_y[i]])
            dic["deltaData"].insert(i,[plot_x[i],plot_y_delta[i]])
        # self.calcData=np.diff(self.calcData,n=1)
        # print("cal--data",dic["data"])
        # print("cal--0",dic["deltaData"])
        # print("cal--1",self.calcData[1])
        self.calcData=dic["deltaData"]

    def calcFloatVolt(self):
        #dataArry=[[v,mA],[],...]
        rawData=self.rawData
        # rawData=[[0,-8],[1,-10],[2,1],[3,0],[0,-1],[1,1]]
        # print("raw:",rawData)
        floatArry=[]
        isUnder=True
        isAddArry=False
        x_coord=None
        y_coord=None
        a_coord=None
        b_coord=None

        for i in range(len(rawData)):
            #プローブ電流が0となる点を挟む2点を求める
            volt=rawData[i][0]
            current=rawData[i][1]
            if(current<=0):
                
                if(isUnder==False):
                    isUnder=True
                    isAddArry=False
                    floatArry=[[volt,current]]
                    
                    pass
                else:
                    isUnder=True
                    floatArry=[[volt,current]]
                pass
            # elif(current==0):
            #     self.floatVolt=volt
            #     break
            else:
                #volt>0 
                isUnder=False
                if(isAddArry==True):
                    pass
                else:
                    isAddArry=True
                    floatArry.append([volt,current])

            # print(i,"isUnder:",isUnder,"isAddArry:",isAddArry,floatArry)
        x_coord,y_coord=self.xyLine(floatArry)
        # print(x_coord,y_coord)
        a_coord,b_coord=self.reg1dim(x_coord,y_coord)
        # print("a",a_coord,b_coord)
        
        #浮遊電位 出力
        self.floatVolt=self.findLinePoint(a=a_coord,b=b_coord,y=0)
        # print(self.floatVolt)
        # print("floatArry",floatArry)
    
    def xyLine(self,arry):
        plot_x= [line[0] for line in arry]
        plot_y= [line[1] for line in arry]
        return plot_x,plot_y
    def findLinePoint(self,*,a=1,b=1,x=None,y=None):
        #y=ax+b
        print("equation: y="+str(a)+"x+"+str(b))
        if(y==None):
            y=a*x+b
            print("[x,y_coord]:",x,y)
            return y
        elif(x==None):
            x=(y-b)/a
            print("[x_coord,y]:",x,y)
            return x
        else:
            print("xまたはyのみを引数にしてください")
    def reg1dim(self,x, y):
        #input : x,y list Arry
        x=np.array(x)
        y=np.array(y)
        n = len(x)
        a = ((np.dot(x, y)- y.sum() * x.sum()/n)/
            ((x ** 2).sum() - x.sum()**2 / n))
        b = (y.sum() - a * x.sum())/n
        return a, b