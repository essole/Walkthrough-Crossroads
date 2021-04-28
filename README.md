# Walkthrough-Crossroads
Walkthrough vulnhub Crossroads 1  machine
Hi guys, through this write-up we'll be talking about all the different process we walkthrough to capture all the flags of Vulnhub Crossroads1 machine.

The machine can be downloaded of this link https://download.vulnhub.com/crossroads/crossroads_vh.ova.
Concerning the virtualisation engine, I used Virtualbox, of course it's the one that is recommended for this machine.

**Here's is the description given from Vulnhub about the machine:**

get flags
difficulty: easy
about vm: tested and exported from virtualbox. dhcp and nested vtx/amdv enabled. you can contact me by email for troubleshooting or questions.
This works better with VirtualBox rather than VMware

**Now that all have been said, let's start:

After starting the machine in virtualbox, we have to look for our target Ip address, so to that we use the command **netdiscover**
![d](https://user-images.githubusercontent.com/63744686/116478438-98007300-a86d-11eb-839f-80d83ad68e55.png)

