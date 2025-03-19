# BruteFast
----
Brutefast is a simple and fast static html form bruteforcer. Use multithreading for max velocity in the requests. Useful for testing and CTFs
# Screenshots
----
![BruteFast](https://github.com/H4k1l/BruteFast/blob/main/images/screenshot1.png)
# Usage
----
  ```
python3 Brutefast.py -h
  usage: BrutefastV2.py [-h] [-d DELAY] [-u URL] [-f FIELD] [-w WORDLIST]
                      [-c COOKIES] [-mw MAXWORKERS] [--wizard] [--pure]
                      [-mx MAXLENGHT] [-ml MINLENGHT] [-ch CHARSET]

Brutefast is a static html form bruteforcer. Use multithreading for max
velocity in the requests. Useful for testing and ctfs

options:
  -h, --help            show this help message and exit
  -d DELAY, --delay DELAY
                        the delay in millisecond between request
  -u URL, --url URL     the url to bruteforce
  -f FIELD, --field FIELD
                        the form to bruteforce
  -w WORDLIST, --wordlist WORDLIST
                        the path of the wordlist
  -c COOKIES, --cookies COOKIES
                        the path of the cookies
  -mw MAXWORKERS, --maxworkers MAXWORKERS
                        the max number of thread
  --wizard              start the application in wizard mode
  --pure                use the pure-bruteforcing technique
  -mx MAXLENGHT, --maxlenght MAXLENGHT
                        the max lenght of the bruteforcing
  -ml MINLENGHT, --minlenght MINLENGHT
                        the min lenght of the bruteforcing
  -ch CHARSET, --charset CHARSET
                        the charset for building the words 'abc123'
```
# Disclaimers
----
The author is not responsible for any damages, misuse or illegal activities resulting from the use of this code.
