#!/bin/bash

source common.sh

./dpxdt/runserver.py \
    --local_queue_workers \
    --phantomjs_binary=$PHANTOMJS_BINARY \
    --phantomjs_script=$CAPTURE_SCRIPT \
    --phantomjs_timeout=20 \
    --release_server_prefix=http://localhost:8080/api \
    --queue_server_prefix=http://localhost:8080/api/work_queue \
    --queue_idle_poll_seconds=10 \
    --queue_busy_poll_seconds=10 \
    --pdiff_timeout=20 \
    --reload_code \
    --port=8080 \
    --verbose \
    $@
