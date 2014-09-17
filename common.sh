#!/bin/bash

export PYTHONPATH=.:./dependencies/lib:$PYTHONPATH
export CAPTURE_SCRIPT=dpxdt/client/capture.js

# Update these for your environment:
export PHANTOMJS_BINARY=/usr/local/share/phantomjs/bin/phantomjs

# Where the API servers to run workers against live.
export RELEASE_SERVER_PREFIX=http://localhost:8080/api
export QUEUE_SERVER_PREFIX=http://localhost:8080/api/work_queue

# Update this for your deployment environment:
export PHANTOMJS_DEPLOY_BINARY=phantomjs
