from queue import PriorityQueue
from collections import defaultdict
import random
import tkinter as tk
import time
from tkinter import messagebox
from MazePathfinderGame import draw_maze, get_start_and_goal, heuristic, draw_maze_with_path,calculate_total_cost,a_star,dfs,bfs,ucs,g_b_f_s,maze,CELL_SIZE,create_game_window,exit_game



start, goal = get_start_and_goal(maze)


    

import time

def solve_maze():
    start_time = time.time()  # Ghi lại thời điểm bắt đầu tìm đường
    
    
    #path = g_b_f_s(maze, start, goal)
    path = a_star(maze, start, goal)
    #path = ucs(maze, start, goal)
    #path = bfs(maze, start, goal)
    
    #path = g_b_f_s(maze, start, goal)
    total_cost = calculate_total_cost(path)
    draw_maze_with_path(maze, path, total_cost)
    
    end_time = time.time()  # Ghi lại thời điểm kết thúc tìm đường
    elapsed_time = end_time - start_time  # Tính thời gian đã trôi qua
    
    messagebox.showinfo("Thời gian tìm đường", f"Thời gian tìm đường: {elapsed_time:.2f} giây")



create_game_window(maze, solve_maze, exit_game)
