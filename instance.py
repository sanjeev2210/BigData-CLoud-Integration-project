#!/usr/bin/python2

import cgi
import commands


print 'Content-Type: text/html'
print

data=cgi.FormContent()['data'][0]
job=cgi.FormContent()['job'][0]
master=cgi.FormContent()['master'][0]
client=cgi.FormContent()['client'][0]


head_data="[data]\n{} ansible_ssh_user=root ansible_ssh_pass=redhat".format(data)
head_name="[master]\n{} ansible_ssh_user=root ansible_ssh_pass=redhat".format(master)
head_job="[job]\n{} ansible_ssh_user=root ansible_ssh_pass=redhat".format(job)
head_client="[client]\n{} ansible_ssh_user=root ansible_ssh_pass=redhat".format(client)

fh3=open('/etc/ansible/hosts','a')
fh3.write(head_data+'\n'+head_name+'\n'+head_job+'\n'+head_client)
fh3.close()



commands.getoutput('sudo ansible-playbook /var/www/cgi-bin/yml-files/name.yml --extra-vars "master={}"'.format(master))
commands.getoutput('sudo ansible-playbook /var/www/cgi-bin/yml-files/job.yml --extra-vars "job={} master={}"'.format(job,master))
commands.getoutput('sudo ansible-playbook /var/www/cgi-bin/yml-files/data.yml --extra-vars "master={} job={}"'.format(master,job))
commands.getoutput('sudo ansible-playbook /var/www/cgi-bin/yml-files/client.yml --extra-vars "job={} master={}"'.format(job,master))


