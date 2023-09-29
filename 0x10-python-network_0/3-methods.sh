#!/bin/bash
# Usage: ./http_methods.sh <URL>
curl -sI 35.175.126.161 | grep "Allow" | cut -d  " " -f2-
