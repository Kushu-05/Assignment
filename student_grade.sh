echo "Enter marks for Subject1"
read sub1
echo "Enter marks for Subject2"
read sub2
echo "Enter marks for Subject3"
read sub3
echo "Enter marks for Subject4"
read sub4
echo "Enter marks foe Subject5"
read sub5

total=$((sub1+sub2+sub3+sub4+sub5))
echo "Total marks ${total}"
avg=$((total/5))
 echo "Average marks ${avg}"
if [[ $avg -ge 90 ]]; then
	grade=A
elif [[ $avg -ge 75 ]]; then
	grade=B
elif [[ $avg -ge 60 ]]; then
	grade=C
elif [[ $avg -ge 50 ]]; then
	grade=D
else
	grade="Fail"
fi

echo "Your grade is ${grade}"
