def next(users, emoticons, arr_dis, max_num_join, max_price):
    if len(arr_dis) == len(emoticons):
        num_join = 0
        price = 0
        
        for percent, join_price in users:
            tmp_price = 0
            
            for i, dis in enumerate(arr_dis):
                if dis >= percent:
                    tmp_price += emoticons[i]*(100-dis)//100
                    
            if tmp_price >= join_price: #가입 o
                num_join += 1
            else: #가입 x
                price += tmp_price

        if num_join > max_num_join:
            max_num_join = num_join
            max_price = price

        elif num_join == max_num_join:
            max_price = max(max_price, price)

    else:
        for dis in [10, 20, 30, 40]:
            arr_dis.append(dis)
            max_num_join, max_price = next(users, emoticons, arr_dis, max_num_join, max_price)
            arr_dis.pop()

    return max_num_join, max_price


def solution(users, emoticons):
    return next(users, emoticons, [], 0, 0)
