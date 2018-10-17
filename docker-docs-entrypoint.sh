#!/usr/bin/env bash

DOCS_PATH=/app/docs

make -C $DOCS_PATH html
python -m http.server --directory $DOCS_PATH/_build/html
