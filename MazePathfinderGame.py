from queue import PriorityQueue
from collections import defaultdict
import random
import tkinter as tk
import time
from tkinter import messagebox

###########################################################################################################
# Tạo từ điển các ký hiệu
symbols = {'.': '⬜',  # Đường đi
           '#': '⬛',  # Tường
           'S': '👸',  # Start
           'G': '🎯',  # Goal
           'W': '🟥'}  # Way

###########################################################################################################
# khởi tạo mê cung
maze = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
        ['#', '#', '.', '#', '#', '#', '.', '#', '#', '.', '#', '#', '.', '#', '.', '#', '.', '.', '#', '#'],
        ['#', '#', '.', '#', '.', '.', '.', '#', '.', '#', '.', '#', '.', '#', '.', '#', '.', '.', '.', '#'],
        ['#', '#', '.', '#', '#', '#', '.', '#', 'S', '#', '#', '#', '.', '#', '.', '#', '#', '#', '.', '#'],
        ['#', '#', '.', '#', '.', '#', '.', '.', '.', '#', '.', '#', '.', '.', '.', '.', '#', '.', '.', '#'],
        ['#', '#', '.', '#', '#', '#', '#', '.', '#', '.', '#', '#', '#', '#', '.', '#', '#', '#', '#', '#'],
        ['#', '#', '.', '.', '.', '#', '.', '.', '.', '.', '#', '.', '.', '.', '.', '.', '#', '.', '.', '#'],
        ['#', '#', '.', '#', '.', '#', '#', '#', '.', '#', '#', '#', '.', '#', '#', '.', '#', '.', '#', '#'],
        ['#', '#', '.', '#', '.', '.', '.', '#', '.', '.', '.', '.', '#', '.', '#', '.', '#', '.', '#', '#'],
        ['#', '#', '#', '#', '.', '#', '#', '#', '#', '#', '#', '#', '#', '#', '.', '#', '#', '#', '.', '#'],
        ['#', '#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#', '.', '.', '.', '.', '#'],
        ['#', '#', '#', '#', '.', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '.', '#', '#', '#', '#'],
        ['#', '#', '.', '.', '.', '.', '#', '.', '#', '.', '.', '.', '#', '.', '.', '.', '#', '.', '.', '#'],
        ['#', '#', '#', '#', '.', '#', '#', '#', '#', '.', '#', '#', '#', '.', '#', '#', '#', '#', '.', '#'],
        ['#', '#', '.', '.', '.', '#', '.', '.', '.', '#', '.', '.', '.', '.', '.', '.', '#', '.', '.', '#'],
        ['#', '#', '.', '#', '.', '#', '#', '#', '.', '#', '#', '#', '.', '#', '#', '.', '#', '.', '#', '#'],
        ['#', '#', '.', '#', '.', '#', '.', '#', '.', '#', '.', '.', '.', '#', '.', '#', '.', 'G', '#', '#'],
        ['#', '#', '.', '#', '#', '#', '.', '#', '#', '#', '.', '#', '#', '#', '.', '#', '#', '#', '.', '#'],
        ['#', '#', '.', '.', '.', '#', '.', '.', '.', '#', '.', '#', '.', '.', '.', '#', '.', '.', '.', '#']]


 
    


###########################################################################################################
# Vẽ mê cung ban đầu
def draw_maze(maze):
    print('Mê cung ban đầu:\n')
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 'S':
                print(symbols['S'], end='')
            elif maze[i][j] == 'G':
                print(symbols['G'], end='')
            elif maze[i][j] == '.':
                print(symbols['.'], end='')
            else:
                print(symbols['#'], end='')
        print()
    print()


###########################################################################################################
# Lấy tọa độ start và goal
def get_start_and_goal(maze):
    start = None
    goal = None
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 'S':
                print(f'Found start node at ({i}, {j})\n')
                start = (i, j)
            elif maze[i][j] == 'G':
                print(f'Found goal node at ({i}, {j})\n')
                goal = (i, j)
    return start, goal


