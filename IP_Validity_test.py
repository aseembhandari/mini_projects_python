# This program checks the validity of the IP address and the Subnet and if valid prints their binary representation
import random
import sys
masks = [255, 254, 252, 248, 240, 224, 192, 128, 0]
ip_address = raw_input("Enter the IP address here: " )
subnet_mask = raw_input("Enter a subnet mask: ")
ip_parts = []
ip_parts = ip_address.split(".")
sub_parts = []
sub_parts = subnet_mask.split(".")
#Check if the IP Address is valid or not
if (len(ip_parts) == 4) and (1 <= int(ip_parts[0]) <= 223) and (int(ip_parts[0]) != 127) and (int(ip_parts[0]) != 169 or int(ip_parts[1]) != 254) and (0 <= int(ip_parts[1]) <= 255 and 0 <= int(ip_parts[2]) <= 255 and 0 <= int(ip_parts[3]) <= 255):
	first = int(ip_parts[0])
	second = int(ip_parts [1])
	third = int(ip_parts [2])
	fourth = int(ip_parts [3])
	# The conversion of first octet to binary
	binary_octet1 = ""
	while first > 0:
		rem = first % 2
		binary_octet1 = binary_octet1 + str(rem)
		first = first // 2
	binary_octet1 = binary_octet1[::-1] 
	# The conversion of second octet to binary
	binary_octet2 = ""
	if second == 0:
		binary_octet2 = "0" + binary_octet2
	while second > 0:
		rem2 = second%2
		binary_octet2 = binary_octet2 + str(rem2)
		second = second //2
	binary_octet2 = binary_octet2[::-1]
	# The conversion of third octet to binary
	binary_octet3 = ""
	if third == 0:
		binary_octet3 = "0" + binary_octet3
	while third > 0:
		rem3 = third%2
		binary_octet3 = binary_octet3 + str(rem3)
		third = third //2
	binary_octet3 = binary_octet3[::-1]
	# The conversion of fourth octet to binary
	binary_octet4 = ""
	if first == 0:
		binary_octet4 = "0" + binary_octet4
	while fourth > 0:
		rem4 = fourth%2
		binary_octet4 = binary_octet4 + str(rem4)
		fourth = fourth //2
	binary_octet4 = binary_octet4[::-1]
	if (len(sub_parts) == 4) and (int(sub_parts[0]) == 255) and (int(sub_parts[1]) in masks) and (int(sub_parts[2]) in masks) and (int(sub_parts[3]) in masks) and (int(sub_parts[0]) >= int(sub_parts[1]) >= int(sub_parts[2]) >= int(sub_parts[3])):
		sub_first = int(sub_parts[0])
		sub_second = int(sub_parts [1])
		sub_third = int(sub_parts [2])
		sub_fourth = int(sub_parts [3])
	# The conversion of first octet to binary
		binary_sub1 = ""
		while sub_first > 0:
			sub_rem = sub_first % 2
			binary_sub1 = binary_sub1 + str(sub_rem)
			sub_first = sub_first // 2
		binary_sub1 = binary_sub1[::-1] 
	# The conversion of second octet to binary
		binary_sub2 = ""
		if sub_second == 0:
			binary_sub2 = "0" + binary_sub2
		while sub_second > 0:
			sub_rem2 = sub_second%2
			binary_sub2 = binary_sub2 + str(sub_rem2)
			sub_second = sub_second //2
		binary_sub2 = binary_sub2[::-1]
	# The conversion of third octet to binary
		binary_sub3 = ""
		if sub_third == 0:
			binary_sub3 = "0" + binary_sub3
		while sub_third > 0:
			sub_rem3 = sub_third%2
			binary_sub3 = binary_sub3 + str(sub_rem3)
			sub_third = sub_third //2
		binary_sub3 = binary_sub3[::-1]
	# The conversion of fourth octet to binary
		binary_sub4 = ""
		if sub_fourth == 0:
			binary_sub4 = "0" + binary_sub4
		while sub_fourth > 0:
			sub_rem4 = sub_fourth%2
			binary_sub4 = binary_sub4 + str(rem4)
			sub_fourth = sub_fourth //2
		binary_sub4 = binary_sub4[::-1]
		subnet_binary = binary_sub1 + "." + binary_sub2 + "." + binary_sub3 + "." + binary_sub4
		print "Subnet address in binary for is: ", subnet_binary

	else :
		"The subnet mask address is invalid"
	#print the complete ip address into binary form
	ip_binary = binary_octet1 + "." + binary_octet2 + "." + binary_octet3 + "." + binary_octet4
	print "IP address in binary form is: " ,ip_binary
	#print "Subnet address in binary for is: " + binary_sub1 + "." + binary_sub2 + "." + binary_sub3 + "." + binary_sub4
else:
	print "The entered ip address is invalid"
# This should be for the network address i have written it for the IP address
no_of_zeros = ip_binary.count("0")
no_of_ones = 32 - no_of_zeros
network_address_binary = ip_binary[:(no_of_ones)] + "0" * no_of_zeros
print network_address_binary
broadcast_address_binary = ip_binary[:(no_of_ones)] + "1" * no_of_zeros
print broadcast_address_binary
#no_of_hosts = abs(2** no_of_zeros - 2)
#print no_of_zeros
#print no_of_ones
#print no_of_hosts




