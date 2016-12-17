# @param {String} str
# @return {Integer}
INT_MAX = 2147483647
INT_MIN = -2147483648
def my_atoi(str)
    integer = str.to_i

    return INT_MAX if integer > INT_MAX
    return INT_MIN if integer < INT_MIN
    return integer
end
