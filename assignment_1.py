# COMP 251: Machine Learning
# Assignment 1: Gradient descent for uni-variable functions

def solution_1():
    theta = 4
    alpha = 0.7

    print(f'J(theta) = theta^2; theta = {theta}; alpha = {alpha}')
    print(f'grad = 2 * theta')
    for i in range (1, 7, 1):
        grad = 2 * theta
        theta = theta - alpha * grad
        print(f'{i}: {theta}')
    print('\n')

def solution_2():
    theta = 4
    alpha = 1.2

    print(f'J(theta) = theta^2; theta = {theta}; alpha = {alpha}')
    print(f'grad = 2 * theta')
    for i in range (1, 7, 1):
        grad = 2 * theta
        theta = theta - alpha * grad
        print(f'{i}: {theta}')
    print('\n')

def solution_3():
    theta = 3
    alpha = 0.15

    print(f'J(theta) = 1/3*theta^3 + 1/2*theta^2 -2*theta; theta = {theta}; alpha = {alpha}')
    print(f'grad = theta^2 + theta - 2')
    for i in range (1, 7, 1):
        grad = theta ** 2 + theta - 2
        theta = theta - alpha * grad
        print(f'{i}: {theta}')
    print('\n')

def solution_4():
    theta = -3
    alpha = 0.15

    print(f'J(theta) = 1/3*theta^3 + 1/2*theta^2 -2*theta; theta = {theta}; alpha = {alpha}')
    print(f'grad = theta^2 + theta - 2')
    for i in range (1, 7, 1):
        grad = theta ** 2 + theta - 2
        theta = theta - alpha * grad
        print(f'{i}: {theta}')
    print('\n')

if __name__ == '__main__':
    solution_1()
    solution_2()
    solution_3()
    solution_4()