import os

# Function to extract name
def img_name(filename):
    img = filename.split('.')[0]
    return img

# Function to extract extention (Alternative filename.endswith(".txt") will extract text files)
def ext_name(filename):
    ext = filename.split('.')[1]
    return ext
        
# Rename heic to jpg
def heic_to_jpg(filename):
    new_filename = img_name(filename) + '.jpeg'
    os.rename(filename, new_filename)
    return new_filename

count = 1
# Traverse the dir for files
for file in os.listdir(os.getcwd()):
    # Extract only files and not directory
    if os.path.isfile(file):
        # Extract only a particular extention
        if file.endswith(".jpg"):
            print("Old file name:",file)
            print("New file name:",heic_to_jpg(file))
            print(f"{count} file renamed successfully")
            print("-------------------------------------------")
            count+=1