<p align="center">
  <img src="https://user-images.githubusercontent.com/5285547/215763561-de33d4f6-3149-463a-8143-62137938902a.png" alt="Sublime's custom image"/>
</p>

## Video 
(Click to goto YouTube.com)
[![image](https://user-images.githubusercontent.com/5285547/215758367-043c6e69-8adb-4051-85a7-9c2ceb876d93.png))](https://www.youtube.com/watch?v=6bdE_BOxPbM)

## Install

```sh
git clone https://github.com/AssassinUKG/Subc.git
cd subc
pip install -r requirements.txt
```

## Usage

```sh
usage: subc.py [-h] -d DOMAIN -w WORDLIST [-o OUTPUT] [-t THREADS] [-s]

options:
  -h, --help            show this help message and exit
  -d DOMAIN, --domain DOMAIN
                        Domain to brute force
  -w WORDLIST, --wordlist WORDLIST
                        DNS wordlist to use
  -o OUTPUT, --output OUTPUT
                        Output file to save the results to
  -t THREADS, --threads THREADS
                        Number of threads to use (Default: 80)
  -s, --silent          Silent mode - Hide all output, except domains
```

Normal usage
```sh
python3 subc.py -d tesla.com -w /usr/share/seclists/Discovery/DNS/deepmagic.com-prefixes-top50000.txt -o results.txt
```

Silent usage (only returns domains, for use with tools like tee etc)
```sh
python3 subc.py -d tesla.com -w /usr/share/seclists/Discovery/DNS/deepmagic.com-prefixes-top50000.txt -o results.txt -s
```
