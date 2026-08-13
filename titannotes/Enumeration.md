

Passive enumeration -> sublist3r -d akhwien.at || amass enum -passive -d akhwien.at

Active enumeration -> amass - amass enum -active -d akhwien.at
				   ffuf -u https://FUZZ.akhwien.at -w /usr/share/wordlists/subdomains.txt

about:preferences