def is_product_divisible_by_the_sum(numbers):
    if not numbers:
        return False
    else:
        total_sum=0
        product=1
        for i in range (len(numbers)):
            total_sum=int(numbers[i])+total_sum
            product=product*int(numbers[i])
        print(total_sum,"and",product)
        if total_sum==0:
            return False
        if product%total_sum==0: #if its divisible 
            return True
        else:
            return False
numbers=input("enter numbers seperated by space : ").split()
numbers=[int(num) for num in numbers] #i can use a generator instead of loop
print(is_product_divisible_by_the_sum(numbers))
