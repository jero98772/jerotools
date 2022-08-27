#!/usr/bin/env python 
# -*- coding: utf-8 -*-"
"""
jerotools - 2022 - por jero98772
jerotools - 2022 - by jero98772
"""
def dfs(matriz, x, y):
  matriz[x][y]  = 0  
  n, m = len(matriz), len(matriz[0])
  for fila in (0, 1, -1):
    for col in (0, 1, -1):
      newx, newy = x + fila, y + col
      if 0 <= newx < n and 0 <= newy < m:
        if matriz[newx][newy] == 0:
          continue
        dfs(matriz, newx, newy)

def treeSize(tree,count):
	if not tree.right:
	     irdaux(tree.right,count+1)
	if not tree.left:
	     irdaux(tree.left,count+1)
	else: return count   