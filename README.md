	Clearclouds fetcher plugin
	The fetcher plugin published and supported by Clearclouds team
	The fetcher plugin enables integrated monitoring of your Local Traffic Manager devices inside of New Relic.
	The fetcher plugin monitor items include:
	TCP
	Throughput: Total, Client side, Server side, Inbound and Outbound
	Latency: Client side, Server side
	CloseStatus: FIN, TIMEOUT, RESET
	New/Close connection : Requests per second
	Retransmited Rate
	Attack: Syn, Scan
	Http
	Throughput : Total, Client side, Server side, Inbound and Outbound
	Latency: Client side, Server side
	StateCode:3XX,4XX,5XX
	Error Rate
	Apdex: user satisfied degree
	Transaction
	Avg response time
	Error Rate
	Apdex : user satisfied degree
	Alert
	Include most 5 alerting items about above all items, each alerting item have caution threshold and critical threshold, when the item value more than Caution threshold, new relic platform raise a caution alerting in GUI, and when the item value more than critical threshold, new relic platform raise a critical alerting in GUI.
	Alerting frequency is once per 30 minute.
	New relic platform will send you a email when alert, if you configure this function.


	Requirement
	OS : CentOS6.2 64Bits or later
	Disk : more than 50G
	Memory : more than 1G
	Software : Python 2.6 or later
	cx_freeze-4.3.3 or later

	iProbe.zip download URL : http://www.clearclouds.com/upload/iProbe-VM-1.0-20150205.zip
	About URL : http://www.clearclouds.com/about/
	Surport URL : http://www.clearclouds.com/service/
	fetcher Download  URL:  https://github.com/StevenLeee/fetcher.git
	How to Install iProbe in Virtual Machine Environment
	This document describes how to install iProbe in Virtual Machine (VM) environment. The released iso file includes both Linux OS and iProbe system.
	We recommend installing the system on Oracle Virtual Box and VMware Player.
	Requirements.
	OS
	Recommended OS is "Red Hat/Centos 6.x(64 bit) Linux", 6.4 is preferred.

	Hardware
	Hard disk        at least 50GB
	Memory           no less then 1GB
	CPU cores        1 or 2


	Installing P-100

	VM time zone settings
	The time zone is "UTC".
	Configure NIC
	Choose one NIC then set the "Bridged Adapter" mode.
	Set NIC running in a promiscuous mode and choose "allow both".

	Set boot device
	Choose the CD/DVD as the default boot device.

	Mount ISO file.
	Configure the IDE controller, add ISO file to the list. (file name: iProbe-VM-xxxx.iso)

	Install the system
	The VM will install the Linux OS including iProbe system automatically.


	Configure iProbe system
	Logging on system
	Logging on the system as root with the password "pProbejy"

	Set an IP for your system
	You may follow the command below:

	vim /etc/sysconfig/network-scripts/ifcfg-ethX  (where X represents the network interface)

	###Here attached a sample for editing the cfg-file.
	#================================================#
	DEVICE=eth0
	HWADDR=68:05:CA:**:**:**
	TYPE=Ethernet
	BOOTPROTO=static
	IPADDR=192.168.10.228
	GATEWAY=192.168.10.1
	DNS1=8.8.8.8
	IPV4_FAILURE_FATAL=yes
	IPV6INIT=no
	UUID=f9a0578b-39c9-456b-b225-***
	ONBOOT=yes
	#================================================#
	Note: This interface works as both network-serve and traffic capturing ports. However, you can configure an extra port for traffic capturing as well.

	service network restart

	Configure time zone settings (optional)
	Follow the commands below to change your system's timezone setting if you have to do.

	cp /usr/share/zoneinfo/America/Los_Angeles /ect/localtime (take Los_Angeles for instance)
	sed -i s/PRC/America\/Los_Angeles/g” /usr/local/php/etc/php.ini
	hwclock –w

	Verify NTP Daemon Operation for Network Data Collection
	vim /etc/ntp.conf
	======================================================================
	#server 0.centos.pool.ntp.org
	#server 1.centos.pool.ntp.org
	#server 2.centos.pool.ntp.org
	restrict  192.168.100.254
	server 192.168.100.254     (e.g.)
	======================================================================
	/etc/init.d/ntpd start
	chkconfig ntpd on

	Restart the iprobe system
	service pprobe restart


	Log on the GUI console
	Open your browser and import the URL.(http://192.168.10.228) The URL depends on the IP of your
	has been configured above.
	Enter the configuration menu and start or shutdown the monitor engine.
	(Config->Monitor Engine,click start or stop button)

	Notes:
	The system will listen to the eth0 port by default. You can customize the listened port by modifying the pprobe.cfg file (/usr/local/etc/pprobe.cfg) and change the value of interface. (["eth1"] e.g.)

	Please separate the different ports by a comma when you need to listen to more ports.(["eth0","eth1"] e.g.)

	If you have any question,please contact us.
	===========================================================
	Silicon Valley Office
	1601 McCarthy Blvd, Milpitas, CA 95035
	Tel: 408-883-5418
	Email: info@clearclouds.com
	============================================================

	Install fetcher.zip
	after download the file fetcher.zip from https://github.com/StevenLeee/fetcher.git
	enter download directory
	unzip  fetcher.zip
	cd fetcher
	chmod -R 777  ./*
	python setup.py install
	configuration
	run fetcher only once:
	fetcher  -d datadir  -n pluginid  -k newrelickey
	here :
	datadir  :  your data directory
	pluginid  :  your plugin name, generally server name
	newrelickey  :  your license key from your New Relic account.
	e.g :
	fetcher -d /home/juyun/datafile  -n ClearClouds -k 19e5cb7a2ec9c43a7a90cec3360fb7b5868d08d6
	until print message as below:
	datadir= home/juyun/datafile
	pluginid= ClearClouds
	newrelickey=19e5cb7a2ec9c43a7a90cec3360fb7b5868d08d6

	Execute fetcher
	fetcher -r
