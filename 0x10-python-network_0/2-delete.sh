#!/bin/bash
# Usage: ./delete_request.sh <URL>
curl -sX DELETE "$1"
