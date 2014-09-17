#!/usr/bin/env python
# Copyright 2013 Brett Slatkin
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Configuration for local development."""

import os
from secrets import *

#SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
SQLALCHEMY_DATABASE_URI = ('mysql+mysqldb://dpxdt_user:pdiffallthethings@localhost/dpxdt')

SERVER_NAME = os.environ.get('SERVER_NAME', None)
MAX_CONTENT_LENGTH = 16 * 1024 * 1024

# Google OAuth2 login config for local development.
GOOGLE_OAUTH2_EMAIL_ADDRESS = ('737892445889-aop3tlqt5ic6bvgm2ve5ojlch04shoai@developer.gserviceaccount.com')
GOOGLE_OAUTH2_REDIRECT_PATH = '/oauth2callback'
GOOGLE_OAUTH2_REDIRECT_URI = ('http://babbage.pushpay.io:8080' + GOOGLE_OAUTH2_REDIRECT_PATH)
GOOGLE_OAUTH2_CLIENT_ID = ('737892445889-aop3tlqt5ic6bvgm2ve5ojlch04shoai.apps.googleusercontent.com')
GOOGLE_OAUTH2_CLIENT_SECRET = 'QDFjtjNVvyttgJOd8ORAEMjH'

CACHE_TYPE = 'simple'
CACHE_DEFAULT_TIMEOUT = 600

SESSION_COOKIE_DOMAIN = None

MAIL_DEFAULT_SENDER = 'Depicted <nobody@localhost>'
MAIL_SUPPRESS_SEND = True
MAIL_USE_APPENGINE = False

SLACK_WEBHOOK = 'https://pushpay.slack.com/services/hooks/incoming-webhook?token=uO0ZXqbMB5LZOtZ8yWTtTzeJ'
SLACK_CHANNEL = '#the_engine_room'
SERVER_URL = 'http://babbage.pushpay.io:8080'

ALLOWED_DOMAIN = 'pushpay.com'
