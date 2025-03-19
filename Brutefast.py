import requests, argparse, time
from concurrent.futures import ThreadPoolExecutor

parser = argparse.ArgumentParser(description="Brutefast is a static html form bruteforcer. Use multithreading for max velocity in the requests. Useful for testing and ctfs")
parser.add_argument("-d", "--delay", type=int, help="the delay in millisecond between request", default=0)
parser.add_argument("-u", "--url", type=str, help="the url to bruteforce")
parser.add_argument("-f", "--field", type=str, help="the form to bruteforce")
parser.add_argument("-w", "--wordlist", type=str, help="the path of the wordlist")
parser.add_argument("-c", "--cookies", type=str, help="the path of the cookies")
parser.add_argument("-mw", "--maxworkers", type=int, help="the max number of thread", default=5)
parser.add_argument("--wizard", action="store_true", help="start the application in wizard mode")
parser.add_argument("--pure", action="store_true", help="use the pure-bruteforcing technique")
parser.add_argument("-mx", "--maxlenght", type=int, help="the max lenght of the bruteforcing")
parser.add_argument("-ml", "--minlenght", type=int, help="the min lenght of the bruteforcing", default=1)
parser.add_argument("-ch", "--charset", type=str, help="the charset for building the words 'abc123'")

args = parser.parse_args()

def loadcookies(path):
    cookies = {}
    with open(path, 'r') as file:
        for l in file:
            l = l.strip()
            key, value = l.split('=', 1)
            cookies[key.strip()] = value.strip()
    return cookies

def sendReq(word, url, field, cookies):
    word = word.strip()
    response = requests.post(url, data={field:word}, cookies=cookies)
    print(f"---\n| Word: {word}\n| Lenght: {len(response.text)}\n| Code: {response.status_code}\n---")

def bruteReq(mxlenght, minlenght, chars, url, field, delay, mxworkers, cookies):
    with ThreadPoolExecutor(max_workers=mxworkers) as executor:
        while True:
            time.sleep(delay/1000)
            total = len(chars) ** minlenght
            futures = []
            for n in range(total):
                word = ""
                temp = n
                for _ in range(minlenght):
                    word = chars[temp % len(chars)] + word
                    temp //= len(chars)
                futures.append(executor.submit(sendReq, word, url, field, cookies))
            for future in futures:
                future.result()
            if mxlenght and mxlenght == minlenght:
                break
            else: 
                minlenght += 1   
                 
def main():
    if args.pure and args.url and args.field:
        cookies = loadcookies(args.cookies)
        if not args.charset: charset = ''.join(chr(i) for i in range(32, 127))
        else: charset = args.charset
        bruteReq(args.maxlenght, args.minlenght, charset, args.url, args.field, args.delay, args.maxworkers, cookies)
    if args.wordlist and args.url and args.field and not args.wizard and not args.pure:
        cookies = loadcookies(args.cookies)
        with open(args.wordlist, 'r')as f:
            wordlist = f.readlines()
        with ThreadPoolExecutor(max_workers=args.maxworkers) as executor:
            futures = []
            for i in wordlist:
                time.sleep(args.delay/1000)
                futures.append(executor.submit(sendReq, i.strip(), args.url, args.field, cookies))
            for future in futures:
                future.result()
    elif args.wizard:  
        pure = input("pure bruteforcing? y/n: ").lower()
        if not pure == 'y': wordlist = input("the path of the wordlist: ")
        else: 
            maxlenght = int(input("the max lenght of the bruteforcing: "))
            minlenght = int(input("the min lenght of the bruteforcing: "))
            chars = input("the charset for building the words 'abc123': ")
        url = input("the url: ")
        field = input("the field to bruteforce: ")
        cookies = input("the path of the cookies: ")
        cookies = loadcookies(cookies)
        delay = int(input("the delay in millisecond: "))
        maxworkers = int(input("the max number of thread: "))
        if not pure == 'y':
            with open(wordlist, 'r')as f:
                wordlist = f.readlines()  
            with ThreadPoolExecutor(max_workers=maxworkers) as executor:
                futures = []
                for i in wordlist:
                    time.sleep(delay/1000)
                    futures.append(executor.submit(sendReq, i.strip(), url, field, cookies))
                for future in futures:
                    future.result()
        else: 
            if not chars: charset = ''.join(chr(i) for i in range(32, 127))
            else: charset = chars
            bruteReq(maxlenght, minlenght, charset, url, field, delay, maxworkers, cookies)       
main()
