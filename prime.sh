
echo "enter limit"
read a b
echo "prime numbers are"
for (( i=$a ; i<=$b ; i++ ))
do
f=0
for (( j=2 ; j=<$i ; j++ ))
do
if [ `expr $i % $j` -eq 0 ]
then 
f=1
break
fi
done
if [ $f -eq 0 ]
then 
echo "$i"
fi
done

