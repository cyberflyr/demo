
def find_path(graph: list[list[int]]):
    ans = []
    items = []

    def backtrack(i):
        if i == len(graph) -1:
            ans.append(items[:])
            return

        for j in graph[i]:
            items.append(j)
            backtrack(j)
            items.pop()
    
    items.append(0)
    backtrack(0)
    return ans

if __name__=='__main__':
    print(find_path([[1,2],[3],[3],[]]))