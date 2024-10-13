#!/bin/bash

gnome-terminal --maximize -x bash -c "tmux new-session 'ssh -i /home/derrick/.ssh/cvec_ed25519 sysadmin@$1 | ct'"
