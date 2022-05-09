FROM tensorflow/tensorflow
WORKDIR /

# Copies the trainer code to the docker image.
COPY . /predict

# 指定 volume
VOLUME "/model"

# Sets up the entry point to invoke the trainer.
ENTRYPOINT ["python", "-m", "predict.main"]