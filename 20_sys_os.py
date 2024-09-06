import sys
import os

def sys_trial():
    # print(type(sys.argv), len(sys.argv))
    # if len(sys.argv) != 5:
    #     print("Incorrect no. of arguments.")
    #     return
    
    # for arg in sys.argv:
    #     print(f"{arg=}")

    print(sys.path)
    sys.path.insert(0, "..\\")
    print(sys.path)

    print(sys.version)


def os_trial():
    print(os.getcwd())
    curr_dir = os.getcwd()

    newFolder = os.path.join(curr_dir, "new_dir")
    print(newFolder)

    if os.path.exists(newFolder):
        print("Folder exists")
    else:
        print("Not present")
        os.mkdir(newFolder)
    
    newFile = os.path.join(newFolder, "new_file.txt")

    if os.path.exists(newFile):
        print("File exists")
    else:
        print("Not present")

        # fileObj = open(newFile, mode="w")
        # fileObj.write("This is a test text.")
        # fileObj.close()

        with open(newFile, mode="w") as fileObj:
            fileObj.write("This is a test text.")

    if os.path.exists(newFile):
        with open(newFile) as fileObj:
            print("File contents are:", fileObj.read(7))
            pos = fileObj.tell()
            print("Position of cursor:", pos)
            # fileObj.seek(5)
            fileObj.seek(2)
            pos = fileObj.tell()
            print("Position of cursor:", pos)
            print(fileObj.read())
        os.remove(newFile)

    # ?? - FileName length restrictions??
    '''
        read()
        read(n)       --> Safer
        readline()
        readlines()   --> list of lines; till the end of file
        readlines(n)  --> Safer
        write(data)
        writeline()  -> Not available
        writelines(coll_str)  
    '''
    if os.path.exists(newFolder):
        os.rmdir(newFolder)


os_trial()