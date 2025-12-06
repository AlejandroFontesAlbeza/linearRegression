import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset = pd.read_csv('dataset.csv')


def MSE(m, b, points):
    
    total_error = 0
    for i in range(len(points)):
        x = points.iloc[i].x
        y = points.iloc[i].y
        total_error += (y - (m * x + b)) ** 2

    total_error = total_error / float(len(points))
    return total_error


def gradient_descent(m_now, b_now, points, lr, epoch):

    m_gradient = 0
    b_gradient = 0

    n = len(points)

    for i in range(n):
        x = points.iloc[i].x
        y = points.iloc[i].y


        m_gradient += -(2/n) * x * (y - (m_now * x + b_now))
        b_gradient += -(2/n) * (y - (m_now * x + b_now))

    m = m_now - m_gradient * lr
    b = b_now - b_gradient * lr
    error = MSE(m, b, points)

    if epoch % 100 == 0: 
        print(f'Epoch: {epoch}, MSE: {error}')

    return m,b


'''doing this instead of m=0 and b=0 we have
to train with a lot of epochs because the linear
regression algortihm needs to adjust more m and b.
If you want to reduce number of epochs in linear
regression training adjust this variables to 0
because is the "idel" example too, but i wanted to
see the algorithm during more epochs.'''

m= 0 #orientation line random º
b= 0 #height of the line random




'''depending on the numbers of m and b maybe yo should
add more epochs and adjust lr '''

lr = 0.0001
epochs = 50000


for i in range(epochs):
    if i <= 10:
        x_line = np.linspace(0,100,100) # I create 100 numbers from 0-100 (i know my dataset is between those numbers)
        y_line = m * x_line + b # we adjust this line

        plt.scatter(dataset.x, dataset.y)
        plt.plot(x_line, y_line, color = 'k', linewidth = 2)
        plt.savefig('gradient_descent.png')
    elif i == 8000:
        x_line = np.linspace(0,100,100) # I create 100 numbers from 0-100 (i know my dataset is between those numbers)
        y_line = m * x_line + b # we adjust this line

        plt.scatter(dataset.x, dataset.y)
        plt.plot(x_line, y_line, color = 'g', linewidth = 2)
        plt.savefig('gradient_descent.png')
    elif i == 25000:
        x_line = np.linspace(0,100,100) # I create 100 numbers from 0-100 (i know my dataset is between those numbers)
        y_line = m * x_line + b # we adjust this line

        plt.scatter(dataset.x, dataset.y)
        plt.plot(x_line, y_line, color = 'y', linewidth = 2)
        plt.savefig('gradient_descent.png')

    m, b = gradient_descent(m, b, dataset, lr, i)


x_line = np.linspace(0,100,100) # I create 100 numbers from 0-100 (i know my dataset is between those numbers)
y_line = m * x_line + b # we adjust this line

plt.scatter(dataset.x, dataset.y)
plt.plot(x_line, y_line, color = 'r', label = 'final_epoch', linewidth = 2)
plt.legend()
plt.savefig('gradient_descent.png')
print('image final saved')

