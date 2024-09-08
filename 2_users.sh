#!/bin/bash
while IFS=, read -r userid userinfo
do 
	IFS=: read -r username userdept <<< "$userinfo"

	echo "User ID: $userid"
	echo "Username: $username"
	echo "Department: $userdept"
	echo ""
done<users.csv







