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

mailfile = /home/yzbx/git/yzbxLib/scripts/mail.txt
while true
do
if test `pgrep tmate | wc -l` = '0' ; then
    echo "start tmate"
    tmate -S /tmp/tmate.sock new-session -d ;
    tmate -S /tmp/tmate.sock wait tmate-ready
    echo "write to mail.txt"
    tmate -S /tmp/tmate.sock display -p '#{tmate_ssh}' > $mailfile
    echo "send email"
    mail -s "tmate" youdaoyzbx@163.com < $mailfile
    mail -s "tmate" 1627884766@qq.com < $mailfile
    cd /home/yzbx/git/yzbxLib/scripts && git commit -a && git push
fi
sleep 30
done
