#!/bin/bash

gnome-terminal --maximize -x bash -c "tmux new-session 'python3 sh_low_light.py $1 | /home/derrick/.local/bin/ct'"
