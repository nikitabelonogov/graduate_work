FROM bamos/openface:latest

ARG workspace
ARG codespace

ENV workspace=${workspace:-"/workspace"}
ENV codespace=${codespace:-"./"}
ENV HOST="0.0.0.0"
ENV PORT="8080"
ENV DLIB_PATH="/root/openface/models/dlib/shape_predictor_68_face_landmarks.dat"
ENV NETWORK_MODEL="/root/openface/models/openface/nn4.small2.v1.t7"
ENV DATA_URL="data.pkl"
ENV DATA_PATH="${workspace}/data/data.pkl"

WORKDIR ${workspace}

# Install libraries
RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install -y \
    python \
    python-pip \
    bash

# Install dependencies
COPY ${codespace}/requirements.txt ${workspace}/requirements.txt
RUN pip install -r ${workspace}/requirements.txt

# Copy modules
COPY ${codespace}/MyClassificator ${workspace}/MyClassificator
COPY ${codespace}/MyOpenFace ${workspace}/MyOpenFace

# Copy helpers script
COPY ${codespace}/helpers.py ${workspace}

# Copy flask application's source code
COPY ${codespace}/MyFlaskApp ${workspace}/MyFlaskApp

# Copy run script
COPY ${codespace}/run.py ${workspace}/

# Dowload/Copy data
ADD ${DATA_URL} ${DATA_PATH}

CMD cd /workspace && \
    python run.py \
    --Host "${HOST}" \
    --Port "${PORT}" \
    --Data "${workspace}/data/data.pkl" \
    --dlib_path "${DLIB_PATH}" \
    --network_model "${NETWORK_MODEL}"
