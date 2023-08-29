from pathlib import Path
import os,pyinputplus as pyip,shutil
sourceFolder = pyip.inputStr(prompt='Enter Folder Where File Are Located : - ')
sourceFolder = Path.home() / sourceFolder
destinationFolder= pyip.inputStr('Enter Destination Folder Name: - ')  # Enter the destination folder name here
destinationFolder = Path.home() / destinationFolder
def validate():
        if sourceFolder.is_dir() and destinationFolder.is_dir() == True:
                try:
                    for files in os.listdir(sourceFolder):
                        sourceFolderfiles = sourceFolder / files 
                        shutil.copy(sourceFolderfiles,destinationFolder)
                except FileNotFoundError:
                    print('Files Not Found')
validate()
for fileText in destinationFolder.glob('*.txt'):
                os.mkdir(Path(destinationFolder/'textfiles'))
                shutil.copy(Path(destinationFolder / fileText),Path(destinationFolder / 'textfiles'))
for fileVideo in destinationFolder.glob('*.mp4'):
                os.mkdir(Path(destinationFolder/'VideoFiles'))
                shutil.copy(Path(destinationFolder / fileVideo),Path(destinationFolder / 'VideoFiles'))
for fileImage in destinationFolder.glob('*.png'):
                os.mkdir(Path(destinationFolder/'ImageFiles'))
                shutil.copy(Path(destinationFolder /fileImage ),Path(destinationFolder / 'ImageFiles'))
for  filescode in destinationFolder.glob('*.py'):
                os.mkdir(Path(destinationFolder/'CodeFiles'))
                shutil.copy(Path(destinationFolder / filescode ),Path(destinationFolder / 'CodeFiles'))
