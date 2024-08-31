def snake(n):
    area_game=n*n
    snake_len=1
    times=0
    while snake_len*2<area_game:
        snake_len*=2
        times+=1
    return times
print(snake(6))