#!/bin/bash
# Usage: ./script.sh <URL>
curl -s "$1" | wc -c
