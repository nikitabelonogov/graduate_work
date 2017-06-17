#!/usr/bin/env bash

cd /workspace

mkdir -p ${DATA_PATH}

curl ${DATA_URL} >> ${DATA_PATH}/data.pkl

python run.py \
    --Host "${HOST}" \
    --Port "${PORT}" \
    --Data "${DATA_PATH}/data.pkl" \
    --dlib_path "${DLIB_PATH}" \
    --network_model "${NETWORK_MODEL}"