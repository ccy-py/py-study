import telnetlib
try:
    telnetlib.Telnet('127.0.0.1', port='81', timeout=10)
except:
    print('connect failed')
else:
    print('success')
