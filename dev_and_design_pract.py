# This was practice of writing stubs from a structure chart
# and practicing bottom up development. I didn't follow the steps
# very well. I wrote it all before testing, very bad.

# This program produces a bill by calculating a total from the base cost,
# the tip, and the tax.
def main():
    base_cost = get_total_cost()
    tip_rate = get_tip_rate()
    total_cost = compute_cost(base_cost, tip_rate)
    display_bill(total_cost)

def get_total_cost():
    cost = get_item_price()
    return cost

def get_item_price():
    price_item = 5
    return price_item

def get_tip_rate():
    tip_rate = 0.2
    return tip_rate

def compute_cost(cost, tip_rate):
    pre_tax_cost = cost + cost * tip_rate
    tax_amount = compute_tax(pre_tax_cost)
    total_cost = pre_tax_cost + tax_amount
    return total_cost

def compute_tax(cost):
    tax_amount = cost * 0.06
    return tax_amount

def display_bill(bill):
    print(bill)

main()