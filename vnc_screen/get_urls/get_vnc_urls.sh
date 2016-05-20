#/bin/bash

# clean url
echo '' > url_list.txt

# put url to text file
for uuid in `nova list --host=${TARGET_HOST} --all- | grep ACTIVE | awk '{print $2}'` 
do 
nova get-vnc-console $uuid novnc | grep novnc | awk '{print $4}'
done
