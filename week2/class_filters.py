# Girls Who Code SIP 2019
# Walmart San Bruno
# CLASS FILTER LIBRARY
# ========================== #
# Instructor: Nikki Kyllonen
# TA: Erika Badalyan
# Students:
# Brisa		Garnica
# Leela		Aji
# Tiffany	Mok
# Luciann	Nguyen
# Marina	Wong
# Shania	Hao
# Zafina	Ameen
# Jade		Nguyen
# Shreya	Holikatti
# Gargi		Deshpande
# Sophia	Clemente
# Ava		Rebollido
# Eshani	Jha
# Ishani	Singh
# Cailey	Murad
# Yojita	Sharma
# Mia		Orr
# Alexandra	Zhang
# Claire	Min
# Shreshta	Ranganathan
# Helin		Yilmaz

# import statements
import math
from PIL import Image

# ---------- AVA'S FILTERS ---------- #
def obamicon_ava(image):
	 new_pixels = []

# OG COLORS
    #2. store possible colors
    #darkBlue = (0,51, 76)
    #red = (217, 26, 33)
    #lightBlue = (112, 150, 158)
    #yellow = (252, 227, 166)

# MY FILTER COLORS
    blue = (0, 0, 128)
    rose = (255, 228, 225)
    red = (255, 0, 0)
    violet = (148,0, 211)

    #3. create a new image of the same size
    filtered_image = Image.new("RGB", (500, 335))
    filter_data = list(image.getdata())
    for pixel in filter_data:
        intensity = sum_list(pixel)
        new_pixel = (0,0,0)

# MY FILTER COLORS
        if intensity < 182:
            new_pixel = blue
        if intensity > 546:
            new_pixel = rose
        if intensity > 182 and intensity < 346:
            new_pixel = red
        if intensity > 346 and intensity < 546:
            new_pixel = violet

# OG COLORS
    #    if intensity < 182:
    #        new_pixel = darkBlue
    #    if intensity > 546:
    #        new_pixel = yellow
    #    if intensity > 182 and intensity < 346:
    #        new_pixel = red
    #    if intensity > 346 and intensity < 546:
    #        new_pixel = lightBlue

        new_pixels.append(new_pixel)
    filtered_image.putdata(new_pixels)

    # when we're done, return the new image
    return filtered_image

def sum_list(alist):
    total = 0
    for value in alist:
        total += value
    return total

# ---------- CLAIRE'S FILTERS ---------- #
def pastel_claire(imageobject):

    #    low = (0, 51, 76)
    low = (227, 197, 219) #lightpink
    #    medium_low = (217, 26, 33)
    medium_low = (196, 197, 242) #darkblue
    #    medium_high = (112, 150, 158)
    medium_high = (242, 220, 240) #pink
    #    high = (252, 227, 166)
    high = (220, 237, 242) #seafoam

    original_pixels = imageobject.getdata()
    new_pixels = []

    for p in original_pixels:
        # calculate the sum
        intensity = sum(p)

        if intensity < 185:
            new_pixels.append(low)
        elif 185 <= intensity and intensity < 423:
            new_pixels.append(medium_low)
        elif 423 <= intensity and intensity < 530:
            new_pixels.append(medium_high)
        else:
            new_pixels.append(high)

        # new_pixels.append[p]

    w = imageobject.width
    h = imageobject.height
    filtered_image = Image.new("RGB", (w,h))
    filtered_image.putdata(new_pixels)
    return filtered_image

# ---------- GARGI'S FILTERS ---------- #
def obamicon_gargi(imageObject):
    w = imageObject.width
    h = imageObject.height
    darkBlue = (0, 51, 76)
    red = (217, 26, 33)
    lightBlue = (112, 150, 158)
    yellow = (252, 227, 166)

    filteredImage = Image.new("RGB", (w, h))
    newPixels = []

    for y in range(h):
        for x in range(w):
            pixelValues = imageObject.getpixel((x, y))
            sum = 0
            for i in range(len(pixelValues)):
                sum += pixelValues[i]

            if (sum < 182):
                newPixels.append(darkBlue)
            elif (sum >= 182 and sum < 364):
                newPixels.append(red)
            elif (sum >= 364 and sum < 546):
                newPixels.append(lightBlue)
            else:
                newPixels.append(yellow)

    filteredImage.putdata(newPixels)
    return filteredImage

