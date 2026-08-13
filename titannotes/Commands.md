
whoami/ hostname
date
pwd - present working directory
history
ls -la /tmp
ls ---> listing
la -a --> to view hidden files
ls -l --> long listing
ls -l -h ---> human readable files / ls -lh
cat /etc/passwd
cat>dummy.txt

rwx - read, write, execute
to add contents --> cat>>dummy.txt
to merge files --> cat d1.txt dummy.txt > merged.txt
tmp folder --> ls -la/tmp
to search for some content -> grep 'word' out.txt .. add (-n) for numbering
wc- word count
wc -w out.txt
wc -l [file name]

Copying files & Directories ---> cp

cp [filename] [filename]

copying multiple files
cp -r [filename] [foldername] [name of path]

change mode
chmod +rwx [filename]  || chmod 777 [filename]

Add/Create user
sudo adduser [username]
switch users
su [username]

IPs
ip addr show | ip a
iwconfig
ip n | arp -a ---> 
ip r | route


nmap -sP ==> sP for scan and Ping
nmap -sP [website name] eg scanme.nmap.org

touch [filename] ==> to create a file

**Start and Stop Apache Server**
sudo service apache2 start
sudo service apache2 stop

**Starting server using python**
python3 -m http.server 80

**Starting service as soon as the machine starts**
sudo systemctl enable ssh --> to disable sudo systemctl disable ssh

sudo apt update && apt upgrade
switch user to root -> sudo su -


basic DNS tools, such as the **nslookup**, **host**, and **dig**

**To Request an IP Address**
sudo dhclient eth0

the **whois** command is used to retrieve the organization name, technical and administrative contacts
whois [IP address]

For a Reverse DNS lookup ---> dig -x 8.8.8.8


