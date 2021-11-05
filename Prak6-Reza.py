# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 19:26:01 2021

@author: rezakurniawan
"""
import math

print('Menghitung Kecepatan Akhir ( GLBB ) - Diketahui Jarak Tempuh')

def kecepatan_akhir(vo, a, s):
    vt = math.sqrt(vo**2 + (2 * a * s))
    print(f"""Kecepatan akhir jika kecepatan awal = {vo},
          percepatan = {a},
          dan jarak tempuh {s},
          adalah = {vt}""")
  
kecepatan_awal = int(input('Masukkan v0 (kecepatan awal): '))
percepatan = int(input('Masukkan a (percepatan): '))
jarak = int(input('Masukkan s (jarak tempuh): '))

kecepatan_akhir(kecepatan_awal, percepatan, jarak)