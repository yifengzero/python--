def demo(num, *nums, **person):
    print(num)
    print(nums)
    print(person)


# demo(1)
demo(1, 2, 3, 4, 5, name="小美", age = 18)