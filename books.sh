file="books.txt"
#To view the books
view_book(){
cat $file
}
#To search the books
search_book(){
	echo "Enter the book name: "
	read name
	grep -i "$name" "$file"
}
  
# count the books that are out of stock
count_out_of_stock(){
grep -c "Out of stock" "$file"
}


#Upadate the stock status
update_stock(){
	echo "Enter the book ID: "
	read id
	echo "Enter New Status ( InStock / out of stock):"
	read status
	sed -i "/^$id,/s/Instock/outofstock/" "$file"
	echo "Stock Updated Successfully"
}
#Calculate the total inventory value
inventory_value(){
	awk -F'|' '{sum+=$4*$5} END {print sum}' "$file"
	
}
#Display books by category 
books_category(){
	echo "Enter category: "
	read cat
	awk -F'|' -v c="$cat" '$3==c{print}' "$file"
}
#Finding the costliest books 
costliest_books(){
	awk -F'|' '
	BEGIN { max=0 }

	{
		if($4>max){
			max=$4
			book=$2
		}
	}
	END{
		print "Costliest Book :",book
		print "Price:",max
	}' "$file"
}

#Menu
 while true
do
echo
echo "==========="
echo "	Menu	"
echo "==========="
echo "1. View all books"
echo "2. Search for a book"
echo "3. count  out of stock"
echo "4.Update the Stock status"
echo "5.Calculate the total inventory values"
echo "6.Display books by category"
echo "7.Costliest books"
echo "8.Exit"


echo "Enter your choice:"
read ch
case $ch in

1)
view_book
;;

2)
search_book
;;

3)
count_out_of_stock
;;

4)
update_stock
;;

5)
inventory_value
;;

6)
books_category
;;

7)
costliest_books
;;

8)
echo "Thank You"
break
;;

*)
echo "Invalid Choice"
;;
esac

done
