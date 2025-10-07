import random

def is_sorted(arr):
    """배열이 정렬되었는지 확인"""
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))

def bogo_sort(arr):
    """Bogo Sort 구현"""
    attempts = 0
    while not is_sorted(arr):
        random.shuffle(arr)
        attempts += 1
    return arr, attempts


# 예제 실행
if __name__ == "__main__":
    data = [3, 1, 4, 8, 9, 10, 7, 2, 5, 6]
    sorted_data, tries = bogo_sort(data)
    print("정렬 결과:", sorted_data)
    print("시도 횟수:", tries)
