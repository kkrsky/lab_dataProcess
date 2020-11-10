import glob
import os
import numpy as np

#local
import DirSelectWidget
import StateAll
import FileCreater


def main():
    # dw=DirSelectWidget.DirSelectWidget()
    # dw.setFileCreaterFunc(FileCreater.fileCreater)
    # dw.start()
    FileCreater.main()
   
if __name__ == '__main__':
    main()