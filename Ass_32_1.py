import hashlib
import os
import sys
import time

def DisplayChksum(FileName):
    fobj = open(FileName,"rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1024)
    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()

def DirectoryScanner(DirectoryName):
        Border = "-"*57
        timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

        Filename ="Chksum" + timestamp + ".log"
        fobj = open(Filename,"w")
         
        fobj.write(Border+"\n")
        fobj.write("-------------------Marvellous Checksum-------------------"+"\n")
        fobj.write(f"-----------Log Created at :{timestamp}-----------"+"\n")
        fobj.write(Border+"\n")
      
        Res = False
        Res = os.path.exists(DirectoryName)
        if(Res == False):
            fobj.write("Directory does not exist"+"\n")
            return
        
        fobj.write("\t \t \t \t \tChecksum Report\n")
        
        Res = os.path.isdir(DirectoryName)
        if(Res == False):
             fobj.write("It is not a Directory"+"\n")
             return
        
        for FolderName , SubFolder , FileName in os.walk(DirectoryName):
             for fname in FileName:
                  fpath = os.path.join(FolderName,fname)
                  Checksum = DisplayChksum(fname)

                  fobj.write(f"File Name : {fpath} | Check Sum : {Checksum} "+"\n")

        fobj.write(Border+"\n")
        fobj.write("-------------------Marvellous Checksum-------------------"+"\n")
        fobj.write(Border+"\n")
        fobj.close()

def main():
    Border = "-"*57
    print(Border)
    print("-------------------Marvellous Checksum-------------------")
    print(Border)

    if(len(sys.argv) != 2):
        print("Inavlid Number of Arguments ")
        print("Please Specify the name of Directory")
        return 

    DirectoryScanner(sys.argv[1])
    print("Log Report Generated !")

    print(Border)
    print("------------------Marvellous Checksum--------------------")
    print(Border)

if __name__ == "__main__":
     main()