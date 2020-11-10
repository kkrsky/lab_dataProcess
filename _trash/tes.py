
import os
import subprocess
import easygui
path = easygui.diropenbox(msg="tes",title="title",default="__outputs__")
print(path)
# FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'Explorer.exe')
# subprocess.run([FILEBROWSER_PATH, '/select,', os.path.normpath(path)])