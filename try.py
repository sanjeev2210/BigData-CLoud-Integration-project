#!/usr/bin/python

import cgi

print 'Content-Type: text/html'
print


data='192.168.43.60'

master='192.168.43.61'

head_data="[data]\n{} ansible_ssh_user=root ansible_ssh_pass=redhat".format(data)
head_name="[master]\n{} ansible_ssh_user=root ansible_ssh_pass=redhat".format(master)
fh=open('/etc/ansible/hosts','a')
fh.write(head_data+'\n'+head_name)
fh.close()
