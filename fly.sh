#!/bin/bash
curl -L https://fly.io/install.sh | sh
mkdir -p flyctl
~/.fly/bin/flyctl --help > flyctl/help.txt
python fly_commands_help.py  | sh
