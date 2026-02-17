# Code to plot Methods 1 and 2 & other time functions for Question 4 of Homework-1

import sys
import math
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def methods(n):
    # make lists for values
    x_vals = list(range(n))
    y_m1 = list(range(n))
    y_m2 = list (range(n))

    for i in range(n):
        # Method 1 has time complexity of n^2
        y_m1[i] = pow(i, 2)
        # Method 2 has time complexity of n-1, which is O(n)
        y_m2[i] = i
    print("Methods done running")

    # set up plot w/matplotlib functions
    plt.figure(figsize=(10,5),num='Sorting Methods 1 and 2 Plots')
    plt.plot()
    plt.xlabel("Integer Input $n{}$")
    plt.ylabel("Time Complexity $f(n){}$")
    ntitle = "Sorting Method 1 vs Method 2 Time Complexity, $n$=" + str(n)
    plt.title(ntitle)
    plt.grid(True)
    plt.plot(x_vals, y_m1, marker='*', linestyle='solid', color='red')
    plt.plot(x_vals, y_m2, marker='o', linestyle='solid', color='blue')
    plt.legend(['Method 1 - $n^2$', 'Method 2 - $n$'])

    # save fig to be able to put in README
    filename = "methods_" + str(n) + ".png"
    plt.savefig(filename)
    plt.show()


# Extra function plots
def extras(n):
    # init lists to hold n! and 2^n
    x_vals = list(range(n))
    y_pow = list(range(n))
    y_fact = list(range(n))

    # fill in values for n! and 2^n
    for i in range(n):
        if i > 1:
            y_fact[i] = y_fact[i] * y_fact[i-1]
        y_pow[i] = pow(2, i)

    # plot w/ matplotlib
    plt.figure(figsize=(10,5),num='Other Function Plots')
    plt.xlabel("Integer Input $n{}$")
    plt.ylabel("Time Complexity $f(n){}$")
    ntitle = "Factorial vs Power Function Plot, $n$=" + str(n)
    plt.title(ntitle)
    plt.yscale('log')
    plt.grid(True)
    plt.plot(x_vals, y_fact, marker='*', linestyle='solid', color='red')
    plt.plot(x_vals, y_pow, marker='o', linestyle='solid', color='blue')
    plt.legend(['n!', '$2^n$'])

    # savefig for showing in README
    print("... done running extras, saving & showing plot now!")
    filename = "extras_" + str(n) + ".png"
    plt.savefig(filename)
    plt.show()


# main fn to run code
def main():
    print("-------------------------")

    if sys.argv[1] == 'methods':
        print("Running method 1...")
        methods(int(sys.argv[2]))
    elif sys.argv[1] == 'extras':
        print("Running extras...")
        extras(int(sys.argv[2]))
    else:
        print("unknown argument, no functions ran...")
        exit(0)

    print("Fig closed, ending program")
    print("-------------------------")

if __name__ == "__main__":
    main()