###########################################################################################################
def heuristic(node, goal):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])


###########################################################################################################
# Các hằng số
CELL_SIZE = 40
DELAY = 0.2

# Hàm vẽ mê cung với đường đi
def draw_maze_with_path(maze, path, total_cost):
    # Tạo cửa sổ tkinter
    window = tk.Tk()
    window.title("Maze Solver")
    canvas = tk.Canvas(window, width=len(maze[0]) * CELL_SIZE, height=len(maze) * CELL_SIZE)
    canvas.pack()

    # Vẽ mê cung ban đầu
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            x1 = j * CELL_SIZE
            y1 = i * CELL_SIZE
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE

            if maze[i][j] == '#':
                canvas.create_rectangle(x1, y1, x2, y2, fill="black")
            elif maze[i][j] == 'S':
                canvas.create_rectangle(x1, y1, x2, y2, fill="green")
            elif maze[i][j] == 'G':
                canvas.create_rectangle(x1, y1, x2, y2, fill="red")
            else:
                canvas.create_rectangle(x1, y1, x2, y2, fill="white")

    # Vẽ đường đi
    for i in range(len(path) - 1):
        x1 = path[i][1] * CELL_SIZE + CELL_SIZE // 2
        y1 = path[i][0] * CELL_SIZE + CELL_SIZE // 2
        x2 = path[i+1][1] * CELL_SIZE + CELL_SIZE // 2
        y2 = path[i+1][0] * CELL_SIZE + CELL_SIZE // 2

        # Kiểm tra xem các phần tử trong đường đi có hợp lệ hay không trước khi vẽ
        if 0 <= x1 < len(maze[0]) * CELL_SIZE and 0 <= y1 < len(maze) * CELL_SIZE and \
                0 <= x2 < len(maze[0]) * CELL_SIZE and 0 <= y2 < len(maze) * CELL_SIZE:
            canvas.create_line(x1, y1, x2, y2, fill="blue", width=2)

        window.update()
        time.sleep(DELAY)
    
    # Hiển thị tổng chi phí sử dụng message box
    messagebox.showinfo("Tổng chi phí", "Tổng chi phí: " + str(total_cost))

    # Hiển thị cửa sổ
    window.mainloop()

###########################################################################################################
def calculate_total_cost(path):
    total_cost = 0
    for i in range(len(path) - 1):
        current_node = path[i]
        next_node = path[i+1]
        # Giả sử chi phí giữa các nút kề nhau là 1
        total_cost += 1
    return total_cost

###########################################################################################################

