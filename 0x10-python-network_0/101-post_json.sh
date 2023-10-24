#!/bin/bash
# Usage: ./101-post_json.sh <URL> <filename>
curl -s -H "Content-Type: application/json" -X POST --data "@$2" "$1"
