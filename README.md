# Image Similarity Search

This is summary readme for image similarity search and segregating similar images and storing them in a folder.  

Install the dependent packages given below:

```
pip install -r requirements.txt
```

Run [image_similarity_search](image_similarity_search.py) to find the image similarity search query and seperate the similar images with reference to the master base image and the script automatically makes the folder with the master image name and pushes all similar images into the folder. 

This similarity search is written with `numpy` package:
```
np.linalg.norm(images_encodings-master_image_encodings)
```
The landmarks are detected from the `face_recognition` library : 

```
import face_recognition

known_image = face_recognition.load_image_file("me.jpg")
known_face_encoding = face_recognition.face_encodings(known_image)[0]

unknown_picture = face_recognition.load_image_file("unknown.jpg")
unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]
```

The similar search query can be done wirth cosine similarity and procrustes libraries:

```
from scipy.spatial import distance
distance.cosine(image_landmarks1, image_landmarks2)
```

```
from scipy.spatial import procrustes

#The matrix b is a rotated, shifted, scaled and mirrored version of a here:

a = np.array(image_landmarks1, 'd')  #reshape the image landmarks into 2D array
b = np.array(image_landmarks2, 'd')
mtx1, mtx2, disparity = procrustes(a, b)
round(disparity)
```


---
## License & Copyright

@ Teric-AI Team

***
