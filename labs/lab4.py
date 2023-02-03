"""
Ashna Razdan
"I pledge my honor that I have abided by the Stevens Honor System."
"""
def knapsack(capacity, items):
        """finds the max number of items that can fit in the knapsack and returns the max value and the items put in and their value."""
        if len(items)==0 or capacity <=0:
                return [0,[]]
        elif items[0][0] > capacity:
                return knapsack(capacity, items[1:])
        else:
                use = knapsack(capacity - items[0][0],items[1:])
                lose = knapsack(capacity, items[1:])
                if (use[0]+ items[0][1]) > lose[0]:
                        return [use[0]+ items[0][1], [items[0]] + use[1]]
                else:
                        return lose
        
                
                
