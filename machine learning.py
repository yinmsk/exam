from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import Adam, SGD
from tensorflow.keras.layers import Input, Dense, Conv2D, MaxPooling2D, Flatten, Dropout
from tensorflow.keras.models import Model
import os
os.environ['KAGGLE_USERNAME'] = ''
os.environ['KAGGLE_KEY'] = ''

! kaggle datasets download - d tongpython/cat-and-dog

!unzip - q cat-and-dog.zip


train_datagen = ImageDataGenerator(
  rescale=1./255,
  rotation_range=10,
  zoom_range=0.1,
  width_shift_range=0.1,
  height_shift_range=0.1,
  horizontal_flip=True

test_datagen=ImageDataGenerator(
  rescale=1./255
)

train_gen=train_datagen.flow_from_directory(
  'training_set/training_set',
  target_size=(224, 224),
  batch_size=32,
  seed=2021,
  class_mode='categorical',
  shuffle=True
)

test_gen=test_datagen.flow_from_directory(
  'test_set/test_set',
  target_size=(224, 224),
  batch_size=32,
  seed=2021,
  class_mode='categorical',
  shuffle=False
)

from pprint import pprint
pprint(train_gen.class_indices)


preview_batch=train_gen.__getitem__(0)

preview_imgs, preview_labels=preview_batch

plt.title(str(preview_labels[0]))
plt.imshow(preview_imgs[0])

from tensorflow.keras.applications.inception_v3 import InceptionV3

input=Input(shape=(224, 224, 3))

base_model=InceptionV3(weights='imagenet', include_top=False,
                       input_tensor=input, pooling='max')

x=base_model.output
x=Dropout(rate=0.25)(x)
x=Dense(256, activation='relu')(x)
output=Dense(2, activation='softmax')(x)

model=Model(inputs=base_model.input, outputs=output)

model.compile(loss='categorical_crossentropy',
              optimizer=Adam(lr=0.001), metrics=['acc'])

model.summary()


from tensorflow.keras.callbacks import ModelCheckpoint

history=model.fit(
    train_gen,
    validation_data=test_gen,
    epochs=20,
    callbacks=[
      ModelCheckpoint('model.h5', monitor='val_acc',
                      verbose=1, save_best_only=True)
    ]
)


fig, axes=plt.subplots(1, 2, figsize=(20, 6))
axes[0].plot(history.history['loss'])
axes[0].plot(history.history['val_loss'])
axes[1].plot(history.history['acc'])
axes[1].plot(history.history['val_acc'])


from tensorflow.keras.models import load_model

model=load_model('model.h5')

print('Model loaded!')


test_imgs, test_labels=test_gen.__getitem__(100)

y_pred=model.predict(test_imgs)

classes=dict((v, k) for k, v in test_gen.class_indices.items())

fig, axes=plt.subplots(4, 8, figsize=(20, 12))

for img, test_label, pred_label, ax in zip(test_imgs, test_labels, y_pred, axes.flatten()):
  test_label=classes[np.argmax(test_label)]
  pred_label=classes[np.argmax(pred_label)]

  ax.set_title('GT:%s\nPR:%s' % (test_label, pred_label))
  ax.imshow(img)
