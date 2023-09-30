#!/bin/bash
# Usage: ./http_methods.sh <URL>
curl -sI "$1" | grep "Allow" | cut -d  " " -f2-
