while True: 
    try:
        ent = input()
        n, h = map(int, ent.split() )
        t = []
        for _ in range(0,n):
            v, th =  map(int, input().split())
            t.append([v,th])
        t.sort(key=lambda x:x[0], reverse=True)
        for time in range(h, 0, -1):
            for task in t:
                if task[1] <= time:
                    t.remove(task)
                    break
        lost = sum(x[0] for x in t)
        print(lost)


    except EOFError:
        break
