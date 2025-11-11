import time

class Item:
    def __init__(self,profit,weight):
        self.profit=profit
        self.weight=weight
        self.ratio=profit/weight
def fractional_knapsack(capacity,items):
    items.sort(key=lambda x:x.ratio, reverse=True)
    total_value=0.0
    remaining_capacity=capacity
    selection=[]

    for item in items:
        if remaining_capacity==0:
            break
        if item.weight<=remaining_capacity:
            total_value+=item.profit
            remaining_capacity-=item.weight
            selection.append((item,1.0))
        else:
            fraction=remaining_capacity/item.weight
            total_value+=fraction*item.profit
            selection.append((item,fraction))
            remaining_capacity=0
    return total_value,selection
if __name__=="__main__":
    n=int(input('enter no of items : '))
    items=[]
    for i in range(n):
        profit=float(input(f"\nEnter profit of item {i+1}: "))
        weight=float(input('Enter weight: '))
        items.append(Item(profit,weight))
    capacity=float(input("\n Enter Capacity of knapsack:"))

    start_time=time.time()
    max_value,selection=fractional_knapsack(capacity,items)
    end_time=time.time()
    exc_time=end_time-start_time
    print("\n==============================") 
    print("         ITEM DETAILS (Sorted by Ratio)") 
    print("==============================") 
    print(f"{'Item':<8}{'Profit':<10}{'Weight':<10}{'Ratio':<10}") 
    print("-" * 40) 
    for idx, item in enumerate(items, start=1): 
        print(f"{idx:<8}{item.profit:<10}{item.weight:<10}{item.ratio:<10.2f}") 
 
    # display selection 
    print("\n==============================") 
    print("      ITEMS SELECTED IN BAG") 
    print("==============================") 
    print(f"{'Item':<8}{'Fraction Taken':<15}{'Profit Added':<15}") 
    print("-" * 45) 
    for sel in selection: 
        item, frac = sel 
        profit_added = item.profit * frac 
        print(f"{items.index(item)+1:<8}{frac*100:<15.2f}{profit_added:<15.2f}") 
 
    # final result 
    print("\n==============================") 
    print("         FINAL RESULTS") 
    print("==============================") 
    print(f"Maximum Profit  : {max_value:.2f}") 
    print(f"Execution Time  : {exc_time:.16f} seconds \n")


## Sample Input/Output:
# n = 7 m =  15
# profits = [10, 5, 15, 7, 6, 18, 3]
# weights = [2, 3, 5, 7, 1, 4, 1]
# Maximum Profit  : 55.33
