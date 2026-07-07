username="admin"
password="Admin@123"
attempt=1

while [ $attempt -le 3 ]
do 
	echo "Enter Username: "
	read username

	echo "Enter Password"
	read -s password
	echo
	if [ "$username" = "$username" ] && [ "$password" =  "$password" ]; then
	echo "Login Successful"
	exit 0
	else
		echo "Invalid Username or Password"
	fi
	attempt=$((attempt + 1))
done
echo "Account Locked"
