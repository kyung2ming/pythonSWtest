
## 탐색

가장 기본적인 탐색( = 순차 탐색). 시간 복잡도 `O(n)`

다른 알고리즘을 이용하여 푸는 문제에서는 순차 탐색이 많이 쓰임
```python
for i in range(n):
	if arr[i] == answer:
		return i # 또는 return i+1
```


## 이진탐색


`정렬`된 배열을 반으로 쪼개면서 탐색. 시간 복잡도 `O(log n)`

start, end, mid 변수 3개를 사용하며, 중간 점을 나타내는 mid를 start와 end에 대입하여 범위를 좁힘

쉬운 탐색을 위해 `소수점 버림`

데이터의 개수가 1,000만 개를 넘어가거나  탐색 범위가 1,000억 이상일 때 이진 탐색을 사용

문제의 핵심은 `최소, 최대 범위`를 구한 뒤 구하려고 하는 답을 이분 탐색으로 범위를 좁혀가며 답을 구하는 것

이진 탐색 문제는 입력 데이터가 많음. input() 대신 sys.stdin.readline()을 사용해야 시간초과가 나지 않음

### 코드
```python
# 재귀 ver.
def binary(start, end):
	if start > end: # 못 찾음 or 예외처리
		return none
		
	mid = (start + end) // 2
	
	if arr[mid] < target:
		binary(mid + 1 , end) # 중간값의 오른쪽부터 끝까지 탐색
	elif arr[mid] > target:
		binary(start , mid - 1) # 처음부터 중간값의 왼쪽까지 탐색
	else: # arr[mid] == target
		return mid

# 반복문 ver.
def binary():
	while start <= end:
		mid = (start + end) // 2

		if arr[mid] < target:
			start = mid + 1
		elif arr[mid] > target:
			end = mid - 1
		else:
			return mid
		
# 라이브러리 ver.
import bisect
bisect.bisect(arr, target) # 값이 없을 경우 가까운 위치를 반환
```
