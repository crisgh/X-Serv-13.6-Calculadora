#!/usr/bin/python
# -*- coding: utf-8 -*-
# mejorado
import sys

if len(sys.argv) != 4:
   # print ("Solo acepto 3 parametros")
    sys.exit("Use : operacion numero numero")
    
# _,operador,op1,op2 = sys.argv

operador = sys.argv[1]

operadores = ["suma","resta","multi", "div"]

if operador not in operadores:
    sys.exit("Solo acepto suma,resta,multi, div")

try:
    op1 = float(sys.argv[2])
    op2 = float(sys.argv[3])
except ValueError:
    sys.exit("Dame un numero")

if operador == "suma" :
    print op1 + op2
if operador == "resta":
    print op1 - op2
if operador == "multi" :
    print op1 * op2
if operador == "div":
    try:
        print op1 / op2
    except ZeroDivisionError:
        print ("¡No dividas entre cero!")
