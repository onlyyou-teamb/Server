# import face_recognition
# from PIL import Image
# import cv2

# def CoordinateFaces (main_path1, main_path2, target_path):
#     target_image = Image.open(target_path)
#     width, height = target_image.size

#     target_image = face_recognition.load_image_file(target_path)
#     coordinates = face_recognition.face_locations(target_image)
#     n_people = len(coordinates)
    
#     if n_people == 0:
#         return "no people"

#     main_image1 = face_recognition.load_image_file(main_path1)
#     main_image2 = face_recognition.load_image_file(main_path2)
    
#     main_encoding1 = face_recognition.face_encodings(main_image1)[0]
#     main_encoding2 = face_recognition.face_encodings(main_image2)[0]
    

#     known_faces = [
#         main_encoding1,
#         main_encoding2
#     ]
    
    
#     result = 1
#     result_loc = 1
#     for a in range(1,n_people):
#         top, right, bottom, left = coordinates[a]
#         individual = target_image[top:bottom, left:right]
#         target_encoding = face_recognition.face_encodings(individual)[0]
#         face_distances = face_recognition.face_distance(known_faces, target_encoding)
#         if result > face_distances[1]:
#             result = face_distances[1]
#             result_loc = a

#     # code from here before return is to test the result
#     #a1, a2, a3, a4 = coordinates[result_loc]
#     #img = Image.open(target_path)
#     #area = (a4, a1, a2, a3)
#     #cropped_img = img.crop(area)
#     #cropped_img.save("./image/hyunjay_face1.jpg")


#     return width, height, coordinates, coordinates[result_loc]


# #indi_sung_jin1 = "./image/KakaoTalk_20190803_203235073_25.jpg"
# #indi_sung_jin2 = "./image/KakaoTalk_20190809_152421406.jpg"
# #indi_sung_jin3 = "./image/KakaoTalk_20190810_210059414_05.jpg"
# #lot_of_people1 = "./image/KakaoTalk_20190806_133853463_04.jpg"
# #lot_of_people2 = "./image/KakaoTalk_20190810_215430625_04.jpg"
# #lot_of_people3 = "./image/KakaoTalk_20190813_112158357.jpg"
# #lot_of_people4 = "./image/KakaoTalk_20190731_222118936_01.jpg"
# #indi_youn_woo1 = "./image/KakaoTalk_20190809_141128768.jpg"
# #indi_youn_woo2 = "./image/KakaoTalk_20190812_113755922.jpg"
# #indi_young_ki1 = "./image/indiv_youngki.jpg"
# #indi_hyun_jay1 = "./image/KakaoTalk_20190811_222711792_05.jpg"
# #indi_hyun_jay2 = "./image/KakaoTalk_20190809_141004388.jpg"


# #print(CoordinateFaces(indi_hyun_jay1, indi_hyun_jay1, lot_of_people1))

