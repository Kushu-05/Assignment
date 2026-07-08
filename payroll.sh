tax_calc(){
	if [[ $1 -le 30000 ]]
	then
		tax=$(( $1 *5 / 100))
	elif [[ $1  -le 60000 ]]
	then
		tax=$(( $1 * 10 / 100 ))
	else
		tax=$(( $1 * 15 / 100 ))
	fi
}
bonus_calc(){
	if [ $1 -le 50000 ]
	then
		bonus=2000
	else
		bonus=5000
	fi
}
net_salary(){
net=$(( $1 -tax + bonus ))
}
echo "Enter employee file:"
read file 

if [ ! -f "$file" ]
then 	
	echo "File not found"
	exit
fi
echo "ID Name Salary Tax Bonus Netsalary" > payroll_report.txt
while read id name salary
do
	tax_calc $salary
	bonus_calc $salary
	net_salary $salary


echo " $id $name $salary $tax $bonus  $net" >> payroll_report.txt
done < "$file"
echo "Payroll report"
echo "Payroll Report" > payroll_repot.tx 

