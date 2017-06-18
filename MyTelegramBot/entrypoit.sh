#!/usr/bin/env sh

cd /workspace

python run.py \
    --token "${TOKEN}" \
    --host "${HOST}" \
    --port "${PORT}"