def blackWhite_gargi(imageObject):
    w = imageObject.width
    h = imageObject.height

    filteredImage = Image.new("RGB", (w, h))
    newPixels = []

    for y in range(h):
        for x in range(w):
            pixelValues = imageObject.getpixel((x, y))
            sum = 0
            for i in range(len(pixelValues)):
                sum += pixelValues[i]
            avg = int(sum / len(pixelValues))
            newPixels.append((avg, avg, avg))

    filteredImage.putdata(newPixels)
    return filteredImage

def inverse_gargi(imageObject):
    w = imageObject.width
    h = imageObject.height

    filteredImage = Image.new("RGB", (w, h))
    newPixels = []

    for y in range(h):
        for x in range(w):
            pixelValues = imageObject.getpixel((x, y))
            inverseValues = [0, 0, 0]
            for i in range(len(pixelValues)):
                inverseValues[i] = 255 - pixelValues[i]
            inverseValues = tuple(inverseValues)
            newPixels.append(inverseValues)

    filteredImage.putdata(newPixels)
    return filteredImage

def brighten_gargi(imageObject):
    w = imageObject.width
    h = imageObject.height
    filterScale = 25

    filteredImage = Image.new("RGB", (w, h))
    newPixels = []

    for y in range(h):
        for x in range(w):
            pixelValues = imageObject.getpixel((x, y))
            brightValues = [0, 0, 0]
            # RBG --> R = tuple[0], G = tuple[1], B = tuple[2]
            for i in range(len(pixelValues)):
                if (pixelValues[i] + filterScale <= 255):
                    brightValues[i] = pixelValues[i] + filterScale
                else:
                    brightValues[i] = 255
            brightValues = tuple(satValues)
            newPixels.append(brightValues)

    filteredImage.putdata(newPixels)
    return filteredImage

def purpleTint_gargi(imageObject):
    w = imageObject.width
    h = imageObject.height
    tintIntensity = 50

    filteredImage = Image.new("RGB", (w, h))
    newPixels = []

    for y in range(h):
        for x in range(w):
            pixelValues = imageObject.getpixel((x, y))
            tintedValues = [0, 0, 0]
            # RBG --> R = tuple[0], G = tuple[1], B = tuple[2]
            if (pixelValues[0] <= 255 - tintIntensity):
                tintedValues[0] = pixelValues[0] + tintIntensity
            else:
                tintedValues[0] = 255

            if (pixelValues[2] <= 255 - tintIntensity):
                tintedValues[2] = pixelValues[2] + tintIntensity
            else:
                tintedValues[2] = 255

            # if (pixelValues[2] >= tintIntensity):
            #     tintedValues[2] = pixelValues[2] - tintIntensity
            # else:
            #     tintedValues[2] = 0
            tintedValues[1] = pixelValues[1]
            tintedValues = tuple(tintedValues)
            newPixels.append(tintedValues)

    filteredImage.putdata(newPixels)
    return filteredImage

# ---------- HELIN'S FILTERS ---------- #
def helin_filter1(im):
    pixels = im.getdata() #method
    new_pixels = [] #empty list/string to build on

    lightred = (255,153,153)
    pink= (255,204,229)
    lightblue=(102,178,255)
    lightpurple = (204,153,255)

    for p in pixels:
        intensity = p[0] + p[1] + p[2] #adding three values in each list of colors

        if intensity < 182:
            new_pixels.append(lightred)

        elif intensity >= 182 and intensity < 364:
            new_pixels.append(pink)

        elif intensity >= 364 and intensity < 546:
            new_pixels.append(lightblue)

        elif intensity >= 546:
            new_pixels.append(lightpurple)

    newim = Image.new("RGB", im.size)
    newim.putdata(new_pixels)
    return newim

