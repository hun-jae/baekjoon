def next(users, emoticons, arr_dis, max_num_join, max_price):
    if len(arr_dis) == len(emoticons):  # 디스카운트 설정 끝
        # 여기서 계산
        num_join = 0
        price = 0
        for percent, join_price in users:
            tmp_price = 0
            for i, dis in enumerate(arr_dis):
                if dis >= percent:
                    tmp_price += emoticons[i]*(100-dis)//100
            if tmp_price >= join_price: #해당 유저가 가입함
                num_join += 1
            else: #해당 유저가 가입하지 않음
                price += tmp_price

        if num_join > max_num_join:
            # print(num_join)
            # print(price)
            # print(arr_dis)

            max_num_join = num_join
            max_price = price

        elif num_join == max_num_join:
            max_price = max(max_price, price)

    else:  # 아직 이모티콘 할인율이 전부 정해지지 않음
        for dis in [10, 20, 30, 40]:
            arr_dis.append(dis)
            max_num_join, max_price = next(users, emoticons, arr_dis, max_num_join, max_price)
            arr_dis.pop()

    return max_num_join, max_price


def solution(users, emoticons):
    return next(users, emoticons, [], 0, 0)
