#if we can go past the last index, we can get to it for sure
#so just recors the max unit we can get to so far

def canJump(self, nums):
    m = 0
    for i, n in enumerate(nums):
        if i > m: #if we got to a place we can't reach
            return False
        m = max(m, i+n)
    return True