def a_star(maze, start, goal):
    # Giải mê cung bằng thuật toán A*
    # Trả về đường đi ngắn nhất từ start đến goal

    # Tạo một set để lưu các node đã xét
    closed_set = set()

    # Tạo một PriorityQueue để lưu các node cần xét
    open_set = PriorityQueue()

    # Đưa node start vào open_set với cost = 0 và priority = heuristic(start, goal)
    open_set.put((heuristic(start, goal), 0, start))

    # Tạo một dictionary để lưu trữ thông tin về parent node và cost đến node đó
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    found_path = False  # Biến kiểm tra xem đã tìm thấy đường đi hay chưa

    while not open_set.empty():
        # Lấy ra node có priority thấp nhất trong open_set
        current = open_set.get()[2]
        if current == goal:
            # Đã tìm thấy đường đi ngắn nhất từ start đến goal
            found_path = True
            break

        # Đánh dấu node hiện tại là đã xét
        closed_set.add(current)

        # Kiểm tra các node lân cận của node hiện tại
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            x, y = current[0] + dx, current[1] + dy
            if 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != '#':
                # Tính toán cost từ start đến node kế tiếp
                new_cost = cost_so_far[current] + 1
                if (x, y) not in cost_so_far or new_cost < cost_so_far[(x, y)]:
                    # Nếu node chưa được xét hoặc cost mới nhỏ hơn cost cũ

                    # Cập nhật thông tin cost và parent node của node kế tiếp
                    cost_so_far[(x, y)] = new_cost
                    came_from[(x, y)] = current

                    # Tính toán priority của node kế tiếp và đưa vào open_set
                    priority = new_cost + heuristic((x, y), goal)
                    open_set.put((priority, new_cost, (x, y)))

                    # In ra thông tin của node kế tiếp nếu đã tìm thấy đường đi
  
                    print(f'Node ({x}, {y}): cost={new_cost}, heuristic={heuristic((x, y), goal)}')
                    print()

    # Tạo đường đi từ start đến goal
    if found_path:

        # In ra đường đi ngắn nhất nếu tìm thấy đường
        path = []
        node = goal
        while node != start:
            path.append(node)
            node = came_from[node]
        path.append(start)
        path.reverse()
    path = []
    current = goal
    while current != start:
        path.append(current)
        if current in came_from:
            current = came_from[current]
            
        else:
            # Không tìm thấy đường đi từ start đến goal
            print("Không tìm thấy đường đi từ start đến goal.\n")
            draw_maze(maze)
            return []

    path.append(start)
    path.reverse()
    path_set = set(path)
    
    print("Vay duong di ngan nhat la: ")
    print("->".join(str(p) for p in path))
    print()


    # Đường đi theo A*  
    draw_maze(maze) 
    print('Đường đi theo A*:\n')
    for i, row in enumerate(maze):
        for j, col in enumerate(row):
            if (i,j) == start:
                print(symbols['S'], end='')  # Ký hiệu node start
            elif (i, j) == goal:
                print(symbols['G'], end='')  # Ký hiệu node goal
            elif (i, j) in path_set:
                print(symbols['W'], end='')  # Ký hiệu đường đã đi
            else:
                print(symbols[col], end='')
        print()
    return path

###########################################################################################################

def g_b_f_s(maze, start, goal):
    # Tạo một set để lưu các node đã xét
    visited = set()

    # Tạo một PriorityQueue để lưu các node cần xét
    open_set = PriorityQueue()

    # Đưa node start vào open_set với priority là heuristic(start, goal)
    open_set.put((heuristic(start, goal), start))

    # Tạo một dictionary để lưu trữ thông tin về parent node và cost đến node đó
    came_from = {}
    came_from[start] = None

    while not open_set.empty():
        # Lấy ra node có priority thấp nhất trong open_set
        current_priority, current = open_set.get()
        if current == goal:
            # Đã tìm thấy đường đi từ start đến goal
            break

        # Đánh dấu node hiện tại là đã xét
        visited.add(current)

        # Kiểm tra các node lân cận của node hiện tại
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            x, y = current[0] + dx, current[1] + dy
            if 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != '#':
                neighbor = (x, y)
                if neighbor not in visited:
                    # Cập nhật parent node của node lân cận
                    came_from[neighbor] = current

                    # Đưa node lân cận vào open_set với priority là heuristic(neighbor, goal)
                    open_set.put((heuristic(neighbor, goal), neighbor))

    # Tạo đường đi từ start đến goal
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = came_from[current]

    path.append(start)
    path.reverse()
    return path


