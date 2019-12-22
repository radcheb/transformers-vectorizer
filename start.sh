#!/usr/bin/env bash
# service nginx start
# uwsgi --ini uwsgi.ini
python3 -u -c "from transformers_vectorizer.serving.app import app

app.run(host='0.0.0.0', port=5005)
"
