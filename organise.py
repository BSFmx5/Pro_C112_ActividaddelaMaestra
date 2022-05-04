import os
import shutil

# .exe , .msi,  .gif, .png .jpg, .jpeg, .csv, .pdf , .xls , .xlsx , .ppt , .pptx

from_dir = "C:/Users/ADMIN/Downloads"
to_dir = "C:/WhiteHatJr/dowanloadedimages"

list_of_files = os.listdir(from_dir)
#print(list_of_files)

# Mueve todas las imagenes  descargadas de una carpeta a otra
for file_name in list_of_files:

    name, extension = os.path.splitext(file_name)
    #print(name)
    #print(extension)

    if extension == '':
        continue
    if extension in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:

        path1 = from_dir + '/' + file_name                       # Ejemplo path1 : Downloads/ImageName1.jpg        
        path2 = to_dir + '/' + "Image_Files"                     # Ejemplo path2 : D:/My Files/Image_Files      
        path3 = to_dir + '/' + "Image_Files" + '/' + file_name   # Ejemplo path3 : D:/My Files/Image_Files/ImageName1.jpg
        #print("path1 " , path1)
        #print("path3 ", path3)

        # Verifica la carpeta/Directorio ruta existente antes de moverlo
        # También crea una nueva carpeta/Directorio luego muevelo
        if os.path.exists(path2):
          print("Moving " + file_name + ".....")

          # Mueve de path1 ---> path3
          shutil.move(path1, path3)

        else:
          os.makedirs(path2)
          print("Moving " + file_name + ".....")
          shutil.move(path1, path3)
