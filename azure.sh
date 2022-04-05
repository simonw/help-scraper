#!/bin/bash
#pip install azure-cli
mkdir -p azure
az --help > azure/azure-help.txt
az version > azure/azure-version.txt
python azure_commands_help.py | sh
