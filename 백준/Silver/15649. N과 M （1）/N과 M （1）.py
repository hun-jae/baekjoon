n, m = map(int, input().split())

result = list()

def back(depth, num_list):
    if depth == m: #길이를 다 채웠으면 수열 리스트에 넣어줘야대 근데 이 수열을 어떻게 알아? 이전단계에서 쌓아서 넘겨줘야 할 것 같은데? 그러면 파라미터로 이전에 넘겨줘야겠다
        for i in num_list:
            print(i, end=' ')
        print()
        return

    for i in range(1, n+1):
        if i in num_list:
            continue
        num_list.append(i)
        back(depth+1, num_list)
        num_list.pop()

back(0, [])
