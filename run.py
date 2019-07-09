from PIL import Image
import os, glob, sys

def offset(side):
    try:
        print("\nHow many pixels should be removed from the " + side + " side of each image in this directory?")
        px = int(input("Please type the desired number of pixels, in integer form. Then press ENTER!\n"))
        return px
    except:
        return False

def start():
    sides = ["top", "bottom", "left", "right"]
    pixels = {"top":0,"bottom":0,"left":0,"right":0}
    for side in sides:
        px = False
        while px is False:
            px = offset(side)
        pixels[side] = px

    input("Press any key to start trimming, or close out to cancel.\nEvery png, jpg/jpeg, and gif file in the current directory of this python file will be trimmed!")
    trim(pixels)
    print("\r\n")
    print("Thank you for using BulkPhotoTrim v0.0.1 - WUBUR LLC - WILLIAM PASSMORE")
    print("https://github.com/NerdiOrg/bulk-photo-trim")

def trim(pixels):
    searchdir = "./" # end in slash!
    os.chdir(searchdir) # this directory
    savepath = searchdir + "trims" # single folder, do not include end slash!

    if not os.path.exists(savepath):
        try:
            os.mkdir(savepath)
        except:
            exit("Fatal Error: Could not create or find the file save path: " + savepath)

    types = ("png", "jpg", "jpeg", "gif")
    for type in types:
        for file in glob.glob("*."+type):
            img = Image.open(file) # open the img
            original_width, original_height = img.size # dimensions of the img
            if(original_width < (pixels["left"] + pixels["right"])):
                print("The file '"+file+"' is not large enough in width to support the desired trim dimensions.")
                continue
            if(original_height < (pixels["top"] + pixels["bottom"])):
                print("The file '"+file+"' is not large enough in height to support the desired trim dimensions.")
                continue
            print("Trimming in Progress: " +file)
            savepathfile = savepath + "/" + file
            img = img.crop((pixels["left"], pixels["top"], original_width - pixels["right"], original_height - pixels["bottom"]))
            img.save(savepathfile, "PNG")

start()
