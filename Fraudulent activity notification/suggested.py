def activityNotifications(expenditure, d):
    median_list=sorted(expenditure[0:d])
    count=0
    for i in range(d,len(expenditure)):
        median = median_list[d//2] if d%2 == 1 else ((median_list[d//2] + median_list[d//2-1])/2)
        if expenditure[i] >= 2*median:
            count+=1
        del median_list[bisect.bisect_left(median_list, expenditure[i-d])]
        bisect.insort(median_list,expenditure[i])
    return count
