#!/usr/bin/python
########################################################
########################################################
##              Script Description                    ##
##                                                    ##
##      Script developed for convert hex files to     ##
##		image (JPG) files		 			          ##
##      Developer:      Junior de Oliveira            ##
##      Date:           19/04/2018                    ##
##      Version:        1.1804.19                     ##
##                                                    ##
##                                                    ##
##                                                    ##
########################################################
########################################################

import binascii
import subprocess
import shlex
import sys

def usage():
    print("Usage mode: " + sys.argv[0] + " folder ext nameList scriptName")
    print("Example: " + sys.argv[0] + " /home/folder jpg listName scriptName")

hexFile = open("arqHex", "r")
fileName = 0

if len(sys.argv) < 4:
    usage()
else:
    folder      = sys.argv[1] # folder de onde esta os arquivos
    ext         = sys.argv[2] # extensao dos arquivos a serem renomeados
    nameList    = sys.argv[3] # lista de nomes que serao usados para renomear os arquivos
    script      = sys.argv[4] # nome do script a ser executado

    newHexFile = hexFile.readlines()
    for hexFileLine in newHexFile:
        if len(str(fileName)) == 1:
            arq = open("000"+str(fileName)+".txt", "w")
        elif len(str(fileName)) == 2:
            arq = open("00"+str(fileName)+".txt", "w")
        elif len(str(fileName)) == 3:
            arq = open("0"+str(fileName)+".txt", "w")
        elif len(str(fileName)) == 4:
            arq = open(str(fileName)+".txt", "w")
        #arq = open(str(fileName)+".txt", "w")
        arq.writelines(hexFileLine)
        arq.close()

        if len(str(fileName)) == 1:
            arq = open("000"+str(fileName)+".txt", "r")
            img = open("000"+str(fileName)+".jpg", "wb")
        elif len(str(fileName)) == 2:
            arq = open("00"+str(fileName)+".txt", "r")
            img = open("00"+str(fileName)+".jpg", "wb")
        elif len(str(fileName)) == 3:
            arq = open("0"+str(fileName)+".txt", "r")
            img = open("0"+str(fileName)+".jpg", "wb")
        elif len(str(fileName)) == 3:
            arq = open(str(fileName)+".txt", "r")
            img = open(str(fileName)+".jpg", "wb")
        while 1:
            hexFileLine = arq.readline()
            newHexFileLine = hexFileLine.strip()
            if not hexFileLine:
                break
            img.write(binascii.a2b_hex(newHexFileLine))

            # Close the file
        img.close()
        arq.close()
        fileName += 1

    subprocess.call(shlex.split("./"+script + " " + folder +" " + ext + " " + nameList))
