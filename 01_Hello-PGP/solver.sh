#!/bin/sh
# http://www.mieliestronk.com/corncob_lowercase.txt
cat dict.txt | while read line
do
  echo $line;
  printf $line | gpg --passphrase-fd 0 --batch password.asc >> password.txt
done
