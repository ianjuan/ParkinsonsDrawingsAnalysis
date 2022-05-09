FROM tensorflow/tensorflow
WORKDIR /

# Copies the trainer code to the docker image.
COPY . /train

# install packages
RUN pip install tensorflow_datasets

# 指定 volume
VOLUME "/model"

# Sets up the entry point to invoke the trainer.
ENTRYPOINT ["python", "-m", "train.main"]