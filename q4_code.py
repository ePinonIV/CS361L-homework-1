# Code to plot Methods 1 and 2 for Question 4 of Homework-1

import sys
import math
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def methods(n):
    x_vals = list(range(n))
    y_m1 = list(range(n))
    y_m2 = list (range(n))

    for i in range(n):
        # Method 1 has time complexity of n^2
        y_m1[i] = pow(i, 2)
        # Method 2 has time complexity of n-1, which is O(n)
        y_m2[i] = i
    print("Methods done running")

    # plot
    plt.figure(figsize=(10,5),num='Sorting Methods 1 and 2 Plots')

    #plt.subplot(1,2,1)
    plt.plot()
    plt.xlabel("Integer Input (n)")
    plt.ylabel("Parabolic Value (n^2)")
    plt.title("Method 1")
    #plt.yscale('log')
    plt.grid(True)
    plt.plot(x_vals, y_m1, marker='o', linestyle='solid', color='red')
    plt.plot(x_vals, y_m2, marker='o', linestyle='solid', color='blue')
    #plt.plot(x_vals, y_m2, marker='o', linestyle='solid', color='blue')

    #plt.subplot(1,2,2)
    #plt.xlabel("Integer Input (n)")
    #plt.ylabel("Linear Value (n)")
    #plt.title("Method 2")
    #plt.yscale('log')
    #plt.grid(True)
    #plt.plot(x_vals, y_m2, marker='o', linestyle='solid', color='blue')

    plt.show()



# Extra function plots
def extras(n):
    # init lists to hold n! and 2^n
    x_vals = list(range(n))
    y_pow = list(range(n))
    y_fact = list(range(n))

    # fill in values for n! and 2^n
    for i in range(n):
        #y_fact[i] = math.factorial(i)
        if i > 1:
            y_fact[i] = y_fact[i] * y_fact[i-1]
        y_pow[i] = pow(2, i)

    plt.figure(figsize=(10,5),num='Other Function Plots')

    # plot n!
    plt.subplot(1,2,1)
    plt.xlabel("Integer Input (n)")
    plt.ylabel("Factorial Value (n!)")
    plt.title("Factorial Function Plot")
    plt.yscale('log')
    plt.grid(True)
    plt.plot(x_vals, y_fact, marker='o', linestyle='solid', color='red')

    # plot 2^n
    plt.subplot(1,2,2)
    plt.xlabel("Integer Input (n)")
    plt.ylabel("Power Value (2^n)")
    plt.title("Power Function Plot")
    #plt.yscale('log')
    plt.grid(True)
    plt.plot(x_vals, y_pow, marker='o', linestyle='solid', color='blue')

    print("... done running extras, showing plot now!")
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
