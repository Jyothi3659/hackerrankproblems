def andXorOr(a):
    max_s = 0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            s1 = ((j & i) ^ (j | i) & (j ^ i))
            if max_s < s1:
                max_s = s1
    return max_s

    # Write your code here.
    # first_max = None
    # next_max = None
    # for each in a:
    #     if first_max is None:
    #         first_max = each
    #     else:
    #         if next_max is None:
    #             if each < first_max:
    #                 next_max = each
    #             else:
    #                 first_max = each
    #         else:
    #             if each > first_max:
    #                 next_max = first_max
    #                 first_max = each
    #             else:
    #                 if each > next_max:
    #                     next_max = each
    # # s1 = ((first_max & next_max)^(first_max | next_max) & (first_max^next_max))
    # return (first_max , next_max)