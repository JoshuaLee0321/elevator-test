# Code Structure:
```bash
.___
    |_scripts
    |       |_elevator.py
    |
    |_client.py
    |_server.py
    |_serverConfig.py
```
# Usage::
```bash
# server...
$ sudo python3 server.py
# client...
$ python3 client.py
```

`command format: <elevator1/2> [[move <floor>] | disp]`
```bash
# for example
elevator1 move 2
elevator2 move 10
elevator1 disp
```