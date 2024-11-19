class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        trans = defaultdict(list)
        invalid = set()

        for i,n in enumerate(transactions):
            name, time_str, amount_str, city = n.split(",")
            time, amount = int(time_str), int(amount_str)
            trans[name].append((time, city, i))

            if amount > 1000:
                invalid.add(i)
            
            for time1, city1, i1 in trans[name]:
                if city != city1 and abs(time1 - time) <= 60:
                    invalid.add(i1)
                    invalid.add(i)
        return [transactions[i] for i in invalid]