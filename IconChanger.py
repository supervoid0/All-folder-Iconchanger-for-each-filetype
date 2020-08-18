#!/usr/bin/env python3
import os
import subprocess
import sys
import shlex

def command_execute(folderPath,extType):
    extention= ""
    ext=extention.join(extType)         # extType is a list. convert to string
    pathing=folderPath
    iconFile_for_ext={                  # dictionary to set icon file for each type
        ".mp4":"mp4.ico",
        ".mp3":"mp3.ico",
        ".flac":"flac.ico",
        ".kmz":"kmz.ico",
        ".py":"python.ico",
        ".java":"java.ico",
        ".cpp":"cpp.ico",
        ".pdf":"pdf.ico"}
    iconPath = os.path.join(os.getcwd(),iconFile_for_ext[ext])    #creates icon path to use in cmd
    #list for cmd commands.
    cmds = ['attrib -s -h -r "{}\desktop.ini"'.format(pathing),   #use double quotes for path or error-Parameter format not correct
    'echo [.ShellClassInfo] > "{}\desktop.ini"'.format(pathing),
    'echo IconFile={}>>"{}\desktop.ini"'.format(iconPath,pathing),
    'echo IconIndex=0 >>"{}\desktop.ini"'.format(pathing),
    'attrib +s +h +r "{}\desktop.ini"'.format(pathing),
    'attrib +s +r "{}"'.format(pathing)]
    
    # executes each command in cmds list
    outputs =[]
    for cmd in cmds:                   
        outputs.append(subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell= True).communicate())
    for line in outputs:  # checks result of commands
       print ( line[0].strip())
    

    #command line for linux/Unix= 'os.system("gvfs-set-attribute -t string \""+ os.path.join(os.getcwd(),fileName) +"\" metadata::custom-icon file://\""+os.path.join(os.path.join(os.getcwd(),fileName),fileName)+"\"")'

    #Cmd Commands for windows = 
    #Set DriveLetter=C    
    #Set Pathing=test    
    #Set IconPath=users\username\desktop\icon.ico    
    #attrib -s -h -r %DriveLetter%:\%Pathing%\desktop.ini    
    #echo [.ShellClassInfo] >%DriveLetter%:\%Pathing%\desktop.ini    
    #echo IconFile=%DriveLetter%:\%IconPath%>>%DriveLetter%:\%Pathing%\desktop.ini    
    #echo IconIndex=0 >>%DriveLetter%:\%Pathing%\desktop.ini    
    #attrib +s +h +r %DriveLetter%:%Pathing%\desktop.ini    
    #attrib +s +r %DriveLetter%:\%Pathing%    
    #pause 

def change_icon(folder_path, fileList):
    Filetype= [".mp4",".flac",".kmz",".mp3"]                #filetype we need
    extList=[]
    for file in fileList:                                   #iterate all files in that folder
        filepath= os.path.join(folder_path,file)
        ext = os.path.splitext(filepath)[-1].lower()        #extract the extenstion name
        extList.append(ext)                                 #create extension list
    
    #check common extensions of fileList and Filetype list
    Filetype_set= set(Filetype)
    matched_ext= list(Filetype_set.intersection(extList))
    
    if len(matched_ext)==1:  #currently working with one type of file exists in a folder.
        command_execute(folder_path, matched_ext) #send working directory(folder),extention to execute in cmd 

def Main():
    rootdir = os.getcwd()
    # Iterate over folders, subfolders and files
    for subdir, dirs, files in os.walk(rootdir):
        change_icon(subdir,files) # This function takes each subfolders and corresponding files to examine

Main()