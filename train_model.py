import tensorflow as tf
from tensorflow.keras import layers

dataset=tf.keras.utils.image_dataset_from_directory(
"data/food_dataset",
image_size=(224,224),
batch_size=32,
validation_split=0.2,
subset="both",
seed=123
)

train_ds=dataset[0]
val_ds=dataset[1]

classes=train_ds.class_names

base=tf.keras.applications.MobileNetV2(

input_shape=(224,224,3),

include_top=False,

weights="imagenet"

)

base.trainable=False

model=tf.keras.Sequential([

layers.Rescaling(
1./127.5,
offset=-1
),

base,

layers.GlobalAveragePooling2D(),

layers.Dense(
128,
activation="relu"
),

layers.Dense(
len(classes),
activation="softmax"
)

])

model.compile(

optimizer="adam",

loss="sparse_categorical_crossentropy",

metrics=["accuracy"]

)

model.fit(

train_ds,

validation_data=val_ds,

epochs=20

)

model.save(
"models/food_model.keras"
)

print("Training Completed ❤️")