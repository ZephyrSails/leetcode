# @param {String} s
# @return {Integer}
def length_of_longest_substring(s)
    return 0 if s == ""

    i, j = 0, 1
    max = 1

    while j < s.length do

        # if s[i] == s[j]
        if s[i..j-1].include? s[j]
            # i += 1
            i += s[i..j-1].index(s[j])+1
            if i == j
                j += 1
            end
        else
            j += 1
        end
        temp = j-i
        max = temp if max < temp
        # puts temp
    end



    return max
end
