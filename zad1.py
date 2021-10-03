import random as rnd
import numpy as np
import statistics as stat

def fill_matrix_with_rnd_numbers():
    size = input('insert matrix size (in format: \'6x6\'): ')
    tab = size.split('x', 2)
    numa = int(tab[0])
    numb = int(tab[1])
    print(f'Generating random matrix {numa} x {numb}')
    sampl = np.random.uniform(low=0.1, high=9.9, size=(numa,numb))
    print(sampl)
    return sampl

def matrix_mean(matrix):
    i = 1
    matrix_mean = []

    for matrix_1_dim in matrix:
        matrix_mean.append(
            sum(matrix_1_dim)/len(matrix_1_dim))

    for mean in matrix_mean:
        print(f'{i}. mean = {mean}')
        i = i + 1

def matrix_median(matrix):
    for sorted_matrix in matrix:
        print(stat.median(sorted_matrix))

rnd_matrix = fill_matrix_with_rnd_numbers()
matrix_mean(rnd_matrix)
matrix_median(rnd_matrix)

#%%
