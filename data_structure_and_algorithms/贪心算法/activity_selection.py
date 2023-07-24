"""
假设有n个活动，这些活动要占⽤同⼀⽚场地，⽽场地在某时刻只能供⼀个活动使⽤。

每个活动都有⼀个开始时间si和结束时间fi（题⽬中时间以整数表示），表示活动在[si, fi)区间占⽤场地。

问：安排哪些活动能够使该场地举办的活动的个数最多？
"""


def activity_selection(activities):
    tmp_list = [activities[0]]  # 因为排序了，
    for i in range(1, len(activities)):
        if activities[i][0] >= tmp_list[-1][1]:
            # 如果当前的活动开始时间大于或等于已经开始的活动截至时间，时间就不冲突，加入到活动列表中
            tmp_list.append(activities[i])
    return tmp_list


if __name__ == '__main__':
    # 每个小元组表示活动开始时间和截止时间
    activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]
    # 保证活动是按照结束时间排好序的
    activities.sort(key=lambda x: x[1])
    activities_plan = activity_selection(activities)
    print(activities_plan)
