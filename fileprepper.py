
import PIL.Image
from PIL.ExifTags import TAGS
import os


# look at folder contents
#directory = '/Users/Lawrence/Documents/Coding/Python/PyProjects/selfieprocessor/imgs'

#directory = os.path.normpath("./imgs/")

directory = os.path.normpath("./TEST2_selfieimgs18bkp/")
newdirectory = os.path.normpath("./TEST2_selfieimgs18bkp/renamed/")

for filename in os.listdir(directory):
    if filename.endswith(".jpg") or filename.endswith(".JPG") or filename.endswith(".jpeg") or filename.endswith(".JPEG"):
        #f = open(filename)
        #lines = f.read()
        #print (lines[10])
        print (filename)

        img = PIL.Image.open("./TEST2_selfieimgs18bkp/"+filename)
        #img = PIL.Image.open("./imgs/"+filename)
        exif_data = img._getexif()
        #print (exif_data)
        
        for tag, value in exif_data.items(): 
            key = TAGS.get(tag, tag) 
            if key == "DateTimeOriginal": 
                print (key + " " + str(value))
                DTO = str(value)
                #datedots = DTO[0:10]
                datetimeonly = DTO.replace(':','-')
                datetimeonly2 = datetimeonly.replace(' ','_')
                print (datetimeonly2)
            
                datefilename = datetimeonly2 + ".jpg"
                src = filename 
                dst = datefilename 
          
                # rename() function will 
                # rename all the files 
                    
                os.rename(os.path.join(directory,src),os.path.join(newdirectory,dst))

        
        continue

        print ("************NEXT PHOTO*****************")
        print ("***************************************")


# more info for exif data: https://www.programcreek.com/python/example/91518/PIL.ExifTags.TAGS.get


# replace filename with reverse date string - DONE





