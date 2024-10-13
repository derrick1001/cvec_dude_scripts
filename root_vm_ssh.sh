#!/bin/bash

gnome-terminal --maximize -x bash -c "tmux new-session 'ssh -i /home/derrick/.ssh/cvec_root_ed25519 root@$1'"
