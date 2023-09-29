#!/bin/bash
# Usage: ./102-catch_me.sh
curl -s -X PUT -L -d "user_id=98" 0.0.0.0:5000/catch_me