def helin_filter2(im):
    pixels = im.getdata() #method
    new_pixels = [] #empty list/string to build on

    lightred = (0,102,102)
    pink= (0,51,26)
    lightblue=(153,77,0)
    lightpurple = (51,102,0)

    for p in pixels:
        intensity = p[0] + p[1] + p[2] #adding three values in each list of colors

        if intensity < 182:
            new_pixels.append(lightred)

        elif intensity >= 182 and intensity < 364:
            new_pixels.append(pink)

        elif intensity >= 364 and intensity < 546:
            new_pixels.append(lightblue)

        elif intensity >= 546:
            new_pixels.append(lightpurple)

    newim = Image.new("RGB", im.size)
    newim.putdata(new_pixels)
    return newim

def helin_filter3(im):
    pixels = im.getdata() #method
    new_pixels = [] #empty list/string to build on

    lightred = (255,204,204)
    pink= (255,0,127)
    lightblue=(0,128,255)
    lightpurple = (178,102,255)

    for p in pixels:
        intensity = p[0] + p[1] + p[2] #adding three values in each list of colors

        if intensity < 182:
            new_pixels.append(lightred)

        elif intensity >= 182 and intensity < 364:
            new_pixels.append(pink)

        elif intensity >= 364 and intensity < 546:
            new_pixels.append(lightblue)

        elif intensity >= 546:
            new_pixels.append(lightpurple)

    newim = Image.new("RGB", im.size)
    newim.putdata(new_pixels)
    return newim

def helin_filter4(im):
    pixels = im.getdata() #method
    new_pixels = [] #empty list/string to build on

    yellow = (255,255,102)
    pink= (255,0,127)
    green=(102,255,102)
    lightpurple = (178,102,255)

    for p in pixels:
        intensity = p[0] + p[1] + p[2] #adding three values in each list of colors

        if intensity < 182:
            new_pixels.append(green)

        elif intensity >= 182 and intensity < 364:
            new_pixels.append(lightpurple)

        elif intensity >= 364 and intensity < 546:
            new_pixels.append(pink)

        elif intensity >= 546:
            new_pixels.append(yellow)

    newim = Image.new("RGB", im.size)
    newim.putdata(new_pixels)
    return newim

def helin_filter5(im): 
    pixels = im.getdata() #method
    new_pixels = [] #empty list/string to build on

    yellow = (26,170,255)
    pink= (160,255,0)
    green=(0,0,135)
    lightpurple = (255,102,255)

    for p in pixels:
        intensity = p[0] + p[1] + p[2] #adding three values in each list of colors

        if intensity < 182:
            new_pixels.append(green)

        elif intensity >= 182 and intensity < 364:
            new_pixels.append(lightpurple)

        elif intensity >= 364 and intensity < 546:
            new_pixels.append(pink)

        elif intensity >= 546:
            new_pixels.append(yellow)

    newim = Image.new("RGB", im.size)
    newim.putdata(new_pixels)
    return newim

def helin_filter6(im): #black and white
    pixels = im.getdata() #method
    new_pixels = [] #empty list/string to build on

    yellow = (0,0,0)
    pink= (255,255,255)
    green=(0,0,0)
    lightpurple = (255,255,255)

    for p in pixels:
        intensity = p[0] + p[1] + p[2] #adding three values in each list of colors

        if intensity < 182:
            new_pixels.append(green)

        elif intensity >= 182 and intensity < 364:
            new_pixels.append(lightpurple)

        elif intensity >= 364 and intensity < 546:
            new_pixels.append(pink)

        elif intensity >= 546:
            new_pixels.append(yellow)

    newim = Image.new("RGB", im.size)
    newim.putdata(new_pixels)
    return newim

