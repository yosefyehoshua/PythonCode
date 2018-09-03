# A
def total_budget(agentlist): 
    agents_total_budget = 0 
    for agent in agentlist:
        agents_total_budget += agent.get_budget() 
    return agents_total_budget 


# B   
def next_winner(agentlist): 
    winner = agentlist[0] 
    max_bid = agentlist[0].next_bid()
    for i in range(1, len(agentlist)):
        current_agent = agentlist[i] 
        if current_agent.next_bid() > max_bid: 
            winner = current_agent 
            max_bid = current_agent.next_bid() 
    return winner 


# C
def allocate_all(agentlist, count): 
    for i in range(count): 
        next_winner(agentlist).win_product() 


# D
class SuperAgent:
    def __init__(self, agentlist):
        self._agent_list = agentlist 
        self._budget = total_budget(agentlist) 
        self._products = 0 
        for agent in self._agent_list: 
            self._products += agent.count_product() 

    def get_budget(self):
        return self._budget 

    def win_product(self):
        self._products += 1 
        allocate_all(self._agent_list, 1)  # or: next_winner(self._agent_list).win_product()

    def count_products(self):
        return self._products 

    def next_bid(self):
        return self._budget/(self._products + 1)

