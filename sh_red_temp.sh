#!/bin/bash

gnome-terminal --maximize -x bash -c "tmux new-session 'python3 sh_red_temp.py $1 | /home/derrick/.local/bin/ct'"