# ---------- MIA'S FILTERS ---------- #
def obamicon_mia(imageobject):
    w =imageobject.width
    h =imageobject.height

    pixels = imageobject.getdata()
    new_pixels = []

    newim = Image.new("RGB", (w,h))

    for p in pixels:
        lightred = (255, 153, 153)
        lightorange = (255, 229, 204)
        light_blue = (219, 229, 230)
        lighterblue = (204, 255, 255)

        intensity = p[0] + p[1] + p[2]
        if intensity < 182:
            new_pixels.append(lightred)
        elif intensity >= 182 and intensity < 364:
            new_pixels.append(lightorange)
        elif intensity >= 364 and intensity < 546:
            new_pixels.append(lighterblue)
        elif intensity >= 546:
            new_pixels.append(light_blue)


    newim.putdata(new_pixels)
    return newim

# ---------- SHREYA'S FILTERS ---------- #
def shreya_filter1(im):

    pixels = im.getdata()
    new_pixels = [] #empty list to add values of different colors

    lightRed = (255, 153, 153)
    pink = (255, 204, 229)
    lightBlue = (102, 178, 255)
    lightPurple = (204, 153, 255)

    for p in pixels:
        intensity = p[0] + p[1] + p[2]

        if intensity < 182:
            new_pixels.append(lightRed)

        elif intensity >= 182 and intensity < 364:
            new_pixels.append(pink)

        elif intensity >= 364 and intensity < 546:
            new_pixels.append(lightBlue)

        elif intensity >= 546:
            new_pixels.append(lightPurple)

    newim = Image.new("RGB", im.size)
    newim.putdata(new_pixels)
    return newim



def shreya_filter2(im):

    pixels = im.getdata()
    new_pixels = [] #empty list to add values of different colors

    red = (153, 0, 0)
    pink = (153, 0, 76)
    blue = (0, 76, 153)
    purple = (76, 0, 153)

    for p in pixels:
        intensity = p[0] + p[1] + p[2]

        if intensity < 182:
            new_pixels.append(red)

        elif intensity >= 182 and intensity < 364:
            new_pixels.append(pink)

        elif intensity >= 364 and intensity < 546:
            new_pixels.append(blue)

        elif intensity >= 546:
            new_pixels.append(purple)

    newim = Image.new("RGB", im.size)
    newim.putdata(new_pixels)
    return newim




def shreya_filter3(im):

    pixels = im.getdata()
    new_pixels = [] #empty list to add values of different colors

    red = (255, 51, 51)
    pink = (255, 51, 153)
    blue = (51, 153, 255)
    purple = (153, 51, 255)

    for p in pixels:
        intensity = p[0] + p[1] + p[2]

        if intensity < 182:
            new_pixels.append(red)

        elif intensity >= 182 and intensity < 364:
            new_pixels.append(pink)

        elif intensity >= 364 and intensity < 546:
            new_pixels.append(blue)

        elif intensity >= 546:
            new_pixels.append(purple)

    newim = Image.new("RGB", im.size)
    newim.putdata(new_pixels)
    return newim


def shreya_filter4(im):

    pixels = im.getdata()
    new_pixels = [] #empty list to add values of different colors

    red = (0, 0, 0)
    pink = (255, 255, 255)
    blue = (0, 0, 0)
    purple = (255, 255, 255)

    for p in pixels:
        intensity = p[0] + p[1] + p[2]

        if intensity < 182:
            new_pixels.append(red)

        elif intensity >= 182 and intensity < 364:
            new_pixels.append(pink)

        elif intensity >= 364 and intensity < 546:
            new_pixels.append(blue)

        elif intensity >= 546:
            new_pixels.append(purple)

    newim = Image.new("RGB", im.size)
    newim.putdata(new_pixels)
    return newim

# ---------- LUCIANN'S FILTERS ---------- #
def obamicon_luciann(im):

    pixels = im.getdata()

    new_pixels = []

    darkBlue = (0, 51, 76)
    red = (217, 26, 33)
    lightBlue = (61, 229, 255)
    yellow = (242,255,0)
    green = (113,255,61)
    orange = (255, 126, 61)
    pink = (255,61,242)
    for p in pixels:
        intensity = p[0] + p[1] + p[2]

        if intensity < 182:
            new_pixels.append(pink)

        elif intensity >= 182 and intensity < 364:
            new_pixels.append(red)
        elif intensity >= 182 and intensity < 364:
            new_pixels.append(darkBlue)


        elif intensity  >= 364  and intensity < 546:
            new_pixels.append(lightBlue)
        elif intensity  >= 364  and intensity < 546:
            new_pixels.append(green)
        elif intensity  >= 364  and intensity < 546:
            new_pixels.append(orange)

        elif intensity >= 546:
            new_pixels.append(yellow)


    newim = Image.new("RGB", im.size)
    newim.putdata(new_pixels)
    return newim

