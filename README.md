# Walkthrough-Crossroads
###Walkthrough vulnhub Crossroads 1  machine###
Hi guys, through this write-up we'll be talking about all the different process we walkthrough to capture all the flags of Vulnhub Crossroads1 machine.

The machine can be downloaded of this link https://download.vulnhub.com/crossroads/crossroads_vh.ova.
Concerning the virtualisation engine, I used Virtualbox, of course it's the one that is recommended for this machine.

**Here's is the description given from Vulnhub about the machine:**

* get flags
* difficulty: easy
* about vm: tested and exported from virtualbox. dhcp and nested vtx/amdv enabled. you can contact me by email for troubleshooting or questions.
* This works better with VirtualBox rather than VMware

**Now that all have been said, let's start:**

After starting the machine in virtualbox, we have to look for our target Ip address, so to that we use the command **netdiscover**

![d](https://user-images.githubusercontent.com/63744686/116478438-98007300-a86d-11eb-839f-80d83ad68e55.png)

As you can see on the image, our target Ip address is **192.168.56.107**
but we'll be using as attacker Ip address **192.168.56.108**

Now then, let's poursue by enumerating services and ports that the target machine is running by using **nmap** command

**nmap -A -Pn- 192.168.56.107**

![d1](https://user-images.githubusercontent.com/63744686/116479614-7b653a80-a86f-11eb-94b6-de2fc8c2f305.png)


With the output of nmap command, it's shows that the target machine is running http server and smb server as well.
Knowing that, we'll continue our journey by web enumeration in other to gather more information and see if there isn't some interesting files on the web server.
so to that, we use **dirb** command to check eventuals files that might be stored on the web server

**dirb http://192.168.56.107**

![d2](https://user-images.githubusercontent.com/63744686/116480687-4fe34f80-a871-11eb-9c0d-2877c158a156.png)





