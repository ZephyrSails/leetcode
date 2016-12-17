# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val)
#         @val = val
#         @next = nil
#     end
# end

# @param {ListNode} l1
# @param {ListNode} l2
# @return {ListNode}
def add_two_numbers(l1, l2)
    carry = (l1.val+l2.val)>9?1:0
    current_node = ListNode.new((l1.val+l2.val)%10)
    start_node = current_node

    while ((l1.next != nil) or (l2.next != nil) or (carry != 0))
        l1 = l1.next
        l2 = l2.next
        if (l2 == nil)
            l2 = ListNode.new(0)
            # current_node.next = l1.next
            # return start_node
        end
        if (l1 == nil)
            l1 = ListNode.new(0)
            # current_node.next = l2.next
            # return start_node
        end
        sum = l1.val+l2.val+carry
        current_node.next = ListNode.new(sum%10)
        current_node = current_node.next
        carry = (sum)>9?1:0
    end
    return start_node

end
