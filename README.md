# proxmox

Telegram notification

v 0.0.0.1-alpha
- create a telegram bot
- create a telegram group/channel
- add the bot to the group/channel
- install syslog-ng
- save pve.conf to /etc/syslog-ng/conf.d/
- create /opt/pvetelegram/bin/
- save pvetelegram_parse.py and pvetelegram_sendmsg.sh to /opt/pvetelegram/bin/
- edit pvetelegram_parse.py and pvetelegram_sendmsg.sh and change TELEGRAM_BOT_TOKEN and CHAT_ID
- chmod 755 on pvetelegram_parse.py and pvetelegram_sendmsg.sh
- enable and start/reload syslog-ng

TODO
- clean code
- conditional message for different tasks types
- add translation 
- autoinstall

![Screenshot from 2025-01-06 16-15-09](https://github.com/user-attachments/assets/b02c6895-97e1-467f-800f-12605d2eae0b)
