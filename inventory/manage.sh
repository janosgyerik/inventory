#!/usr/bin/env bash

set -euo pipefail

cd "$(dirname "$0")"

if test $# = 0; then
    pipenv run python manage.py help
else
    pipenv run python manage.py "$@"
fi
