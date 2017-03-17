#!/bin/bash
# see web https://tmate.io
# sudo apt-get install software-properties-common && \
# sudo add-apt-repository ppa:tmate.io/archive    && \
# sudo apt-get update                             && \
# sudo apt-get install tmate

# tmate -S /tmp/tmate.sock new-session -d               # Launch tmate in a detached state
# tmate -S /tmp/tmate.sock wait tmate-ready             # Blocks until the SSH connection is established
# tmate -S /tmp/tmate.sock display -p '#{tmate_ssh}'    # Prints the SSH connection string
# tmate -S /tmp/tmate.sock display -p '#{tmate_ssh_ro}' # Prints the read-only SSH connection string
# tmate -S /tmp/tmate.sock display -p '#{tmate_web}'    # Prints the web connection string
# tmate -S /tmp/tmate.sock display -p '#{tmate_web_ro}' # Prints the read-only web connection string

while true
do
if [ ! `pgrep tmate` ] ; then
tmate -S /tmp/tmate.sock new-session -d
tmate -S /tmp/tmate.sock wait tmate-ready
tmate -S /tmp/tmate.sock display -p '#{tmate_ssh}' > /tmp/mail.txt
mail -s "tmate" youdaoyzbx@163.com < /tmp/mail.txt
mail -s "tmate" 1627884766@qq.com < /tmp/mail.txt
fi
sleep 30
done
