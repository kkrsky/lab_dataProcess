import os,sys
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

#local


class DirSelectWidget():
    def __init__(self):
        self.entry1=None
        self.entry2=None
        self.dirPath=None
        self.FileCreater=None
    

    # フォルダ指定の関数
    def dirdialog_clicked(self):
        iDir = os.path.abspath(os.path.dirname(__file__))
        iDirPath = filedialog.askdirectory(initialdir = iDir)
        self.entry1.set(iDirPath)

    # # ファイル指定の関数
    # def filedialog_clicked(self):
    #     fTyp = [("", "*")]
    #     iFile = os.path.abspath(os.path.dirname(__file__))
    #     iFilePath = filedialog.askopenfilename(filetype = fTyp, initialdir = iFile)
    #     self.entry2.set(iFilePath)

    # 実行ボタン押下時の実行関数
    def conductMain(self):
        text = ""

        self.dirPath = self.entry1.get()
        dirPath=self.dirPath
        # filePath = self.entry2.get()
        if dirPath:
            text += "フォルダパス：" + dirPath + "\n"
        # if filePath:
        #     text += "ファイルパス：" + filePath

        if text:
            # messagebox.showinfo("info", text)
            print(text)

            #Dirパスを取得
            self.FileCreater(dirPath)
            quit()
        else:
            messagebox.showerror("error", "パスの指定がありません。")
    def setFileCreaterFunc(self,func):
        self.FileCreater=func
    def start(self):
        
        # rootの作成
        root = Tk()
        root.title("変換するフォルダの選択")

        # Frame1の作成
        frame1 = ttk.Frame(root, padding=10)
        frame1.grid(row=1, column=2, sticky=(E,W))

        
        # 「フォルダ参照」ラベルの作成
        IDirLabel = ttk.Label(frame1, text="フォルダ参照＞＞", padding=(5, 2))
        # IDirLabel.pack(side=LEFT)
        IDirLabel.grid(row=0, column=0)

        #使い方表示
        msg="・選択したフォルダ内の.txtのみ変換\n・[V] [μA]→[V] [mA]に一括変換\n・[__outputs__]フォルダに変換したファイルが入る"
        IDirLabel_detail = ttk.Label(frame1, text=msg, padding=(5, 2))
        IDirLabel_detail.grid(row=1, column=1)


        # 「フォルダ参照」エントリーの作成
        self.entry1 = StringVar()
        IDirEntry = ttk.Entry(frame1, textvariable=self.entry1, width=30)
        # IDirEntry.pack(side=LEFT)
        IDirEntry.grid(row=0, column=1)

        # 「フォルダ参照」ボタンの作成
        IDirButton = ttk.Button(frame1, text="参照", command=self.dirdialog_clicked)
        # IDirButton.pack(side=LEFT)
        IDirButton.grid(row=0, column=2)

        # # Frame2の作成
        # frame2 = ttk.Frame(root, padding=10)
        # frame2.grid(row=2, column=1, sticky=E)

        # # 「ファイル参照」ラベルの作成
        # IFileLabel = ttk.Label(frame2, text="ファイル参照＞＞", padding=(5, 2))
        # IFileLabel.pack(side=LEFT)

        # # 「ファイル参照」エントリーの作成
        # self.entry2 = StringVar()
        # IFileEntry = ttk.Entry(frame2, textvariable=self.entry2, width=30)
        # IFileEntry.pack(side=LEFT)

        # # 「ファイル参照」ボタンの作成
        # IFileButton = ttk.Button(frame2, text="参照", command=self.filedialog_clicked)
        # IFileButton.pack(side=LEFT)

        # Frame3の作成
        frame3 = ttk.Frame(root, padding=10)
        frame3.grid(row=5,column=2,sticky=(E,W))

        # 実行ボタンの設置
        button1 = ttk.Button(frame3, text="選択", command=self.conductMain)
        # button1.pack(fill = "x", padx=30, side = "left")
        button1.grid(row=0, column=0,sticky=(E,W),padx=50)
        # キャンセルボタンの設置
        button2 = ttk.Button(frame3, text=("閉じる"), command=quit)
        # button2.pack(fill = "x", padx=30, side = "left")
        button2.grid(row=0, column=1,sticky=(E,W),padx=50)

        root.mainloop()

        # return self.dirPath

if __name__ == "__main__":
    DirSelectWidget().start()