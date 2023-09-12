"""
任务安排
时间限制： 3000MS
内存限制： 589824KB
题目描述：
    小明所在的团队在接下来n天已经有 m个任务需要执行，第 i 个任务从第li天开始执行，直到第ri天结束时完成。
    该团队希望再接受第 m+1 个任务，该任务需要连续的 k 天时间来完成，任务的开始时间由团队自行决定。
    为了保证所有任务的完成质量，团队任意一天同时执行的任务数量不能超过a 个。
    小明希望你帮忙计算，如果接受第 m+1 个任务，则从第1天到第n天，有多少天可以作为第m+1 个任务的开始时间，使得该任务可以在第 n 天结束前完成。

输入描述
- 输入第一行包含四个正整数n(1≤n≤105)，m(1≤m≤5*104)，k(1≤k≤105 )，a(1≤a≤5*104 )，
分别表示总天数、已接受的任务数量、执行第m+1个任务所需的天数、团队最多能同时执行的任务数量。
- 输入第二行包含m个整数，第 i 个整数表示第 i 个任务开始的时间li。(1≤li≤ri)
- 输入第三行包含m个整数，第 i 个整数表示第 i 个任务完成的时间ri。(li≤ri≤n)
- 输入保证，已接受的m个任务不会使得团队某一天同时执行的任务数量超过a个。

输出描述
- 输出包含一行，一个整数，表示有多少天可以作为第m+1个任务的开始时间。

- 样例输入
10 3 3 2
1 5 4
4 10 5

- 样例输出
4

- 样例解释
样例中，第m+1个任务可以安排在第1、6、7、8天开始，共4天符合题目条件。
"""
