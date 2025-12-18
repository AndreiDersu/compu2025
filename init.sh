#!/bin/bash
source figmaflow/bin/activate
python3 scripts/main.py 
echo "gracias por revisar :)"
cvlc --no-video --play-and-exit sources/stillalive.flac
