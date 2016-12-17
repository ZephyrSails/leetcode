# @param {String} s
# @param {Integer} num_rows
# @return {String}
def convert(s, num_rows)
    result = [""] * (num_rows + 1)
        level, order = 1, 1
        for i in s.split("")
            result[level*order] += i
            level += 1
            if level >= num_rows
                level, order = 1, order * (-1)
            end
        end
        return result.join
    # a = s.split("")
    # arr = []
    # one = true
    # until a.empty?
    #     if one
    #         arr << a.shift(num_rows)
    #     else
    #         ar = Array.new(num_rows)
    #         ar[num_rows/2] = a.shift((num_rows)/2-1)
    #         arr << ar.flatten
    #     end
    #     one ^= true
    # end
    # arr
    # str = ""
    # for i in 0..(num_rows-1)
    #     arr.each do |j|
    #         str += j[i].to_s
    #     end
    # end
    # str
end
