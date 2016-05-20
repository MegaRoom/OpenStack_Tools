#vnc_screen
Sometimes, I would like to save the VM's before doing operation
to make sure VM was not affected with the operation.

It is difficult to check with accessing each 
because
1. possibility touch/moving in OS  2. troublesome to access each VNC URL.

This script automate that

##Requirement
- python 2.7

- firefox

- selenium 2.53.2 (python library)

#How to use this script
1. get urls by using 
  ```./get_vnc_urls.sh```

2. copy and paste url_list to 
  ```cp ./get_urls/url_list.txt ./take_screen_shots/url_list.txt
  
3. take screenshot
  ```./get_vnc_urls.sh```

#Next step
I will improbe below items.

1. use uuid on the file name of the screen shot

2. automate everything (one command do getting url and taking screenshot)
