FROM python:2.7.13-alpine

ARG workspace
ARG codespace

ENV workspace=${workspace:-"/workspace"}
ENV codespace=${codespace:-"./"}
ENV TOKEN=""
ENV HOST="0.0.0.0"
ENV PORT="8080"

WORKDIR ${workspace}

# Install dependencies
COPY ${codespace}/requirements.txt ${workspace}/requirements.txt
RUN pip install -r ${workspace}/requirements.txt

# Copy telegram bot's source code
COPY ${codespace}/TelegramBot ${workspace}/TelegramBot

# Copy run script
COPY ${codespace}/run.py ${workspace}/

# Copy entrypoit
COPY ${codespace}/entrypoit.sh ${workspace}/
RUN chmod +x ${workspace}/entrypoit.sh

CMD ${workspace}/entrypoit.sh
