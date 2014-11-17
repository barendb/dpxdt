 #!/bin/bash

source common.sh

./dpxdt/runworker.py \
    --phantomjs_binary=$PHANTOMJS_BINARY \
    --phantomjs_script=$CAPTURE_SCRIPT \
    --release_server_prefix=$RELEASE_SERVER_PREFIX \
    --queue_server_prefix=$QUEUE_SERVER_PREFIX \
    --verbose \
    --pdiff_timeout=50 \
    --release_client_id=yfnje6vikkazeeymtscey3gfz6uqzrrt \
    --release_client_secret=hMGp4UWzVkFloy5tpfDxcgU4rbk \
    --release_server_prefix=http://0.0.0.0:8080/api \
    --queue_server_prefix=http://0.0.0.0:8080/api/work_queue \
    $@
