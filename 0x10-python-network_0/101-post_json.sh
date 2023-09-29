#!/bin/bash
# Usage: ./101-post_json.sh <URL>
curl -sX POST -d "$(cat "$2")" "$1"