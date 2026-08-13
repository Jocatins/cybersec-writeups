
physical engagement 
phishing
location info -> drone recon - building layout
work badge photos
actually going on site

Web/ host
target validation -> 

data breaches ->

Steps in performing an installation for Gedit
sudo apt update -----------------------
sudo apt full-upgrade -y                     |
sudo apt install gedit -y                      |
							|
		for PUB KEY => sudo apt install kali-archive-keyring -y -> 
	download the key =>	wget https://archive.kali.org/archive-key.asc -O kali-archive-key.asc
convert new keyring format => gpg --dearmor -o kali-archive-keyring.gpg kali-archive-key.asc
Move it to the trusted keyrings folder	=> sudo mv kali-archive-keyring.gpg /usr/share/keyrings/ update sources list  ===> sudo nano /etc/apt/sources.list
 to this ==> deb [signed-by=/usr/share/keyrings/kali-archive-keyring.gpg] http://http.kali.org/kali kali-rolling main contrib non-free
