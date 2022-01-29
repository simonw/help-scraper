#!/bin/bash
curl -L https://fly.io/install.sh | sh
mkdir -p flyctl
~/.fly/bin/flyctl --help > flyctl/flyctl-help.txt
~/.fly/bin/flyctl version > flyctl/flyctl-flyctl-version.txt
python fly_commands_help.py | sh
