#!/bin/bash
curl -L https://fly.io/install.sh | sh
mkdir -p flyctl
python fly_commands_help.py ~/.fly/bin/flyctl

# Grab a list of current Fly regions too
~/.fly/bin/flyctl platform regions > flyctl/fly-regions.txt
# And vm-sizes
~/.fly/bin/flyctl platform vm-sizes > flyctl/fly-vm-sizes.txt
