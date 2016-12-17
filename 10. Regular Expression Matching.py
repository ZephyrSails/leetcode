class Solution(object):
    memo = {}

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p: return not s
        key = (s, p)
        if key not in self.memo:
            head = self.car(p)
            # print s, p, head
            if len(head) == 1:  # head is a constent
                if not s or head != '.' and head != s[0]:
                    self.memo[key] = False
                else:
                    self.memo[key] = self.isMatch(s[1:], p[1:])
            else:               # head is a variable
                if not s:       # No s
                    self.memo[key] = self.isMatch(s, p[len(head):])
                elif head[0] == '.' or s[0] == head[0]:     # match!
                    self.memo[key] = (self.isMatch(s, p[len(head):])
                                      or self.isMatch(s[1:], p[len(head):])
                                      or self.isMatch(s[1:], p))
                else:           # variable don't match
                    self.memo[key] = self.isMatch(s, p[len(head):])
        return self.memo[key]

    def car(self, p):
        if len(p) < 2:
            return p
        if p[1] == '*':
            return p[:2]
        return p[0]
        
