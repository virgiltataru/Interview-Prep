#If n/k = 0, leftover_part will take care of dividing the
#items in groups of 1

class Solution(object):
    def splitListToParts(self, root, k):
        n = 0
        curr = root
        while curr != None:
            n += 1
            curr = curr.next

    # determine part length and any leftover length
        length = n / k
        leftover_length = n % k
        curr = root
        parts = []
        for i in xrange(k):
            part = []
            for j in xrange(length):
                part.append(curr.val)
                curr = curr.next
            if leftover_length > 0:
                part.append(curr.val)
                curr = curr.next
                leftover_length -= 1
            parts.append(part)
        return parts
