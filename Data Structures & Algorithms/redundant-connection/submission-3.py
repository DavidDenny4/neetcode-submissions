class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        for a, b in edges:
            default_dict[a].append(b)
            default_dict[b].append(a)
        
        print(f"the adj_list is {adj_list}")
        return []