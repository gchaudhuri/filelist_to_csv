# Convert the image list and mask/label image list in a folder to a csv file. 
#The training image names and corresponding label names should be same

# Import modules

import os
import pandas

# create variables with the folder names for each folder
img = os.listdir('./image') #assuming folder where training images are saved is named as 'image'. change folder path if different
lbl = os.listdir('./label') #assuming folder where masks images are saved is named as 'label'. change folder path if different.

#Create an empty dataframe
df= pd.DataFrame()

# Assign new columns as each folder list
df['image'] = img
df['label'] = lbl

# Save it as csv
df.to_csv('training.csv', index=False)
