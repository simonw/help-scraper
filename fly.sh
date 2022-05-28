#!/bin/bash
curl -L https://fly.io/install.sh | sh
mkdir -p flyctl
python fly_commands_help.py ~/.fly/bin/flyctl
