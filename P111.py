import os 
import shutil

os.getcwd()
os.mkdir("images")

path="C:/Users/18nam/Desktop/f4.pptx"
root,extention=os.path.splitext(path)
print('The root elements are ', root)
print('The extension is ', extention)


source="C:/Users/18nam/Desktop/f1.pptx"
destination="C:/Users/18nam/Desktop/f2.pptx"
dest=shutil.copy(source,destination)
print('After copying the file')

