
# This file renames and 

import Pillow.Image
from Pillow.ExifTags import TAGS
import os


# gets the metadata and renames the file based on date and time info
def nameFromMeta(photo):
    img = Pillow.Image.open(photo)
    #img = Pillow.Image.open("./imgs/"+filename)
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

            return [src, dst]
        
            # rename() function will 
            # rename all the files 
                
            
# calculate blur value for later comparison
def blurCalc(photo):
    # use this: https://www.pyimagesearch.com/2015/09/07/blur-detection-with-opencv/
    return

# full loop over prepped files
# decides which to keep by maintaining local cache
def photoChoose(photos):
    currentDate = 0 # begins at first photo date
    currentPhotos = []
    timeBlocks = [[]] #blocks of time photos were taken in (minute of the first one)
    lastNoPhoto = 0 #date of last day with no photo

    # [This will keep doing loops, maybe should create proxy array first that I can delete from?]
    for photo in os.listdir(photos):
        # if photo matches currentDate, add to currentPhotos
        # for each of photos
        #   calculate blur value & attach to photo entry (tuple?) currentPhotos.push((photo, blurVal))
        #   if timeBlocks.length === 0 or currentPhotoTime > prev+120secs
        #       create new timeBlock entry with current photo time

        # if photos.length > 1, 
        #   then take latest timeBlock (timeBlocks.length-1)
        #       lowestBlurIndex = 0 #index for current lowest
        #   loop over timeblock
        #       if current photo blurVal > lowestBlurIndex
        #           then set lowestBlurIndex with current
        #   after loop, copy timeBlockPhoto[lowestBlurIndex] photo to an output dir


        # if timeblocks.length > 1 && lastNoPhoto === currentDate-1day.....deals with missing prevday
        #   then take timeBlocks[0]
        #   lowestBlurIndex = 0 #index for current lowest 
        #   loop over timeblock
        #       if current photo blurVal > lowestBlurIndex
        #           then set lowestBlurIndex with current
        #   after loop, copy timeBlockPhoto[lowestBlurIndex] photo to an output dir
        #   clear lastNoPhoto    
        
        # if list is = 0 
        #   then set lastNoPhoto date

        # increase currentDate by 1 day
        # if timeBlocks.length  === 1 OR lastNoPhoto === 0
        #   then clear timeblocks
        

    # if same as prev, add to cache
    # if none the day before
    # do stuff





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

        newName = nameFromMeta(directory+filename)
        os.rename(os.path.join(directory,newName[0]),os.path.join(newdirectory,newName[1]))
        
        continue

        print ("************NEXT PHOTO*****************")
        print ("***************************************")


# more info for exif data: https://www.programcreek.com/python/example/91518/PIL.ExifTags.TAGS.get


# replace filename with reverse date string - DONE


