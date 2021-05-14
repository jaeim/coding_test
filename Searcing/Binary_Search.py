# 아 진짜 무한 재귀 걸려서 죽는줄 알았다.
# 실수요인: 무한재귀를 거르는 요인을 제대로 못만들었고, if-else로 안나누고 각각의 if문 세개로 처리해서 자꾸 무한재귀
def binary_search(minimum, maximum, key, nums, size):
    # int로 변환도 ok
    middle = round((minimum + maximum) / 2)
    # print(middle)

    if nums[middle] == key:
        print(middle + 1)

    # 	무한재귀 막기 => 여기서 실수한 것! if-else문으로 안나눠주어서..
    # max, mid, mid가 일치할때 (마지막 회귀) vs 더 재귀가능할 때로 안나누고 각각 if문을 쓰니 계속 재귀문을 호출했던거..

    if maximum == middle or minimum == middle:
        print('X')
    else:
        if nums[middle] < key:
            binary_search(middle, maximum, key, nums, size)

        if nums[middle] > key:
            binary_search(minimum, middle, key, nums, size)

    # 실수 코드는 아래와 같다.
    # if maximum == middle or minimum == middle:
    #     print('X')
    #
    # if nums[middle] < key:
    #     binary_search(middle, maximum, key, nums, size)
    #
    # if nums[middle] > key:
    #     binary_search(minimum, middle, key, nums, size)

size = int(input())
nums = list(map(int, input().split()))
# print(nums)
key = int(input())

if size <= 100:
    binary_search(0, size - 1, key, nums, size)