def ucs(maze, start, goal):
    # Tạo một set để lưu các node đã xét
    visited = set()

    # Tạo một PriorityQueue để lưu các node cần xét
    open_set = PriorityQueue()

    # Đưa node start vào open_set với cost là 0
    open_set.put((0, start))

    # Tạo một dictionary để lưu trữ thông tin về parent node và cost đến node đó
    came_from = {}
    came_from[start] = None

    # Tạo một dictionary để lưu trữ cost từ start đến mỗi node
    cost_so_far = {}
    cost_so_far[start] = 0

    while not open_set.empty():
        # Lấy ra node có cost thấp nhất trong open_set
        current_cost, current = open_set.get()
        if current == goal:
            # Đã tìm thấy đường đi từ start đến goal
            break

        # Đánh dấu node hiện tại là đã xét
        visited.add(current)

        # Kiểm tra các node lân cận của node hiện tại
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            x, y = current[0] + dx, current[1] + dy
            if 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != '#':
                neighbor = (x, y)
                # Tính toán cost mới từ start đến neighbor thông qua node hiện tại
                new_cost = cost_so_far[current] + 1  # Giả sử cost giữa các node là 1

                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    # Cập nhật parent node của node lân cận
                    came_from[neighbor] = current

                    # Cập nhật cost từ start đến node lân cận
                    cost_so_far[neighbor] = new_cost

                    # Đưa node lân cận vào open_set với cost là new_cost
                    open_set.put((new_cost, neighbor))

    # Tạo đường đi từ start đến goal
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = came_from[current]

    path.append(start)
    path.reverse()
    return path


def bfs(maze, start, goal):
    # Tạo một hàng đợi (queue) để lưu các node cần xét
    queue = []

    # Đưa node start vào hàng đợi
    queue.append(start)

    # Tạo một set để lưu các node đã xét
    visited = set()

    # Tạo một dictionary để lưu trữ thông tin về parent node
    came_from = {}
    came_from[start] = None

    while queue:
        # Lấy ra node đầu tiên trong hàng đợi
        current = queue.pop(0)
        if current == goal:
            # Đã tìm thấy đường đi từ start đến goal
            break

        # Đánh dấu node hiện tại là đã xét
        visited.add(current)

        # Kiểm tra các node lân cận của node hiện tại
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            x, y = current[0] + dx, current[1] + dy
            if 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != '#':
                neighbor = (x, y)
                if neighbor not in visited and neighbor not in queue:
                    # Đưa node lân cận vào hàng đợi
                    queue.append(neighbor)

                    # Cập nhật parent node của node lân cận
                    came_from[neighbor] = current

    # Tạo đường đi từ start đến goal
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = came_from[current]

    path.append(start)
    path.reverse()
    return path


def dfs(maze, start, goal):
    # Tạo một stack để lưu trữ các node cần xét
    stack = []

    # Đưa node start vào stack
    stack.append(start)

    # Tạo một set để lưu trữ các node đã xét
    visited = set()

    # Tạo một dictionary để lưu trữ thông tin về parent node
    came_from = {}
    came_from[start] = None

    while stack:
        # Lấy ra node trên cùng của stack
        current = stack.pop()
        if current == goal:
            # Đã tìm thấy đường đi từ start đến goal
            break

        # Đánh dấu node hiện tại là đã xét
        visited.add(current)

        # Kiểm tra các node lân cận của node hiện tại
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            x, y = current[0] + dx, current[1] + dy
            if 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != '#':
                neighbor = (x, y)
                if neighbor not in visited and neighbor not in stack:
                    # Đưa node lân cận vào stack
                    stack.append(neighbor)

                    # Cập nhật parent node của node lân cận
                    came_from[neighbor] = current

    # Tạo đường đi từ start đến goal
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = came_from[current]

    path.append(start)
    path.reverse()
    return path




def create_game_window(maze, solve_func, exit_func):
    # Tạo cửa sổ giao diện
    root = tk.Tk()
    root.title("MazePathfinderGame")

    # Tạo canvas để vẽ mê cung
    canvas = tk.Canvas(root, width=len(maze[0]) * CELL_SIZE, height=len(maze) * CELL_SIZE)
    canvas.pack()

    # Thêm nút "Solve Maze"
    solve_button = tk.Button(root, text="Chạy mê cung", command=solve_func)
    solve_button.pack()

    # Thêm nút "Exit"
    exit_button = tk.Button(root, text="Thoát", command=exit_func)
    exit_button.pack()

    # Hiển thị cửa sổ
    root.mainloop()


def exit_game():
    root.quit()





