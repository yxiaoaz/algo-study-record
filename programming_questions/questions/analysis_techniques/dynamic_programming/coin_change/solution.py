from utils.solution import Solution

class CoinChange(Solution):

    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        minCoin(a) = min{minCoin(a-c) + 1} for c in coins
        '''
        
        combinations = [-1] * (amount + 1)
        for sub_amount in range(amount+1):
            if sub_amount == 0:
                combinations[sub_amount] = 0
                continue
            
            candidates = []
            for c in coins:
                closest_sub_amount = sub_amount - c
                if closest_sub_amount < 0:
                    continue
                if combinations[closest_sub_amount] >= 0:
                    candidates.append(combinations[closest_sub_amount] + 1)
            
            combinations[sub_amount] = min(candidates, default = -1)
        
        return combinations[-1]