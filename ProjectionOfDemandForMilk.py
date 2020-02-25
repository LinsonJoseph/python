response = 'Y'
type_of_milk = ''
quantity_sold = ''
mrp_of_milk_type = ''

valid_response = True
daily_quatity_of_type = {}

while(response == 'Y'): 
    while(type_of_milk == ''):
        type_of_milk = input("Type of Milk: ")
        if(type_of_milk == ''):
            print("Please enter a valid value for milk type: ")
        
    while(quantity_sold.isnumeric() == False):
        quantity_sold = input("Enter a numeric value for quantity sold: ")

    while(mrp_of_milk_type.isnumeric() == False):      
        mrp_of_milk_type = input("Enter a numeric value for MRP of Milk Type: ")
        
    daily_quatity_of_type.update({type_of_milk : quantity_sold})
    type_of_milk = ''
    quantity_sold = ''
    mrp_of_milk_type = ''
    
    while(valid_response == True):
        response = input("\nDo you want to make another entry (Y/N): ")
        if response[0] == 'Y' or response[0] == 'y':
            response = 'Y'
            break
        elif response[0] == 'N' or response[0] == 'n':
            response = 'N'
            break
        else:
            print("Please enter a valid response: ")

print("\nAll entries today...\n", daily_quatity_of_type)

for x,y in daily_quatity_of_type.items():
    projected_quantity = int(y) + (20/100*int(y))
    print("\nProjected quantity for tomorrow for type '" + x.capitalize() + "' is: " + str(projected_quantity))
