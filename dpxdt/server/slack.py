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

"""Implements email sending for the API server and frontend."""

import logging
import urllib2

# Local libraries
from flask import url_for
from flask.ext.login import current_user

# Local modules
from . import app
from dpxdt import server
from dpxdt.server import models
from dpxdt.server import operations
from dpxdt.server import utils


@utils.ignore_exceptions
@app.route('/email/ready_for_review/<int:build_id>/'
           '<string:release_name>/<int:release_number>')


def slack_ready_for_review(build_id, release_name, release_number):
    """Sends a message to slack that build is ready for review"""
    build = models.Build.query.get(build_id)

    """Reuse flag"""
    if not build.send_email:
        logging.debug(
            'Not sending slack webhook ready for review because build does not have '
            'email enabled. build_id=%r', build.id)
        return

    ops = operations.BuildOps(build_id)
    release, run_list, stats_dict, _ = ops.get_release(
        release_name, release_number)

    if not run_list:
        logging.debug(
            'Not sending slack webhook ready for review because there are '
            ' no runs. build_id=%r, release_name=%r, release_number=%d',
            build.id, release.name, release.number)
        return

    """curl -X POST --data-urlencode 'payload={"channel": "@barendb",
          "username": "webhookbot",
          "text": "This is posted to #general and comes from a bot named webhookbot.",
          "icon_emoji": ":ghost:"}'
          https://pushpay.slack.com/services/hooks/incoming-webhook?token=%s
    """


    data = {
      'channel' : '@barendb',
      'username' : 'webhookbot',
      'text' : 'PDiff %s: %s - Ready for review'  % (build.name, release.name),
      'icon_emoji' : ':pdiff:',
      'attachments' : [{
          'fallback' : 'New open task [Urgent]: <%s|Test out Slack message attachments>' % url_for('view_release', id=build.id, name=release.name, number=release.number, _external=True),
          'pretext' : 'New open task [Urgent]: <%s|Test out Slack message attachments>' %url_for('view_release', id=build.id, name=release.name, number=release.number, _external=True),
          'color' : '#D00000',
          'fields' : [
            {
              'title' : 'Notes',
              'value' : 'This is much easier than I thought it would be.',
              'short' : 'false'
            }
          ]
        }
      ]
    }


    req = urllib2.Request(server.app.config['SLACK_WEBHOOK'], 'payload=%s' % urllib2.urlencode(data))
    response = urllib2.urlopen(req)
    #result = response.read()
    return



    """
    email_body = render_template(
        'email_ready_for_review.html',
        build=build,
        release=release,
        run_list=run_list,
        stats_dict=stats_dict)

    recipients = []
    if build.email_alias:
        recipients.append(build.email_alias)
    else:
        for user in build.owners:
            recipients.append(user.email_address)

    if not recipients:
        logging.debug(
            'Not sending ready for review email because there are no '
            'recipients. build_id=%r, release_name=%r, release_number=%d',
            build.id, release.name, release.number)
        return

    message = Message(title, recipients=recipients)
    message.html = email_body

    logging.info('Sending ready for review email for build_id=%r, '
                 'release_name=%r, release_number=%d to %r',
                 build.id, release.name, release.number, recipients)

    return render_or_send(send_ready_for_review, message)
    """
