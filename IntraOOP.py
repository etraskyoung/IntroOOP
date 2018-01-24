class ChanceNode:
    def __init__(self, probs, costs):
        self.probs = probs
        self.costs = costs
        #self is the object we will create; init means initializing the object
    def get_expected_cost(self):
        num_outcomes = len(self.costs)
        exp_cost = 0 #expected costs
        for i in range(num_outcomes):
            exp_cost += self.probs[i] * self.costs[i]

        return exp_cost

myChanceNode = ChanceNode([0.1, 0.2, 0.7], [10, 20, 30])

print(myChanceNode.get_expected_cost())
