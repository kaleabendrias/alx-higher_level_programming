#!/bin/bash
# Usage: ./100-status_code.sh <URL>
curl -s -o /dev/null -w "%{http_code}" "$1"
