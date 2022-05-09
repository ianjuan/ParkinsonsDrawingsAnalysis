import os
import tensorflow as tf
import tensorflow_datasets as tfds

# config
EPOCH = 10
PATIENCE = 10
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'

# load dataset
ds_train, ds_test = tfds.load('mnist', split=['train', 'test'],
                              shuffle_files=True, as_supervised=True)
def normalize_img(image, label):
    return tf.cast(image, tf.float32) / 255., label
## train dataset
ds_train = ds_train.map(normalize_img, num_parallel_calls=tf.data.AUTOTUNE)
ds_train = ds_train.cache()
ds_train = ds_train.batch(128)
ds_train = ds_train.prefetch(tf.data.AUTOTUNE)
## test dataset
ds_test = ds_test.map(normalize_img, num_parallel_calls=tf.data.AUTOTUNE)
ds_test = ds_test.batch(128)
ds_test = ds_test.cache()
ds_test = ds_test.prefetch(tf.data.AUTOTUNE)

# the model
def get_model():
    model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10)
    ])
    return model

model = get_model()
model.compile(optimizer=tf.keras.optimizers.Adam(0.001),
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=[tf.keras.metrics.SparseCategoricalAccuracy()])

# callbacks
my_callbacks = tf.keras.callbacks.EarlyStopping(patience=PATIENCE, 
                                                monitor='val_loss', 
                                                restore_best_weights=True)

# fit dataset to model
model.fit(ds_train, epochs=EPOCH, validation_data=ds_test)

# save model
model.save('./model')

print("finished")