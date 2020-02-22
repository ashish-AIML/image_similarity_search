'''
PYTHON CODE FOR IMAGE SIMILARITY SEARCH AND SEPERATE LIKE IMAGES FROM UNLIKE
'''
#import necessary packages and install necessary packages by running requirements.txt
import face_recognition
import numpy as np
import os
import shutil

#similarity search function to compute similarity between images using Euclidean distance
def similarity_search():

	image_directory= '/home/ozbek/Documents/face_recognition/examples/knn_examples/sample/'  #test images directory
	master_image= '/home/ozbek/Desktop/master/barack-obama.jpg'  #master base image
	master_image_directory = '/home/ozbek/Desktop/master/'   #master base folder

	for each_image in os.listdir(image_directory):
		path = image_directory + each_image
		images = face_recognition.load_image_file(path)
		images_encodings = face_recognition.face_encodings(images)[0]   #computing landmarks of test images

		# my_face_encoding now contains a universal 'encoding' of my facial features that can be compared to any other picture of a face!
		# for each_image_master in os.listdir(master_image_directory):  #can uncomment this for computing master images in bulk
		# path1 = master_image_directory + each_image_master
		master_img = face_recognition.load_image_file(master_image)
		master_image_encodings = face_recognition.face_encodings(master_img)[0]  #computing landmarks of master image

		similarity= np.linalg.norm(images_encodings-master_image_encodings) #brain behind similarity search, i.e., euclidean distance
		print(similarity)
		print(each_image)
		folder1= master_image.split('.')[0]
		folder= folder1.split('/')[-1]
		if similarity < 0.4:
			if not os.path.exists('/home/ozbek/Desktop/master/'+folder):
				os.mkdir('/home/ozbek/Desktop/master/'+folder)
			shutil.move(path, master_image_directory+folder)

similarity_search()
