echo "Enter a number"
read num
if [ $num -lt 0 ]
then
echo "number is negetive"
elif [ $num -gt 0 ]
then
echo "number is positive"
else
echo "neither positive or negetive"
fi

