
google-chrome --proxy-server="127.0.0.1:8080"

Install Burp CA in Chrome (Kali Linux)
In Chrome (through Burp proxy), go to:

http://burp

Download:

cacert.der

convert certificate - openssl x509 -inform DER -in cacert.der -out burp.crt

## Move it to trusted certificate store

sudo cp burp.crt /usr/local/share/ca-certificates/
## Update system trust

sudo update-ca-certificates

## Restart Chrome

Close ALL Chrome windows, then restart.

---

## 🚀 Step 6: Launch Chrome with Burp proxy

google-chrome --proxy-server="127.0.0.1:8080"

google-chrome --proxy-server="127.0.0.1:8080" --proxy-bypass-list="<-loopback>"
