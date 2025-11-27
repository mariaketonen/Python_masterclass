def sum_numbers(*values: float) -> float:
    """
    Summing up random values.
    :type values: float
    :param values: Given random values.
    :return: Sum
    """
    addition = 0
    for number in values:
        addition += number
    return addition

  #  addition = sum(values)
  #  print(*values, sep=", ")
  #  print("{}"
  #    .format(addition))
  #  return addition


sum_numbers(1, 2, 3)
sum_numbers(8, 20, 2)
sum_numbers(12.5, 3.147, 98.1)
sum_numbers(1.1, 2.2, 5.5)
sum_numbers(366663, 666, 78545, 32423, 9090909)



