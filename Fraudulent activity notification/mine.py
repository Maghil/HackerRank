def activityNotifications(expenditure, d):
    count=0
    for i in range(d,len(expenditure)):
        if  expenditure[i] >= (statistics.median(expenditure[(i-d):i])*2):
            print(statistics.median(expenditure[(i-d):i]))
            count+=1
    return count
