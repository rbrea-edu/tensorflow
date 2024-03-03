# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 16:38:08 2023

@author: Juan
"""


# Crear un perceptron en Keras
import keras 
from keras.models import Sequential
from keras.layers import Dense
import numpy

# Fija las semillas aleatorias para la reproducibilidad
numpy.random.seed(7)

# Establecer los ejemplos y salidas deseadas
# para la función O
X = numpy.array([[0, 0], [0, 1], [1, 0], [1, 1]])
Y = numpy.array([0, 1, 1, 1])
# crea el modelo
ctd_salidas = 1
ctd_entradas = 2
activation='sigmoid'
model = Sequential()
model.add(Dense(1, input_dim = 2, activation='sigmoid'))
#model.summary()
# Compila el modelo
# Recordar que Accuracy se define como 
# Accuracy = (TP + TN) / (TP + TN + FP + FN) 
# donde TP significa True Positive y es cuando el clasificador
# clasificó un ejemplo como positivo y era efectivamente positivo
# mientras que FP (False Positive) cuando lo clasificó como 
# positivo y era negativo.
# Analogamente con TN (que no es Todo Noticias sino que True Negative) y FN.
# Mean square error es la media de los errores al cuadrado
# MSE = (1/n) * Suma_i:1..n (Y - O)^2
# muy parecido a la función de costo que habíamos visto 
opt = keras.optimizers.SGD(learning_rate = 0.01, momentum = 0.0)
model.compile(loss = 'mean_squared_error', optimizer = opt, metrics = ['accuracy'])


# Ajusta el modelo
model.fit(X, Y, epochs = 100, batch_size=4)

# evalua el modelo
scores = model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))