# ---------- MARINA'S FILTERS ---------- #
def obamicon_marina(imageobject):
#get images width and height attributions

    new_pixels = []


    black= (32,32,32)
    gray= (96,96,96)
    grey= (160,160,160)#612
    lightGray= (224,224,224) #459

#create new image of same size
    filtered_image = Image.new("RGB", (728, 400))
    filter_data = list(imageobject.getdata()) #turns the data from a sequence into a list
    for pixel in filter_data: #pixel: can put any variable and computer will recognize that the list in "filter_data" consists of tuples and will do the commands in the function body through each tuple.
        intensity = sum_list(pixel) #it will fufill the command of "sum_list" for the varibel "pixel"
        new_pixel = (0,0,0)

        if intensity < 50:
            new_pixel = black
        if intensity > 50 and intensity < 145:
            new_pixel = gray
        if intensity > 145 and intensity < 152:
            new_pixel = grey
        if intensity > 152 and intensity < 306:
            new_pixel = lightGray

        new_pixels.append(new_pixel)
    filtered_image.putdata(new_pixels)
    return filtered_image

# ---------- LEELA'S FILTERS ---------- #
def leelafilter(im):
    pixels = im.getdata()


    #filter the pixels
    new_pixels = []

    magenta = (204, 0, 102)
    mustard = (204, 204, 0)
    robinegg = (51, 153, 255)
    violet = (255, 0, 255)

    for p in pixels:
        intensity = p[0] + p[1] + p[2]

        if intensity < 182:
            new_pixels.append(magenta)

        elif intensity >= 182 and intensity < 364:
            new_pixels.append(mustard)

        elif intensity >= 364 and intensity < 546:
            new_pixels.append(robinegg)

        elif intensity >= 546:
            new_pixels.append(violet)

    newim = Image.new("RGB", im.size)
    newim.putdata(new_pixels)

    return newim

# ---------- SHRESHTA'S FILTERS ---------- #
def shreshta(im):
  # Load the pixel data from im.
  pixels = im.getdata()
  # Create a list to hold the new image pixel data.
  new_pixels = []

  # Define color constants to use for recoloring.
  yellow = (224, 211, 22)
  pink = (217, 132, 183)
  orange1 = (222, 132, 22)
  white = (252, 242, 242)

  # Process the pixels in the image.
  for p in pixels:
    # Pixel intensity = R value + G value + B value
    intensity = p[0] + p[1] + p[2]

    if intensity < 182:
      new_pixels.append(white)

    elif intensity >= 182 and intensity < 364:
      new_pixels.append(yellow)

    elif intensity >= 364 and intensity < 564:
        new_pixels.append(pink)

    elif intensity >=546:
      new_pixels.append(orange1)

  # Save the filtered pixels as a new image
  newim = Image.new("RGB", im.size)
  newim.putdata(new_pixels)
  return newim

# ---------- CAILEY'S FILTERS ---------- #
def obamicon_cailey(im):
    pixels = im.getdata()
    new_pixels = [] #empty list to combine color values
    darkBlue = (0,51,76)
    red = (217,26,33)
    lightBlue = (112,150,158)
    yellow = (252,227,166)

    for p in pixels:
        intensity = p[0] + p[1] + p[2]

        if intensity < 182:
            new_pixels.append(darkBlue)

        elif intensity >= 182 and intensity <= 364:
            new_pixels.append(red)

        elif intensity >= 364 and intensity <= 546:
            new_pixels.append(lightBlue)

        elif intensity >= 546:
            new_pixels.append(yellow)

    newim = Image.new("RGB", im.size)
    newim.putdata(new_pixels)
    return newim

