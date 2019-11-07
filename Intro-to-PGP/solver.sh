#!/bin/sh
gpg --import gpg.pub
cat cipher.txt | gpg -d >message.txt

