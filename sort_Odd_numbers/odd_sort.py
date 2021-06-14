def sort_array(source_array):
    copy = source_array # don't mutate the information.
    odds = [y for y in copy if y % 2 != 0]

    odds.sort() # because reverse wont sort a list
    odds.reverse()

    for index, value in enumerate(copy):
        if value % 2 != 0:
            x = odds.pop()
            copy[index] = x

    print(copy, source_array)
    return copy

sort_array([10,9,8,7,6,5,4,3,2,1])
sort_array([5, 3, 1, 8, 0])

#           10,1,8,3,6,5,4,7,2,9
# should return # 10,1,8,3,6,5,4,7,2,9


    #bob = [y for y in copy if y % 2 != 0]
    #print(bob, " here")

    # for num in copy:
    #     if num % 2 != 0:
    #         odds.append(num)



# someone elses solutin. HAHA

# def sort_array(arr):
#   odds = sorted((x for x in arr if x%2 != 0), reverse=True)
#   return [x if x%2==0 else odds.pop() for x in arr]
