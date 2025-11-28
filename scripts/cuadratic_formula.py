from math import *
import numpy as np

def cuadratic_formula (a=int, b=int, c=int):
    """Sean a,b,c numeros reales tal que ax**2+bx+c=0, con a distinto a 0.
    Se admiten resultados complejos."""
    dis = b ** 2 - 4 * a * c
    
    x1 = -b + dis ** (1/2) / (2 * a)
    
    x2 = -b - dis ** (1/2) / (2 * a)
    
    x=[x1,x2]
    print(x1,x2)
    return (x)

def matmult (a11=float,a21=float,a31=float,a12=float,a22=float,a32=float,a13=float,a23=float,a33=float,b11=float,b21=float,b31=float,b12=float,b22=float,b32=float,b13=float,b23=float,b33=float):
    """Sean A y B dos matrices de 3x3"""
    a_matrix = np.array([[a11,a12,a13],[a21,a22,a23],[a31,a32,a33]])
    b_matrix = np.array([[b11,b12,b13],[b21,b22,b23],[b31,b32,b33]])

    #print(a_matrix)
    #print(b_matrix)

    ab_matrix = np.linalg.matmul(a_matrix,b_matrix)    
    print(ab_matrix)
    return ab_matrix

def matinv (a11=float,a21=float,a31=float,a12=float,a22=float,a32=float,a13=float,a23=float,a33=float):
    """Sean A una matriz de 3x3"""
    a_matrix = np.array([[a11,a12,a13],[a21,a22,a23],[a31,a32,a33]])
    #print(a_matrix)
    #print(b_matrix)

    inv_matrix = np.linalg.inv(a_matrix)    
    print(inv_matrix)
    return inv_matrix
