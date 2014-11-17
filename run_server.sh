#!/bin/bash

source common.sh

./dpxdt/runserver.py \
    --reload_code \
    --port=8080 \
    --verbose \
    --ignore_auth \
    --release_server_prefix=http://0.0.0.0:8080/api \
    --queue_server_prefix=http://0.0.0.0:8080/api/work_queue \
    --release_client_id=yfnje6vikkazeeymtscey3gfz6uqzrrt \
    --release_client_secret=hMGp4UWzVkFloy5tpfDxcgU4rbk \
    $@
