import glob
import os
import shutil
import numpy as np
import subprocess
import easygui
import tkinter as tk
from tkinter import messagebox

#local
import DataProcess as dp
dp=dp.DataProcess()
def main():
    dirPath=r"C:\Users\紅林亮平\Desktop\【Input to excel】"
    fileCreater(dirPath)
def openExplorer(path):
    FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'Explorer.exe')
    subprocess.run([FILEBROWSER_PATH, '/select,', os.path.normpath(path)])

def getDirPath():
    return easygui.diropenbox(title="変換するフォルダを選択")

def fileCreater(dirPath):
    dirPath=getDirPath()
    i=None
    initialIndex=None
    outputFolder=r"\__outputs__"
    outputdirPath=dirPath+outputFolder
    
    if not os.path.isdir(outputdirPath):
        os.makedirs(outputdirPath)
    else:
        shutil.rmtree(outputdirPath)
        os.makedirs(outputdirPath)

    file_list = sorted(glob.glob(dirPath+'/*.txt'))
    # print("file_list",file_list)
    i=0
    for filenamePath in file_list:
        initialIndex=("00"+str(i+1))[-2:]+"_"
        fileNameText=filenamePath.split("\\")[-1:][0]
        if(fileNameText=="env.txt"):
            pass
        else:      
            arry=None
            with open(filenamePath, 'r') as fr:
                dp.setFileRawData(fr)
                # dp.startUnitChangeForCalcProgram()
                dp.startCalcIonSatCurrent()
                # dp.showGraph()

            with open(outputdirPath+"\\"+initialIndex+fileNameText,"w") as fw:
                dp.setFileName(initialIndex+fileNameText)
                arry=dp.getOutputData()
                fw.write(arry)
        i+=1
    dp.showAllGraph()
    
    if(i==0):
        root = tk.Tk()
        root.withdraw() #小さなウィンドウを表示させない
        shutil.rmtree(outputdirPath)
        messagebox.showerror("選択エラー", "変換可能なテキストファイルがありません。")
    else:
        #完了
        openExplorer(outputdirPath)

    

if __name__ == '__main__':
    main()