#!/usr/bin/python2

import sys
import commands


ipName=str(sys.argv[1])
hdfs_str='<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<configuration>\n<property>\n<name>dfs.data.dir</name>\n<value>/data</value>\n</property>\n</configuration>'

fh1=open('/etc/hadoop/hdfs-site.xml','w')
fh1.write(hdfs_str+'\n')
fh1.close()


core_str='<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{}:10001</value>\n</property>\n</configuration>'.format(ipName)
fh2=open('/etc/hadoop/core-site.xml','w')
fh2.write(core_str+'\n')
fh2.close()

commands.getstatusoutput('hadoop-daemon.sh start datanode')
