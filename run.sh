#!/bin/bash

source ~/.pyenv/versions/educannombra/bin/activate
cd "$(dirname "$0")"
exec python main.py run
