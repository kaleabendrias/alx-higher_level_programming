#!/bin/bash
# Usage: ./102-catch_me.sh
curl -sL -X PUT -H "Origin: School" -d "user_id=98" 0.0.0.0:5000/catch_me_3
