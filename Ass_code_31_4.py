import sys 
import os
import shutil
from pathlib import Path
import time

def DirectoryFIleCopyExt(Source, Destination,Extention):
   
    Border = "-"*57
    
    timestamp = time.strftime("%Y_%m_%d_%H_%M_%S")
    Filename = "Marvellous" +"_"+timestamp+".log"

    fobj = open(Filename, "w")

    fobj.write(Border+"\n")
    fobj.write("This is a Log File created by Marvellous Automation\n")
    fobj.write("Created at : "+time.strftime("%Y-%m-%d__%H:%M:%S")+"\n")
    fobj.write(Border+"\n")
    
    Ret = False
    Ret = os.path.exists(Source)

    if Ret == False:
        print("Directory Does not exist")
        fobj.close()
        return

    Ret = os.path.isdir(Source)

    if Ret == False:
        print("It is not a Directory")
        fobj.close()
        return
    
    
    os.makedirs(Destination, exist_ok=True)
    fobj.write(f"Created destination directory: {Destination}\n")
    fobj.write(Border+"\n")

   
    for FolderName, SubFolderName, FileName in os.walk(Source):
        for files in FileName:
            src_path = os.path.join(FolderName,files)

            relative = os.path.relpath(src_path,Source)
            dest_path = os.path.join(Destination,relative)
            filepath = Path(files)

            os.makedirs(os.path.dirname(dest_path), exist_ok = True)

            if (not os.path.exists(dest_path)):
                if(filepath.suffix == Extention):
                    shutil.copy2(src_path,dest_path)
                    fobj.write(f"{files} Copied Sucessfully To {Destination} From {Source}\n")

                else:
                    fobj.write(f"Failed to copy {filepath.suffix} file: extension not found in permitted extensions")
                    return
           
            else:
                fobj.write("Unable to Copy as File already exists")
                print("Unable to Copy as File already exists")
                return
    
    print("Files Copied Suceesfully")

    fobj.write("\n"+Border)
    fobj.write(f"\nAll files and folders copied from {Source} to {Destination}\n")
    fobj.write(Border+"\n")
    fobj.close()
    
    print(f"\nAll files copied successfully to {Destination}")

def main():
    Border = "-"*57
    print(Border)
    print("-------------Marvellous Directory Automation-------------")
    print(Border)

    if(len(sys.argv) != 4):
        print("Invalid Number of Arguments")
        print("Please Specify the source and destination directory names")
        return 

    DirectoryFIleCopyExt(sys.argv[1], sys.argv[2],sys.argv[3])

    print(Border)
    print("-------------Marvellous Directory Automation-------------")
    print(Border)


if __name__ == "__main__":
    main()