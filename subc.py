#!/usr/env/bin python3
import requests 
import threading
import argparse
from urllib3 import exceptions 
import gc
import signal



##################################################
# Created by Richard Jones @defencelogic.io      #
# Date: 31/01/2023                               #
##################################################

def main():

    def handler(signum, frame):
        try:
            print(f"{colors['red']}[-]{colors['white']} Application Exiting...{colors['reset']}")
            exit(0)
        except Exception:
            pass

    try:
        signal.signal(signal.SIGINT, handler)
    except Exception:
        pass

    requests.packages.urllib3.disable_warnings()
    
    colors: dict = {
            "red": "\033[31m",
            "green": "\033[32m",
            "yellow": "\033[33m",
            "blue": "\033[34m",
            "magenta": "\033[35m",
            "cyan": "\033[36m",
            "white": "\033[37m",
            "reset": "\033[0m"
        }

    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--domain', help='Domain to brute force', required=True)
    parser.add_argument('-w', '--wordlist', help='DNS wordlist to use', required=True)
    parser.add_argument('-o', '--output', help='Output file to save the results to')
    parser.add_argument("-t", "--threads", help="Number of threads to use (Default: 80)", type=int, default=80)
    parser.add_argument("-s", "--silent", help="Silent mode - Hide all output, except domains", action="store_true", default=False)
    args = parser.parse_args()
    THREAD_LIMITER = threading.BoundedSemaphore(value=args.threads)

    if not __import__("sys").stdout.isatty():
        for _ in dir():
            if isinstance(_, str) and _[0] != "_":
                locals()[_] = ""
    else:
        # set Windows console in VT mode
        if __import__("platform").system() == "Windows":
            kernel32 = __import__("ctypes").windll.kernel32
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
            del kernel32

    banner = """\n #####         ##       ####
##   ##        ##      ##  ##
##      ##  ## ## ##  ##
####    ##  ## ### ## ##
 #####  ##  ## ##  ## ##
   #### ##  ## ##  ## ##
     ## ##  ## ##  ## ##
##   ## ## ### ### ##  ##  ##
 #####   ## ## ## ##    ####"""

    if not args.silent:
        print(f"{colors['green']}{banner}{colors['reset']}")
        print(f"{colors['white']}The Domain BruteForce Tool\n{colors['reset']}")
        print(f"{colors['white']}Developed by:{colors['green']} richard@defencelogic.io{colors['reset']}")
        print(f"{colors['white']}Version:{colors['green']} 1.0{colors['reset']}\n")
        print(f"{colors['green']}[+]{colors['white']} Starting subdomain brute force on {colors['yellow']}{args.domain}{colors['reset']}")
    if not args.output and not args.silent:
        print(f"{colors['red']}[-]{colors['white']} No output file specified!{colors['reset']}\n")
        exit(0)
    if args.output and not args.silent:
        print(f"{colors['green']}[+]{colors['white']} Saving results to {colors['cyan']}{args.output}{colors['reset']}\n")
    
    
    def test_subdomain(subdomain):
        THREAD_LIMITER.acquire()
        url = f"https://{subdomain}"
        try:
            r = requests.get(url, verify=False)        
        except requests.ConnectionError:
            pass
        except requests.exceptions.InvalidURL:
            pass
        except exceptions.LocationParseError:
            pass
        except:
            pass
        else:
            if args.silent:
                print(f"{subdomain}")
            else:
                print(f"{colors['green']}[*]{colors['white']} Discovered: {colors['cyan']}{subdomain}{colors['reset']}")
                # a+ appends to the file even if its been opened before (also creates the file if it doesnt exist)
                if args.output:
                    with open(args.output, 'a+') as output_file:
                        output_file.write(f"{subdomain}")
        finally:
            THREAD_LIMITER.release()
    
    try:                    
        with open(args.wordlist, 'r', encoding='Latin-1') as wordlist_file:
            for line in wordlist_file:
                word = line.strip()
                subdomain = f"{word}.{args.domain}"
                t = threading.Thread(target=test_subdomain, args=(subdomain,))
                t.daemon = True
                t.start()
                gc.collect()
    except Exception:
        pass

if __name__ == "__main__":
    main()
