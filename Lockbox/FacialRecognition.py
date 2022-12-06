import cv2
import os
from os import listdir
from deepface import DeepFace

#LockBox Project - Jack Wylie - 2022

def main():
    #Lockbox1234
    nav = ""
    again = ""
    password = ""
    
    print("Lockbox Project")
    while nav not in ('1', '2'):
        nav = str(input("""What would you like to do?
                            1.) Access Lockbox
                            2.) Enter password to add a new person to the list of verified faces
                            Please enter a number:"""))

    if nav == '2':
        password = str(input("Please enter the Lockbox password:"))
        if password == 'Lockbox1234':
            newface()
        elif password != 'Lockbox1234':
            print("Incorrect password")
    elif nav == '1':
        photo_capture()
        identification()



    print("Would you like to run the program again?")
    while again not in ('y', 'n'):
        again = str(input("Enter (y/n):"))

    if again == 'y':
        print("")
        main()
    else:
        print("Program completed")
            
        
    
    
def photo_capture():

    print("")
    print("Taking photo for verification")
    webcam = cv2.VideoCapture(0) #0 = integrated cam, 1 = other connected cam

    result = True
    while(result):
        cap,photo = webcam.read()
        cv2.imwrite(r"C:\Users\Owner\Desktop\Lockbox\temp_photo\‪Access_Photo.jpg", photo)
        result = False
    webcam.release()

    oldname = "C:\\Users\\Owner\\Desktop\\Lockbox\\temp_photo\\â€ªAccess_Photo.jpg"
    newname = "C:\\Users\\Owner\\Desktop\\Lockbox\\temp_photo\\Access_Photo.jpg"
    os.rename(oldname, newname)
    
    access_photo = cv2.imread("C:\\Users\\Owner\\Desktop\\Lockbox\\temp_photo\\Access_Photo.jpg")
    cv2.imshow('Face to be analyzed', access_photo)
    cv2.waitKey(0)#allows face photo to be shown for 3 secs before closing
    cv2.destroyAllWindows()
    
    return 0
    


def identification():
    
    AccessPhoto = "temp_photo\\Access_Photo.jpg"
    AllowedFaces = "assets\\AllowedFaces" 
    model = "Facenet"

    print("")
    print("Identifying photo")
    
    for images in listdir(AllowedFaces):
        AllowedPhoto = AllowedFaces + "\\" + images
        
        try:
            result = DeepFace.verify(img1_path = AccessPhoto, img2_path = AllowedPhoto, model_name = model) #result becomes a library
        except Exception:
            print("Sorry unable to use the photo taken. Please try again and remember to take a clear photo with adequate lighting!")
            break
        else:
            if result['verified'] == True:
                break
            else:
                pass

    if result['verified'] == False:
        print("Access Denied")
    elif result['verified'] == True:
        print("Access Granted")
        os.startfile("C:\\Users\\Owner\\Desktop\\Lockbox\\assets\\Cache")

    os.remove("C:\\Users\\Owner\\Desktop\\Lockbox\\temp_photo\\Access_Photo.jpg")



def newface():

    name = str(input("Please enter the name of the person you want to grant access to:"))
    print("Taking photo")
    location = "C:\\Users\\Owner\\Desktop\\Lockbox\\assets\\AllowedFaces\\"
    newperson = location + name + ".jpg"
    

    webcam = cv2.VideoCapture(0)

    result = True
    while(result):
        cap,photo = webcam.read()
        cv2.imwrite(newperson, photo)
        result = False
    webcam.release()

    print("New Face Added")

main()

