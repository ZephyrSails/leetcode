# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Float}
def find_median_sorted_arrays(nums1, nums2)
    l1 = nums1.length
    l2 = nums2.length
    l3 = l1+l2

    nums3 = []
    i, j, k = 0, 0, 0
    for k in 0..(l3/2) do
        if i == l1
            nums3 += nums2[j..-1]
            break
        end
        if j == l2
            nums3 += nums1[i..-1]
            break
        end
        if nums1[i] <= nums2[j]
            nums3[k] = nums1[i]
            i += 1
            k += 1

        else
            nums3[k] = nums2[j]
            j += 1
            k += 1

        end
    end
    # p nums3
    if l3 % 2 == 0
        return (nums3[l3/2-1] + nums3[l3/2]) / 2.0
    else
        return nums3[l3/2]
    end

end
