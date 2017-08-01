# mount via sudo
sshfs -o allow_other,default_permissions,kernel_cache,auto_cache,reconnect,compression=no,cache_timeout=600,ServerAliveInterval=15 -o sftp_server="/usr/bin/sudo  /usr/lib64/ssh/sftp-server"<user>@<machine>:/remote/folder /local/folder
