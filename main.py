"""Making the Taylor's series for 1 / (1 + sin(x)) and comparing
it with the original function."""
from math import factorial, sin
import numpy as np
import matplotlib.pyplot as plt


def sin_finder(amount_of_iterations: int, x: float) -> float:
    """
    Finds the sum only for sin(x) function.
    :param amount_of_iterations: int
    :param x: float (point)
    :return: float (sum in the point)
    (int, float -> float)
    """
    ans = 0
    for i in range(amount_of_iterations):
        ans += ((-1) ** i) * (x ** (2 * i + 1)) / factorial(2 * i + 1)
    return ans


def sum_finder(amount_of_iterations: int, lst: list) -> list:
    """
    Finds the Taylor's sum for y.
    :param amount_of_iterations: int
    :param lst: list of points
    :return: list of sums
    (int, list -> list)
    """
    ans = []
    for x in lst:
        y, i = 0, 0
        while i < 1000:
            y += ((-1) ** i) * (sin_finder(amount_of_iterations, x)) ** i
            i += 1
        ans.append(y)
    return ans


def graph_builder(amount_of_iterations) -> None:
    """
    Building the graph for Taylor's series and for the original function.
    :param amount_of_iterations: int
    :return: matplotlib graph
    """
    x = np.arange(-8, 5, 0.05)
    plt.plot(x, sum_finder(amount_of_iterations, x), color="green")
    plt.plot(x, (1 / (1 + np.sin(x))), color="red")
    plt.ylim(-1, 15)
    plt.title("Taylor for 1 / (1 + sin(x))")
    plt.ylabel("y axis")
    plt.xlabel("x label")
    plt.show()


def difference_finder(x: float) -> str:
    """
    Finds the faults for different amount of iterations.
    :param x: float (point)
    :return: str
    (float -> str)
    """
    nums, ans = [1, 5, 10, 25, 50], ""
    for i in nums:
        try:
            ans += f"For the amount of iterations = {i} the taylor's number is {sum_finder(i, [x])[0]}, " \
                   f"the difference is {abs(sum_finder(i, [x])[0] - (1 / (1 + sin(x))))}\n"
        except OverflowError:
            continue
    return ans


def fault_finder(x: float, psy: float) -> str:
    """
    Finds the minimum amount of iterations for different faults.
    :param x: float (point)
    :param psy: float (fault)
    :return: str
    (float, float -> str)
    """
    ans = 0
    i = 1
    while True:
        try:
            if abs(sum_finder(i, [x])[0] - (1 / (1 + sin(x)))) < psy:
                ans += i
                break
            else:
                i += 1
        except OverflowError:
            i += 1
    return f"For the fault of {psy} the minimum amount of iterations is {ans}"


def main(amount_of_iterations: int, x: float) -> str:
    """
    The main function starting other functions.
    :param amount_of_iterations: int
    :param x: float (point)
    :return: str
    (int, float -> str)
    """
    print(f"The number we got is: {sum_finder(amount_of_iterations, [x])[0]}")
    print(f"The real number is: {1/ (1 + sin(x))}")
    print(f"The difference between them is: "
          f"{abs(sum_finder(amount_of_iterations, [x])[0] - (1 / (1 + sin(x))))}\n")
    print(difference_finder(x))
    print(fault_finder(x, 10 ** (-1)))
    print(fault_finder(x, 10 ** (-3)))
    print(fault_finder(x, 10 ** (-6)))
    graph_builder(amount_of_iterations)


if __name__ == '__main__':
    print("This is the Taylor's series for the function: 1 / (1 + sin(x))")
    try:
        number_of_iterations = int(input("Enter the number of iterations:\n>>> "))
        point = float(input("Enter point (x coordinate):\n>>> "))
        main(number_of_iterations, point)
    except OverflowError:
        print("The number is too be displayed large. Try again")
    except ValueError:
        print("Wrong input!")
