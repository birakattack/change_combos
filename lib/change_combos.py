class ChangeCombos:

    def __init__(self, coins):
        self.coins = sorted(coins, key=int)

    def combo_count(self, target, partial=[]):
        try:
            parsed_target = int(target)
        except:
            raise ValueError('Failed to convert to integer.')

        ways = [1]+[0]*parsed_target
        for coin in self.coins:
            for i in range(coin, parsed_target+1):
                ways[i] += ways[i-coin]

        return ways[parsed_target]
