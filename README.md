
Clearclouds fetcher plugin

1           The fetcher plugin published and supported by Clearclouds team

2           The fetcher plugin enables integrated monitoring of your Local Traffic Manager devices inside of New Relic.

3           The fetcher plugin monitor items include:

3.1          TCP

3.1.1     Throughput: Total, Client side, Server side, Inbound and Outbound

3.1.2     Latency: Client side, Server side

3.1.3     CloseStatus: FIN, TIMEOUT, RESET

3.1.4     New/Close connection : Requests per second

3.1.5     Retransmited Rate

3.1.6     Attack: Syn, Scan

3.2          Http 

3.2.1     Throughput : Total, Client side, Server side, Inbound and Outbound

3.2.2     Latency: Client side, Server side

3.2.3     StateCode:3XX,4XX,5XX

3.2.4     Error Rate

3.2.5     Apdex: user satisfied degree

3.3          Transaction

3.3.1     Avg response time

3.3.2     Error Rate

3.3.3     Apdex : user satisfied degree

3.4          Alert

         Include most 5 alerting items about above all items, each alerting item have caution threshold and critical threshold, when the item value more than Caution threshold, new relic platform raise a caution alerting in GUI, and when the item value more than critical threshold, new relic platform raise a critical alerting in GUI.

         Alerting frequency is once per 30 minute.

         New relic platform will send you a email when alert, if you configure this function.

 

 

4           Requirement

         OS : CentOS6.2 64Bits or later

         Disk : more than 50G

         Memory : more than 1G

         Software : Python 2.6 or later

                             cx_freeze-4.3.3 or later

 

5           iProbe.zip download URL : http://www.clearclouds.com/upload/iProbe-VM-1.0-20150205.zip

6           About URL : http://www.clearclouds.com/about/

7           Surport URL : http://www.clearclouds.com/service/

8           fetcher Download  URL:  https://github.com/StevenLeee/fetcher.git

9           How to Install iProbe in Virtual Machine Environment

         This document describes how to install iProbe in Virtual Machine (VM) environment. The released iso file includes both Linux OS and iProbe system.

         We recommend installing the system on Oracle Virtual Box and VMware Player.

9.1          Requirements.

9.1.1     OS 

                        Recommended OS is "Red Hat/Centos 6.x(64 bit) Linux", 6.4 is preferred. 

 

9.1.2     Hardware      

                        Hard disk        at least 50GB 

                        Memory           no less then 1GB

                        CPU cores        1 or 2

   

 

9.2          Installing P-100 

 

9.2.1     VM time zone settings

  The time zone is "UTC".

9.2.2     Configure NIC

  Choose one NIC then set the "Bridged Adapter" mode.

  Set NIC running in a promiscuous mode and choose "allow both".

 

9.2.3     Set boot device

  Choose the CD/DVD as the default boot device.

 

9.2.4     Mount ISO file.

   Configure the IDE controller, add ISO file to the list. (file name: iProbe-VM-xxxx.iso)

   

9.2.5     Install the system

  The VM will install the Linux OS including iProbe system automatically.

 

  

9.3          Configure iProbe system

9.3.1     Logging on system

  Logging on the system as root with the password "pProbejy" 

  

9.3.2     Set an IP for your system

  You may follow the command below:

  

  a) vim /etc/sysconfig/network-scripts/ifcfg-ethX  (where X represents the network interface)

  

  ###Here attached a sample for editing the cfg-file.

  #=================#

    DEVICE=eth0

    HWADDR=68:05:CA:**:**:**

    TYPE=Ethernet

    BOOTPROTO=static

    IPADDR=192.168.10.228   

    GATEWAY=192.168.10.1

    DNS1=8.8.8.8

    IPV4_FAILURE_FATAL=yes

    IPV6INIT=no

    UUID=f9a0578b-39c9-456b-b225-***

    ONBOOT=yes

  #==================#

     Note: This interface works as both network-serve and traffic capturing ports. However, you can configure an extra port for traffic capturing as well.

    

    b) service network restart

    

9.3.3     Configure time zone settings (optional)

   Follow the commands below to change your system's timezone setting if you have to do.

   

  a) cp /usr/share/zoneinfo/America/Los_Angeles /ect/localtime (take Los_Angeles for instance)

  b) sed -i s/PRC/America\/Los_Angeles/g” /usr/local/php/etc/php.ini

  c) hwclock –w

  

9.3.4     Verify NTP Daemon Operation for Network Data Collection

   a) vim /etc/ntp.conf

 =================

  #server 0.centos.pool.ntp.org

  #server 1.centos.pool.ntp.org

  #server 2.centos.pool.ntp.org

  restrict  192.168.100.254  

  server 192.168.100.254     (e.g.)

 ==============

   b) /etc/init.d/ntpd start

   c) chkconfig ntpd on

  

9.3.5     Restart the iprobe system

  service pprobe restart

  

 

9.3.6     Log on the GUI console

9.3.6.1    Open your browser and import the URL.(http://192.168.10.228) The URL depends on the IP of your

                            has been configured above.

9.3.6.2    Enter the configuration menu and start or shutdown the monitor engine.

 (Config->Monitor Engine,click start or stop button) 

 

9.3.7     Notes:

         The system will listen to the eth0 port by default. You can customize the listened port by modifying the pprobe.cfg file (/usr/local/etc/pprobe.cfg) and change the value of interface. (["eth1"] e.g.)

 

         Please separate the different ports by a comma when you need to listen to more ports.(["eth0","eth1"] e.g.)

 

         If you have any question,please contact us.

====================

Silicon Valley Office                  

1601 McCarthy Blvd, Milpitas, CA 95035 

Tel: 408-883-5418                      

Email: info@clearclouds.com            

====================

 

10          Install fetcher.zip

10.1       after download the file fetcher.zip from https://github.com/StevenLeee/fetcher.git

10.2       enter download directory

10.3       unzip  fetcher.zip

10.4       cd fetcher

10.5       chmod -R 777  ./*

10.6       python setup.py install

11       configuration

11.1       run fetcher only once:

                  fetcher  -d datadir  -n pluginid  -k newrelickey

                   here :

                  datadir  :  your data directory

                  pluginid  :  your plugin name, generally server name

                  newrelickey  :  your license key from your New Relic account.

11.2       e.g :

                  fetcher -d /home/juyun/datafile  -n ClearClouds -k 19e5cb7a2ec9c43a7a90cec3360fb7b5868d08d6

         until print message as below:

                  datadir= home/juyun/datafile

                  pluginid= ClearClouds

                  newrelickey=19e5cb7a2ec9c43a7a90cec3360fb7b5868d08d6

 

12       Execute fetcher

         fetcher -r
