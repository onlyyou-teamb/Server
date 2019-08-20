import face_recognition  # import face_recognition open source

def NumOfFace (path):  # input path of image
    image = face_recognition.load_image_file(path)  # load image from path

    faces_coordinate = face_recognition.face_locations(image)  # get all the coordinates of detected faces in the image

    len_of_image = len(faces_coordinate)  # count how many faces has been detected

    if len_of_image == 1:  # if there is only one face detected
        return True, faces_coordinate  # return True and the coordinate of the face in the image
    else:  # if not
        return False  # return False


# codes below is for test

#path1 = "./image/KakaoTalk_20190803_203235073_25.jpg"
#path2 = "./image/KakaoTalk_20190806_133853463_04.jpg"


#print(NumOfFace(path1))
#print(NumOfFace(path2))
