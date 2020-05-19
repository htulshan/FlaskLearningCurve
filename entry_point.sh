#!/bin/bash

service nginx start
cd /app
gunicorn flashcards:app

exec "$@"