# ---------- YOJITA'S FILTERS ---------- #
def yojita_grey(im):

    pixels = im.getdata()
    new_pixels = []
    #color_intensity = (255, 100, 255)
    color_intensity = []
    color_r = int(input("What is the red value?: "))
    color_g = int(input("What is the green value?: "))
    color_b = int(input("What is the blue value?: "))
    color_intensity.append(color_r)
    color_intensity.append(color_g)
    color_intensity.append(color_b)

    for p in pixels:
        intensity_x = (color_r - p[0])**2
        intensity_y = (color_g - p[1])**2
        intensity_z = (color_b - p[2])**2
        red = p[0]
        green = p[1]
        blue = p[2]
        closeness = math.sqrt(intensity_x + intensity_y + intensity_z)
        if int(closeness) < 130:
            new_pixels.append(tuple(color_intensity))
        else:
            avg = int((red + green + blue)/3)
            new_intensity = (avg, avg, avg)
            new_pixels.append(new_intensity)
    newim = Image.new("RGB", im.size)
    newim.putdata(new_pixels)
    return newim

# ---------- ISHANI'S FILTERS ---------- #
def ishani(im):
    pixels = im.getdata()
    new_pixels = []

    red = (255,0,0)
    orange = (255, 86, 0)
    yellow = (255, 220, 0)
    green = (102, 255, 0)
    blue = (0,180,255)
    purple = (216, 0, 255)
    black=(0,0,0)


    for p in pixels:
        intensity = p[0] + p[1] + p[2]

        if intensity < 123:
            new_pixels.append(black)
        elif intensity >= 123 and intensity <264:
            new_pixels.append(green)
        elif intensity >= 264 and intensity < 311:
            new_pixels.append(yellow)
        elif intensity >= 311 and intensity < 405:
            new_pixels.append(blue)
        elif intensity >= 405 and intensity < 499:
            new_pixels.append(orange)
        elif intensity >= 499 and intensity <546:
            new_pixels.append(purple)
        elif intensity >=546:
            new_pixels.append(red)


    newim = Image.new("RGB", im.size)
    newim.putdata(new_pixels)
    return newim

# ---------- TIFFANY'S FILTERS ---------- #
def obamicon_tiffany(imageobject):
    # number 1-> get this image's width and height attributes
    w = imageobject.width
    h = imageobject.height

    #number 2 -> create a new image of the same size

    #darkBlue = (0, 51, 76)
    #red = (217, 26, 33)
    #lightBlue = (112, 150, 158)
    #yellow = (252, 227, 166)

    yellow = (255, 255, 0)
    darkTurquoise = (0, 206, 209)
    rosyBrown = (188, 143, 143)
    darkGoldenrod = (184, 134, 11)

    #filter the pixels!
    pixels = imageobject.getdata()
    new_pixels = []

#for p in pixels:
#intensity = get sum of (0, 1 , 2)
    for p in pixels:
        intensity = p[0] + p[1] + p[2]

        if intensity < 182:
            new_pixels.append(yellow)
        elif 182 <= intensity and intensity < 364:
            new_pixels.append(darkTurquoise)
        elif 364 <= intensity and intensity < 546:
            new_pixels.append(rosyBrown)
        else:
            new_pixels.append(darkGoldenrod)

    #put pixel color in filtered image

    filtered_image = Image.new("RGB", (w,h))
    filtered_image.putdata(new_pixels)
    #when we're done, return the new image
    return filtered_image

# ---------- JADE'S FILTERS ---------- #
def obamicon(im):
    pixels = im.getdata()
    new_pixels = [ ]

    darkBlue = (0,51,76)
    red = (217, 26, 33)
    lightBlue = (112, 150, 158)
    yellow = (252, 227, 166)

    for p in pixels:
        intensity = p[0] + p[1] + p[2]



        if intensity < 182:
            new_pixels.append(darkBlue)

        elif intensity >= 182 and intensity < 364:
            new_pixels.append(red)

        elif intensity >= 364 and intensity < 546:
            new_pixels.append(lightBlue)

        elif intensity >= 546:
            new_pixels.append(yellow)

    newim = Image.new("RGB", im.size)
    newim.putdata(new_pixels)
    return newim

