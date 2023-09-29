#!/bin/bash
# Usage: ./get_with_header.sh <URL>
curl -sH "X-School-User-Id: 98" "$1"
