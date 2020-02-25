#Calculation of Monthly Profit of an organization
print("---------------------------------------------------------------------------")
print("#                      Calculation of Monthly Profit                      #")
print("---------------------------------------------------------------------------")
sold_quantity     = int(input("Sold Quantity.........: "))
raw_material_cost = int(input("Raw Material Cost.....: "))
manufacturing_cost= int(input("Manufacturing Cost....: "))
profit_margin     = int(input("Profit Margin (in%)...: "))
tax_deduction     = int(input("Tax Deduction (in%)...: "))

print("---------------------------------------------------------------------------")
cost_of_product = raw_material_cost + manufacturing_cost
print("Cost of product (=raw material + mfg. cost) is...: ", cost_of_product)
selling_price = cost_of_product + (profit_margin/100) * cost_of_product
print("Selling price (=CoP+Prft_mrgn/100 * CoP) is......: ", selling_price)
net_sales = sold_quantity * selling_price
print("Net sales (=Sold_qty * Selling_Price) is.........: ", net_sales)
net_cost_price = sold_quantity * cost_of_product
print("Net CP (=Sold_qty * CoP) is......................: ", net_cost_price)
gross_profit = net_sales - net_cost_price
print("Gross Profit (=net_sales-net_cost_price) is......: ", gross_profit)

print("---------------------------------------------------------------------------")
monthly_profit = gross_profit - (tax_deduction/100) * gross_profit
print("Monthly Profit of Organization (=gp-td/100*gp)...: ", monthly_profit)
print("---------------------------------------------------------------------------")