# ---------- SHANIA'S FILTERS ---------- #
def shaniacon(im):

    pixels = im.getdata()
    new_pixels = [ ]

    g = (166,153,155)
    g1 = (150,137,140)
    g2 = (188,167,171)
    g3 = (191,163,168)
    g4 = (143,123,127)

    for p in pixels:
        intensity = p[0] + p [1] + p[2]

        if intensity < 76:
            new_pixels.append(g)

        elif intensity >= 76 and intensity < 148:
            new_pixels.append(g1)

        elif intensity >= 148 and intensity < 213:
            new_pixels.append(g2)

        elif intensity >= 213 and intensity < 269:
            new_pixels.append(g3)

        elif intensity >= 269 and intensity < 324:
            new_pixels.append(g4)

        elif intensity >= 324 and intensity < 397:
            new_pixels.append(g)

        elif intensity >= 397 and intensity < 434:
            new_pixels.append(g1)

        elif intensity >= 434 and intensity < 497:
            new_pixels.append(g2)

        elif intensity >= 497 and intensity < 546:
            new_pixels.append(g3)

        elif intensity >= 546:
            new_pixels.append(g4)

    newim = Image.new("RGB", im.size)
    newim.putdata(new_pixels)
    return newim

# ---------- ALEX'S FILTERS ---------- #
#Apply emphasize a color filter in the image
###INSTRUCTIONS
    #For this program you need to input your own RGB VALUE that you want to emphasize

    # For example, you could do this:
    # color = input("What color do you want to emphasize? ")
    # color_list = color.split(',')
    # target_color =  [int(value) for value in color_list]
    #
    # filtered = filters.emphasize_yellow(myimage, target_color)

    #There is another function inside the emphasize function to grayscale the pixels you dont want to emphasize


def emphasize_alex(img_obj, target):
    #get original image's width and height attributes
    w = img_obj.width
    h = img_obj.height

    #create a new empty image of the same size
    filtered_img = Image.new("RGB", (w,h))

    ###########filter the pixels##############
    new_pixels = [] #new list to store the new pixels
    distance_desired = 130 #how far away from the desired color pixel should the program tolerate

    pixels = img_obj.getdata() #get a list of tuples with rgb values

    for pixel in pixels: #go thro one pixel at a time and do the following for every of them
        difference = 0 #reset intensity
        sum = 0
        distance = 0
        new_rgb_values = [] #empty list to store new rgb
        tuple_new_rgb = () #empty tuple

        for i in range (len(pixel)): #x index and increments by one each time
            difference = ( target[i] - pixel[i] ) ** 2 #substract value in x index from pixel from target
            sum += difference #add all the differences

        distance = math.sqrt(sum) #square root the sum

        if distance > distance_desired: #if the distance is larger than then
            new_rgb_values = greyscale_only_rgb_alex(pixel) #get the new greyscale rgb values
            tuple_new_rgb = tuple(new_rgb_values) #transform list into tuple
        else:
            tuple_new_rgb = pixel #don't change the color

        new_pixels.append(tuple_new_rgb) #add the new rgb values into new pixels list for the image

    filtered_img.putdata(new_pixels) #put all the new pixels into the empty image

    #return the new image
    return filtered_img

#this is the function to get greyscale rgb values
def greyscale_only_rgb_alex(pixel):
    intensity = 0 #reset intensity
    new_rgb_values = [] #empty list to store new rgb
    tuple_new_rgb = () #empty tuple

    for value in pixel:
        intensity += value #adding all the rgb values inside the tuple

    intensity = intensity // 3 #get average of the rgb values

    new_rgb_values = [intensity] * 3 #the new rgb value will be a tuple of the same intensity for each three values
    tuple_new_rgb = tuple(new_rgb_values)

    return tuple_new_rgb

# ---------- BRISA'S FILTERS ---------- #
# ---------- SOPHIA'S FILTERS ---------- #    
# ---------- ZAFINA'S FILTERS ---------- #