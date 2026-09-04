class Decode_Ways:
    def numDecodings(self, s: str) -> int:
        s_size = len(s)
        ans = 0
        prev_but_one_ways = 1
        prev_ways = 1
        def can_join_with_prev_char(index):
            """
            index must be greater than 0
            and 
            if prev_char should be '1'
            or prev_char should be '2' and current char should be '0' to '6'
            """
            if index <= 0: return False
            if s[index-1] == '1': return True
            if s[index-1] == '2' and ord(s[index]) <= ord('6'): return True
            return False
        
        for index in range(s_size):
            curr = prev_ways
            if s[index] == '0':
                if can_join_with_prev_char(index):
                    curr = prev_but_one_ways
                else:
                    return 0
            elif can_join_with_prev_char(index):
                # add prev_but_one to prev
                curr = prev_ways+prev_but_one_ways
            prev_but_one_ways = prev_ways
            prev_ways = curr
        
        return prev_ways
        