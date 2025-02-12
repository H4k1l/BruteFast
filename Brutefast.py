import requests, threading, argparse, time

parser = argparse.ArgumentParser(description="Brutefast is a static html form bruteforcer. Use multithreading for max velocity in the requests. Useful for testing and ctfs")
parser.add_argument("-d", "--delay", type=int, help="the delay in millisecond between request", default=0)
parser.add_argument("-u", "--url", type=str, help="the url to bruteforce")
parser.add_argument("-f", "--field", type=str, help="the form to bruteforce")
parser.add_argument("-w", "--wordlist", type=str, help="the path of the wordlist")
parser.add_argument("--wizard", action="store_true", help="start the application in wizard mode")
args = parser.parse_args()

def sendReq(word, url, field):
    word = word.strip()
    response = requests.post(url, data={field:word})
    print(f"---\n| Word: {word}\n| Lenght: {len(response.text)}\n| Code: {response.status_code}\n---")

def main():
    if args.wordlist and args.url and args.field and not args.wizard:
        threads = []
        with open(args.wordlist, 'r')as f:
            wordlist = f.readlines()
        for i in wordlist:
            time.sleep(args.delay/1000)
            t = threading.Thread(target=sendReq, args=(i.strip(), args.url, args.field))
            t.start()
            threads.append(t)
        for t in threads:
            t.join()
    elif args.wizard:
        threads = []
        wordlist = input("the path of the wordlist: ")
        url = input("the url: ")
        field = input("the field to bruteforce: ")
        delay = int(input("the delay in millisecond: "))
        with open(wordlist, 'r')as f:
            wordlist = f.readlines()              
        for i in wordlist:
            time.sleep(delay/1000)
            t = threading.Thread(target=sendReq, args=(i, url, field))
            t.start()
            threads.append(t)
        for t in threads:
            t.join()
            
main()