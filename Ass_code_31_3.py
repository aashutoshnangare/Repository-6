import sys 
import os
import shutil

def DirectoryFIleCopy(Source, Destination):
   
    Border = "-"*57

    fobj = open("Marvellous.log", "w")

    fobj.write(Border+"\n")
    fobj.write("This is a Log File created by Marvellous Automation\n")
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

            os.makedirs(os.path.dirname(dest_path), exist_ok = True)

            if (not os.path.exists(dest_path)):
                shutil.copy2(src_path,dest_path)
                fobj.write(f"{files} Copied Sucessfully To {Destination} From {Source}\n")
                           
            else:
                fobj.write("Unable to Copy as File already exists")
                print("Unable to Copy as File already exists")
    
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

    if(len(sys.argv) != 3):
        print("Invalid Number of Arguments")
        print("Please Specify the source and destination directory names")
        return 

    DirectoryFIleCopy(sys.argv[1], sys.argv[2])

    print(Border)
    print("-------------Marvellous Directory Automation-------------")
    print(Border)


if __name__ == "__main__":
    main()