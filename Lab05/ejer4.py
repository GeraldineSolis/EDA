from collections import deque

def maximo_ventana(nums, k):
    if not nums:
        return []

    deq = deque()
    resultado = []

    for i in range(len(nums)):
        while deq and deq[0] <= i - k:
            deq.popleft()

        while deq and nums[deq[-1]] < nums[i]:
            deq.pop()

        deq.append(i)

        if i >= k - 1:
            resultado.append(nums[deq[0]])

    return resultado
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
resultado = maximo_ventana(nums, k)
print("Máximos en ventanas:", resultado)

