
import pandas as pd #for make a histgram data
import numpy as np
import matplotlib.pyplot as plt

class GraphGenerator():
    def __init__(self):
        pass
    def makeSimpleGraph(self,plot_x,plot_y):
        # plot_x=list()
        # plot_y=list()

        #グラフ共通設定
        #flg=10  # 凡例のフォントサイズ
        fti=20 # タイトルのフォントサイズ  

        # plt.rcParams["font.size"] = 20
        plt.rcParams['font.family'] ='sans-serif'

        #グラフ初期化
        fig = plt.figure(figsize=(8, 8))
        ax1 = fig.add_subplot(111)

        #グラフ作成
        ax1.plot(plot_x,plot_y)

        #グラフ設定
        ax1.set_title("Pixcel-Frequency",fontsize=fti)
        ax1.set_xlabel("Pixcel",fontsize=fti)
        ax1.set_ylabel("Normalized Frequency",fontsize=fti)
        ax1.set_xlim(0,255)
        ax1.set_ylim(ymin=0)
        # ax1.set_xlim(auto=True)
        # ax1.set_ylim(auto=True)

        #グラフ描画
        plt.show()
    def makeAllGraph(self,graphArry,titleArry):
        axList=list()
        graphId=0
        maxGraphNum=len(graphArry)
        label=None

        #グラフを表示する領域作成
        fig = plt.figure()

        #各種データ作成
        for outputData in graphArry:
            plot_x=[line[0] for line in outputData]
            plot_y=[line[1] for line in outputData]
            #add_subplot()でグラフを描画する領域を追加する．引数は行，列，場所
            ax=fig.add_subplot(maxGraphNum, 1, graphId+1)
            axList.append(ax)
            label="label"
            axList[graphId].plot(plot_x,plot_y,label=label)
            axList[graphId].set_xlabel("V [V]")
            axList[graphId].set_ylabel("I [mA]")
            axList[graphId].legend(loc = 'upper right') #凡例
            graphId+=1
        
        fig.tight_layout()              #レイアウトの設定
        plt.show()

