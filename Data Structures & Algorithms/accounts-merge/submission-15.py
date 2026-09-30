class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        parent = {}
        rank = {}

        for i in range(len(accounts)):
            parent[i] = i
            rank[i] = 0
        
        def find(acc_index):
            p = parent[acc_index]
            while p != parent[parent[p]]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p

        def union(acc_a, acc_b):
            par_a, par_b = find(acc_a), find(acc_b)
            if par_a == par_b:
                return False
            
            if rank[par_a] > rank[par_b]:
                parent[par_b] = par_a
                rank[par_a] += rank[par_b]
            else:
                parent[par_a] = par_b
                rank[par_b] += rank[par_a]
            return True

        email_map = {}
        for account in range(len(accounts)):
            for email in accounts[account][1:]:
                if email in email_map:
                    union(email_map[email], account)
                else:
                    email_map[email] = account
        
        print(f" the email map is {email_map}")
        index_map = defaultdict(list)
        for email in email_map:
            index_map[find(email_map[email])].append(email)
        
        res = []
        for index in index_map:
            name = accounts[index][0]
            emails = index_map[index]
            account = [name] + emails
            res.append(account)
        return res