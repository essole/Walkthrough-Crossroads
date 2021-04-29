# Walkthrough-Crossroads
Walkthrough vulnhub Crossroads 1  machine

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

So looking on image, it's possible to see that, there are somes files on the web server. While checking the content of the robot.txt file, it's mentioned inside that
the route /crossroad.png is disabled. Of course, our first impression might be to suppose that file should contain the first flag, but looking at it, it's not

![d3](https://user-images.githubusercontent.com/63744686/116487908-a441fb80-a880-11eb-8502-a1c2812943f1.png)

So then, as I said earlier, I first download the file and try to see if it's possible that something was hiden inside. To that I used a python package called **stegoveritas** to extract everthing that the picture might hide. If you do want to install the package stegoveritas on your python environnement, you just have to do **pip3 install stegoveritas** 
and there you go.
**stegoveritas crossroads.png**

![d4](https://user-images.githubusercontent.com/63744686/116488509-0c451180-a882-11eb-9d4e-1fa13ba80b4f.png)

When the file is done extracting, you'll find in your curent directory a new directory created and named **results**. Inside this one, there's another directory named keepers in which there are somes files and among those file we find a wordlist, with it what we might expect is that soon it should come in handy while try to do a brute force attack.
bellow the wordlist file captured

![d5](https://user-images.githubusercontent.com/63744686/116489113-9e014e80-a883-11eb-92b6-816f0a52ea79.png)

Now let's save this wordlist in our repository

![d6](https://user-images.githubusercontent.com/63744686/116489011-5da1d080-a883-11eb-9570-ecc135123f74.png)

After that, we are sure there is no more interesting thing on the side, we can head to smb server side. There, we start as usually with the smb server enumeration.
First, we'll check the shared directories on the server their access permission by using **smbmap** command

**smbmap -H 192.168.56.107**

![d7](https://user-images.githubusercontent.com/63744686/116489436-7bbc0080-a884-11eb-9199-1c311ef0a597.png)

As we can see on the image, all the shared directories have **no access** permission a guest user. So we have to look for a user who has somehow an access to one of the shared 
directories. To that, we can use **enum4linux** or nmap smb enumeration script, but in my case I used enum4linux to find another user who has access to the smb server. Below the command that used

**enum4linux 192.168.56.107**

![d8](https://user-images.githubusercontent.com/63744686/116489998-ddc93580-a885-11eb-9bb1-e36702fe5d37.png)

The image beyond shows a fragment of the output of enum4linux command, and we can see on it that there's another user called **albert** on the target machine. Knowing that, let's try to find his credentials and enumerate the access he might have on the shared directories. We can use a banch of tools to brute force smb creds but in my case I used metasploit **auxiliary scanner/smb/smb_login**. 
Using the metasploit auxiliary I just mentionned, we must set our options as shown on the image below

![d9](https://user-images.githubusercontent.com/63744686/116490646-6f857280-a887-11eb-9235-918a7d2b89ad.png)

At the of the execution we'll find as result

![d10](https://user-images.githubusercontent.com/63744686/116490749-a9567900-a887-11eb-88bb-b3b1ae50d987.png)

Now that we have the user albert creds, we can try to enumerate the kind of access he has on the shared directories with the command below

**smbmap -H 192.168.56.107 -u albert -p bradley1**

![d11](https://user-images.githubusercontent.com/63744686/116490831-ec185100-a887-11eb-8e58-ebbc670bd6b3.png)






