while(1):
	print("1:set 2:list 3:exit")
	choice=int(input("enter your choice"))
	if choice==1:
		while(1):
			s1={1,2,3,4,5,6,7,8,9,10,11,12}
			s2={6,7,8,9,10,11,12}
			print("1.union 2,intersection 3.substract 4.issuperset 5.issubset 6.add 7. discard 8.length 9.clear 10.pop")
			ch=int(input("enter your choice"))
			if(ch==1):
				print(s1.union(s2))
			elif ch==2:
				print(s1.intersection(s2))
			elif ch==3:
				print(s1-s2)
			elif ch==4:
				print(s1.issuperset(s2))
			elif ch==5:
				print(s2.issubset(s1))
			elif ch==6:
				print(s1.add(10))
				print(s1)
			elif ch==7:
				print(s1.discard(2))
				print(s1)
			elif ch==8:
				print(len(s1))
			elif ch==9:
				print(s1.clear())
				print(s1)
			elif ch==10:
				print(s2.pop())
			else:
				print("Invalid Input")
				break
	elif choice==2:
		while(1):
			l1=["hard rock",1,2,4]
			l2=[6,"disco",9]
			print("1.add 2.remove 3.extend 4.append 5.count 6.clear 7.range 8.reverse 9.pop 10.length")
			ch=int(input("enter choice"))
			if(ch==1):
				print(l1+l2)
			elif ch==2:
				print(l1.remove(2))
				print(l1)
			elif ch==3:
				print(l1.extend(l2))
				print(l1)
			elif ch==4:
				print(l1.append("jack"))
				print(l1)
			elif ch==5:
				print(l1.count(l1))
			elif ch==6:
				print(l1.clear())
				print(l1)
			elif ch==7:
				print(l1[1:3])
			elif ch==8:
				print(l1[::-1])
			elif ch==9:
				print(l1.pop())
			elif ch==10:
				print(len(l1))
			else:
				print("Invalid Input")
				break
