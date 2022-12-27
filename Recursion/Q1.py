n = int(input())
fibonacci = {}


def fibo(n):
  if n not in fibonacci:
    fibonacci[n] = 0
  fibonacci[n] += 1
  if n == 0:
    return 0
  if n == 1:
    return 1
  return fibo(n - 1) + fibo(n - 2)

if 0 <= n and n <= 30:
    print(f"fibonacci({n}) = {fibo(n)}.")
if n == 1:
    print("0 chamada(s) a fibonacci(0).")
    for i in sorted(fibonacci):
        print(f"{fibonacci[i]} chamada(s) a fibonacci({i}).")
else:
    for i in sorted(fibonacci):
        print(f"{fibonacci[i]} chamada(s) a fibonacci({i}).")
