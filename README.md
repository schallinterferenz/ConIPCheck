# Simple Backdoor Check

The runs a netstat check and analyses the found external ip adresses for any known fraud issues.

Data is retrievied from two APIs:

* spamhaus.org
* ipinfo.io

There is also a list with Trusted Services, which you can customize for your needs.

## Get Started

### Dependencies

* Python 3.11
* Pip Libraries:
  * requests
  * colorama

Install python and run the python script inside this folder

```
python checkLocIPs.py
```
