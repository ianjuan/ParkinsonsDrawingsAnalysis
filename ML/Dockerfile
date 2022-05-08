FROM gcr.io/deeplearning-platform-release/tf2-cpu.2-8
WORKDIR /

# Copies the trainer code to the docker image.
COPY ML/train /train

# Sets up the entry point to invoke the trainer.
ENTRYPOINT ["python", "-m", "train.train"]