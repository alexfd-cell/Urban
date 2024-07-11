data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])]

def f(x):
  if isinstance(x, str):
    return len(x)
  if isinstance(x, int):
    return x
  if isinstance(x, (list, tuple)):
    if len(x) == 0:
      return 0
    else:
      return f(x[0]) + f(x[1:])
  if isinstance(x, dict):
    return f(list(x.items()))
  if isinstance(x, set):
    return f(list(x))

print(f(data_structure))