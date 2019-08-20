import face_recognition
from PIL import Image
import cv2

def CoordinateFaces (main_path1, main_path2, target_path):
    target_image = Image.open(target_path)
    width, height = target_image.size

    target_image = face_recognition.load_image_file(target_path)
    coordinates = face_recognition.face_locations(target_image)
    n_people = len(coordinates)
    
    if n_people == 0:
        return "no people"

    main_image1 = face_recognition.load_image_file(main_path1)
    main_image2 = face_recognition.load_image_file(main_path2)
    
    main_encoding1 = face_recognition.face_encodings(main_image1)[0]
    main_encoding2 = face_recognition.face_encodings(main_image2)[0]
    

    known_faces = [
        main_encoding1,
        main_encoding2
    ]
    
    
    result = 1
    result_loc = 1
    for a in range(1,n_people):
        top, right, bottom, left = coordinates[a]
        individual = target_image[top:bottom, left:right]
        target_encoding = face_recognition.face_encodings(individual)[0]
        face_distances = face_recognition.face_distance(known_faces, target_encoding)
        if result > face_distances[1]:
            result = face_distances[1]
            result_loc = a

    # code from here before return is to test the result
    #a1, a2, a3, a4 = coordinates[result_loc]
    #img = Image.open(target_path)
    #area = (a4, a1, a2, a3)
    #cropped_img = img.crop(area)
    #cropped_img.save("./image/hyunjay_face1.jpg")


    return width, height, coordinates, coordinates[result_loc]