class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        def validChange(s,e):
            changes=0
            for i in range(len(s)):
                if s[i]!=e[i]:
                    changes+=1
            return changes==1
        queue=[(start,0)]
        visited=set()
        while queue:
            curr,steps=queue.pop(0)
            visited.add(curr)
            if curr==end:return steps
            for string in bank:
                if validChange(curr,string) and string not in visited:
                    queue.append((string,steps+1))

        return -1
