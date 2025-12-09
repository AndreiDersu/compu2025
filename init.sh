#!/bin/bash
source figmaflow/bin/activate
cvlc --no-video --play-and-exit sources/stillalive.flac &
python3 scripts/main.py &
echo "gracias por revisar :)"
