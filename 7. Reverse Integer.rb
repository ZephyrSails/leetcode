# @param {Integer} x
# @return {Integer}
def reverse(x)
    ans = x.to_s.reverse.to_i
    return 0 if ans > 2147483648
    x >= 0 ? ans : -ans
end
