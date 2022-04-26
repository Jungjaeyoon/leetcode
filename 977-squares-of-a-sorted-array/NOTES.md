# Using built-in sorted method
# two-pointer 알고리즘을 이요한 풀이가 아님, python sorted() 가 O(n) 복잡도를 보장하는가? 
# 뭣보다... 이렇게 풀라고 문제를 낼까...?
sorted([x**2 for x in nums])​

# two-pointer 알고리즘을 이용한 풀이

# 문제 정리.
# 이 문제를 정리하면 절대값 순으로 정렬하여 제곱값을 리턴하라는 의미
# 문제가 되는 부분은 음수를 어떻게 비교하여 목록에 넣을 것인가

# 1. minval, maxval 2개의 포인터를 지정, 각 포인터는 리스트의 첫 번째 값과 마지막 값을 설정
        minval=0
        maxval=len(nums)-1
# 2. 정답 리스트를 미리 구현, [0,0,0...] 식으로 주어진 리스트의 길이와 동일한 0 값 리스트 생성
        sortedlist=[0]*len(nums)

#    이 리스트는 정렬된 리스트이다
#    첫 번째 값의 제곱이 마지막 값의 제곱보다 크다면 그 값은 무조건 최대값이 된다.
#    마지막 값의 제곱이 첫 번째 값의 제곱보다 크다면 그 값은 무조건 최대값이 된다.

# 3. for 문을 만든다, 범위는 range(len(nums)-1, -1, -1) 즉 리스트의 마지막 값 부터 1씩 줄여가며 값을 호출한다
        for x in range(len(nums)-1,-1,-1):

# 4. 위의 정리 내용에 따라 더 큰 값을 정답 리스트의 마지막 값에 구현한다.
            if nums[minval]**2 < nums[maxval]**2:
                sortedlist[x] = nums[maxval]**2

# 5. 그렇다면 그 다음 값은 어떻게 처리해야 할까?
# 만약 maxval 즉 리스트의 마지막 값의 제곱이 더 크다면? 
#   ->마지막 값을 정답 리스트의 마지막에 넣는다
#   ->마지막 값의 이전(-2) 값을 첫 번째 값과 다시 비교한다

# 만약 minval 즉 리스트의 첫 번째 값의 제곱이 더 크다면?
#   ->첫 번째 값을 정답 리스트의 마지막에 넣는다
#   ->첫 번째 값의 다음값(1)을 마지막 값과 다시 비교한다.

# 즉 최고로 작은 음수와 최대로 큰 양수의 제곱을 비교하여 
# 더 큰 값을 정답 리스트의 가장 큰 값에 넣고,
# 둘 중 정답 리스트로 이동한 값의 다음 값(두 번째로 작은 음수, 두 번째로 큰 양수)과 이동하지 못한 값을 비교하여 정답 리스트의 두 번째 값을 넣고...
# 이를 리스트 길이만큼 반복하며 정답 리스트의 모든 값을 갱신하면 완성

                maxval -= 1
            else:
                sortedlist[x] = nums[minval] **2
                minval += 1
        return sortedlist



        minval=0
        maxval=len(nums)-1

        sortedlist=[0]*len(nums)

        for x in range(len(nums)-1,-1,-1):
            if nums[minval]**2 < nums[maxval]**2:
                sortedlist[x] = nums[maxval]**2
                maxval -= 1
            else:
                sortedlist[x] = nums[minval] **2
                minval += 1
        return sortedlist