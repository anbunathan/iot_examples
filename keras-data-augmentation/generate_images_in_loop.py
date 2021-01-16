# USAGE
# python generate_images.py --image dog.jpg --output generated_dataset/dogs
# python generate_images.py --image cat.jpg --output generated_dataset/cats

# import the necessary packages
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing.image import load_img
import numpy as np
import argparse
import os

directory = "input_images"
out_dir = "generate_images"
for filename in os.listdir(directory):
	if filename.endswith(".png") or filename.endswith(".jpg"):
		file = os.path.splitext(filename)[0]
		outdir = out_dir + "/" + file
		if not os.path.exists(outdir):
			os.makedirs(outdir)
		print(os.path.join(directory, filename))
		print(os.path.splitext(filename)[0])
		print("[INFO] loading example image...")
		image = load_img(os.path.join(directory, filename))
		image = img_to_array(image)
		image = np.expand_dims(image, axis=0)
		# construct the image generator for data augmentation then
		# initialize the total number of images generated thus far
		# https://keras.io/api/preprocessing/image/
		aug = ImageDataGenerator(
			rotation_range=30, #Int. Degree range for random rotations.(-40,40)
			zoom_range=0.15, #Float or [lower, upper]. Range for random zoom. If a float, [lower, upper] = [1-zoom_range, 1+zoom_range].
			width_shift_range=0.2,
			height_shift_range=0.2,
			shear_range=0.15, #Float. Shear Intensity (Shear angle in counter-clockwise direction in degrees)
			horizontal_flip=True,
			fill_mode="nearest") #Points outside the boundaries of the input are filled according to the given mode
		total = 0
		# construct the actual Python generator
		print("[INFO] generating images...")
		imageGen = aug.flow(image, batch_size=1, save_to_dir=outdir,
							save_prefix="image", save_format="jpg")
		# loop over examples from our image data augmentation generator
		for image in imageGen:
			# increment our counter
			total += 1
			# if we have reached the specified number of examples, break
			# from the loop
			if total == 500:
				break


