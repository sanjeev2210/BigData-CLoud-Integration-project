#!/usr/bin/python2

import sys
import commands

ipJob=str(sys.argv[1])
ipName=str(sys.argv[2])



mapred_str='<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<configuration>\n<property>\n<name>mapred.job.tracker</name>\n<value>{}:9001</value>\n</property>\n</configuration>'.format(ipJob)

fh=open('/etc/hadoop/mapred-site.xml','w')
fh.write(mapred_str+'\n')
fh.close()

core_str='<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{}:10001</value>\n</property>\n</configuration>'.format(ipName)
fh2=open('/etc/hadoop/core-site.xml','w')
fh2.write(core_str+'\n')
fh2.close()
