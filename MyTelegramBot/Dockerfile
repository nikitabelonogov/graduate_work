FROM bamos/openface:latest

ARG workspace
ARG codespace

ENV workspace=${workspace:-"/workspace"}
ENV codespace=${codespace:-"../.."}
ENV TOKEN=""
ENV HOST="0.0.0.0"
ENV PORT="8080"

WORKDIR ${workspace}

# Install libraries
RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install -y \
    python \
    bash

# Copy telegram bot's source code
COPY ${codespace}/TelegramBot ${workspace}/TelegramBot

# Copy run script
COPY ${codespace}/run_bot.py ${workspace}/

CMD cd /workspace && \
    python run.py \
    --Host ${HOST} \
    --Port ${PORT} \
    --Data ${DATA_PATH} \
    --dlib_path ${DLIB_PATH} \
    --network_model ${NETWORK_MODEL}
