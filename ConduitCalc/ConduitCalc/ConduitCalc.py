#This is a program to calculate conduit fill. 
#Property of Morgan Alsbrook. All rights reserved. No one may reproduce or modify the program without the owner's expressed permission.
#! /usr/bin/python
#Variable Declarations
size = 0;
wire_size = 0;
wire_qty = 0;
continue_var = 0;
Percent_Full = 0;
#
#Function Declarations Below
def continuecalc():
    print("Do you have anything else to add to this calculation? 'y' or 'n'")
    continue_var = input()
    if continue_var == 'y':
        continuecalc1()
    elif continue_var is 'n':
       final_answer()
def more_qty():
    print("Please enter the qty of wire/cable of this type and hit enter. Note: Press enter after each entry then, type 'Done' when finished.")
    qty_list = []
    while True:
            qty_list.append(int(input()))
            print(qty_list)
def final_answer():
    Percent_Full = float(100 * ((wire_qty * wire_size) / conduitsize ))
    print("This conduit is :  " + str(round(Percent_Full,2)) + "% Full")
#Conduit Size
print("Please enter the conduit size. For example, 1-1/4 Conduit will be entered as 1.25")
conduitsize = float(input())
#OD of Cable
print("Please enter the O.D. of wire/cable.")
wire_size = float(input())
#Qty of wire
print("Please enter the qty of wire/cable of this type.")
wire_qty = float(input())
continuecalc() 