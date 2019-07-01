# Copyright 2018 Google LLC
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

# [START gae_python37_app]
from flask import Flask, request
import re
import os
from concrete_task import HtmlReport, PlaneTextReport
import logging
logging.getLogger().setLevel(logging.INFO)


# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


@app.route('/')
def main():
    try:
        query = request.args.get('target', '')
        env = os.environ.get('PATTERN')
        pattern = re.compile(r'%s' % env)
        logging.info(pattern)
        match = re.match(pattern, query)
        if match:
            logging.info('match!')
        else:
            logging.info('not matcn!')
        logging.info('start')
        logging.info(query)
        title = "Report Title"
        text = [
            "report line 1",
            "report line 2",
            "report line 3"
        ]

        plane_report = PlaneTextReport(title, text)
        plane_report.display()
        print()

        html_report = HtmlReport(title, text)
        html_report.display()
        print()

        logging.info('stop')
        return 'Hello World!'
    except Exception:
        logging.error('error')


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]
