from PIL import Image
import numpy as np

image_path = input("Enter the Image Path : ")
try:
    image = Image.open(image_path)
    image.verify()
    image = Image.open(image_path)
    print("Success! File Load Successfully")
except FileNotFoundError:
    print("The file was not found. Check the path and spelling!")
    print("Please Give Valid Input Code is terminated")
    exit()
except Exception as e:
    print(f"The image file is corrupted or broken. Details: {e}")
    print("Please Give Valid Input Code  is treminated")
    exit()

current_image = image.copy()
def change(n1):
        global current_image
        ax = input("Do you Want See image (Yes/No) :").lower()
        if (ax == "yes"):
            az = Image.fromarray(n1)
            az.show()
        else:
            return

        al = input("Do You Want to Save Image (Yes/No) :").lower()
        if (al == "yes"):
            ab = input("By which name Do you want to save: ")
            az = Image.fromarray(n1)
            az.show()
            az.save(f"{ab}.jpg")
            print(f"Saved Successfully as {ab}.jpg")

        else:
            print("Changes discarded.")
            return

while True:
    menu = """
    =========================
    Image Processing Toolkit
    =========================

    1. Increase Brightness
    2. Decrease Brightness
    3. Negative Image
    4. Horizontal Flip
    5. Vertical Flip
    6. Convert to GrayScale
    7. Reset To orginal
    8. Exit
    """

    print(menu)
    try:
        n = int(input("Enter the Number Accodrding to Toolkit :"))
    except ValueError:
        print("invalid")
        continue

# Brightness Increment 
    if (n == 1):
        try:
            a = int(input("Enter the The amount Of increase: "))

            ar = np.array(current_image,dtype=np.int16) 
            n1 = ar + a
            n1 = np.clip(n1, 0, 255).astype(np.uint8)
            print("Brightness Increased")
            change(n1)
            
        except ValueError:
            print("Please Enter valid Amount")
            continue
    
    elif(n == 2):
        try:
            aq = int(input("Enter the The amount Of Decrease: "))
            ar = np.array(current_image,dtype=np.int16)
            n1 = ar - aq
            n1 = np.clip(n1, 0, 255).astype(np.uint8)
            print("Brightness Decreased")
            change(n1)

        except ValueError:
            print("Please Enter valid Amount")
            continue
    
    elif(n==3):
        ar = np.array(current_image)
        n1 = 255 - ar
        change(n1)

    elif(n==4):
        ar = np.array(current_image)
        n1 = ar[:,::-1]
        change(n1)

    elif(n==5):
        ar = np.array(current_image)
        n1 = ar[::-1,:]
        change(n1)

    elif (n==6):
        ar = np.array(current_image)
        if len(ar.shape) < 3:
            print("Image is already in grayscale!")
            continue
        else:
            n1 = np.dot(ar[..., :3], [0.2989, 0.5870, 0.1140]).astype(np.uint8)
        
        print("Converted to Grayscale successfully!")
        change(n1)

    elif (n==7):
        current_image = image.copy()
        print("Toolkit reset! All edits cleared back to the original image.")


    elif(n==8):
        print("Thankyou")
        break

    else:
        print("Invalid Input")