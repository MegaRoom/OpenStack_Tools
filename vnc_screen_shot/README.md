#vnc_screen_shot
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
  ```
   $ for uuid in `nova list --all- | grep keyword | awk '{print $2}'`; do nova get-vnc-console $uuid novnc | grep novnc | awk '{print $4}'; done
  ```

2. copy urls and paste them to ./take_creen_shot/url_list.txt
  
3. run script
  ```
  cd take_screen_shot/
  ./get_vnc_urls.sh
  ```

#Next step
I will improbe below items.

1. use uuid on the file name of the screen shot
