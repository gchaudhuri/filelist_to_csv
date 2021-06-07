# Convert the image list and mask/label image list in a folder to a csv file. 
#The training image names and corresponding label names should be same

# Import modules

import os
import pandas

# create variables with the folder names for each folder
# assuming folder where training images are saved is named as 'image'. change folder path if different
train_img = [os.path.join(r,file) for r,d,f in os.walk("C:/Users/gchaudhuri/jupyternb/solaris/test_gc/train_image") for file in f] 
# assuming folder where masks images are saved is named as 'label'. change folder path if different.
lbl = [os.path.join(r,file) for r,d,f in os.walk("C:/Users/gchaudhuri/jupyternb/solaris/test_gc/label") for file in f]
# assuming folder where test images are saved is named as 'test_image'. change folder path if different.
test_img = [os.path.join(r,file) for r,d,f in os.walk("C:/Users/gchaudhuri/jupyternb/solaris/test_gc/test_image") for file in f] 


# Create an empty dataframe
df_train= pd.DataFrame()
df_test=pd.DataFrame()

# Assign new columns as each folder list
df_train['image'] = train_img
df_train['label'] = lbl
df_test['image']=test_img

# Save it as csv
df_train.to_csv('training_df.csv', index=False)
df_test.to_csv('test_df.csv', index=False)
