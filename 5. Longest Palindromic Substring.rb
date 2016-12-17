# @param {String} s
# @return {String}
def longest_palindrome(s)
    return 0 if s == ""
    n = s.length
    for m in n.downto(2) do
        # substring_len = m
        # substring_count = n-m+1
        # middle_points: (m-1)/2 .. (n-(m-1)/2)
        # i, middle, j, j = 2 * middle - i
        memo = Array.new(n-m+1, true)
        # middle_points = [*((m-1)/2.0)..(n-1-(m-1)/2.0)]
        middle_points = []
        first_middle = (m-1)/2.0
        (n-m+1).times do
            middle_points << first_middle
            first_middle += 1
        end

        for i in 0...n do
            for k in 0..n-m+1 do

                if memo[k] == true
                    middle = middle_points[k]
                    # p middle_points
                    j = 2 * middle - i
                    # p (1+(i+j)/2.0-m/2.0)..((i+j)/2.0+m/2.0)
                    # p s[(1+(i+j)/2.0-m/2.0)..((i+j)/2.0+m/2.0)]

                    if j < n
                        # p "#{i}, #{j}"
                        if s[i] == s[j]
                            if i == j or i == j-1
                                return s[(1+(i+j)/2.0-m/2.0)..((i+j)/2.0+m/2.0)]
                            end
                        else
                            memo[k] = false
                        end
                    end
                end

            end
        end
    end
    return s[0]

end

# def longest_palindrome(s)
#     return "" if s == ""
#     max_str = ""
#     for i in 0...s.length do
#         if s[0..i] == s[0..i].reverse
#             max_str = s[0..i] if max_str.length < s[0..i].length
#             rest = longest_palindrome(s[i+1..-1])
#             max_str = rest.length > max_str.length ? rest : max_str
#         end
#     end
#     max_str

# end

# def


# end
