from pathlib import Path
import os,pyinputplus as pyip,shutil,glob
sourceFolder = pyip.inputStr(prompt='Enter Folder Where File Are Located : - ')
sourceFolder = Path.home() / sourceFolder
destinationFolder= pyip.inputStr('Enter Folder Where The FileS will be moved: - ')  # Enter the destination folder name here
destinationFolder = Path.home() / destinationFolder
def validate():
        if sourceFolder.is_dir() and destinationFolder.is_dir() == True:
                try:
                    for files in os.listdir(sourceFolder):
                        sourceFolderfiles = sourceFolder / files 
                        shutil.copy(sourceFolderfiles,destinationFolder)
                except FileNotFoundError:
                    print('Files Not Found')
def text_files():
        os.chdir(destinationFolder)
        text_files = glob.glob('*.txt')
        if text_files:
            os.mkdir('Text')
            for i in text_files:
                shutil.move(i,'Text')

def video_files():
        os.chdir(destinationFolder)
        video_files = glob.glob('*.mp4')
        video_files2 = glob.glob('*.mkv')
        if video_files or video_files2:
            os.mkdir('Videos')
            for i in video_files:
                shutil.move(i,'Videos')
            for i in video_files2:
                shutil.move(i,'Videos')

def code_files():
        os.chdir(destinationFolder)
        python_files = glob.glob('*.py')
        html_files = glob.glob('*.html')
        css_files = glob.glob('*.css')
        if python_files or html_files or css_files:
            os.mkdir('Code')
            for i in python_files:
                shutil.move(i,"Code")
            for i in html_files:
                shutil.move(i,"Code")
            for i in css_files:
                shutil.move(i,"Code")

def image_files():
        os.chdir(destinationFolder)
        image_files = glob.glob('*.jpg')
        image_files2 = glob.glob('*.png')
        if image_files or image_files2:
            os.mkdir('Images')
            for i in image_files:
                shutil.move(i,'Images')
            for i in image_files2:
                shutil.move(i,'Images')
    
def music_files():
        os.chdir(destinationFolder)
        music_files = glob.glob('*.mp3')
        music_files2 = glob.glob('*.m4a')
        if music_files or music_files2:
            os.mkdir('Music')
            for i in music_files:
                shutil.move(i,'Music')
            for i in music_files2:
                shutil.move(i,'Music')
validate()
text_files()
video_files()
code_files()
image_files()
music_files()
