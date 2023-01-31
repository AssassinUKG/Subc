# Subc
A subdomin bruteforce tool

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

Normal usage
```sh
python3 subc.py -d tesla.com -w /usr/share/seclists/Discovery/DNS/deepmagic.com-prefixes-top50000.txt -o results.txt
```

Silent usage (only returns domains, for use with tools like tee etc)
```sh
python3 subc.py -d tesla.com -w /usr/share/seclists/Discovery/DNS/deepmagic.com-prefixes-top50000.txt -o results.txt -s
```
