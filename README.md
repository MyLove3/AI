# Giải mê cung bằng thuật toán A*

# Giới thiệu

- Đây là một chương trình dùng để tạo và giải các mê cung bằng thuật toán A*. Chương trình cho phép tạo ra mê cung và tìm đường đi ngắn nhất từ điểm bắt đầu đến điểm kết thúc trong mê cung.

- Chúng em tạo ra chương trình này với hy vọng nó có thể được ứng dụng trong nhiều lĩnh vực, từ giải trí đến giảng dạy và nghiên cứu về thuật toán tìm đường. Với Maze Solver, người dùng có thể tạo ra các mê cung độc đáo và thử nghiệm thuật toán A* để tìm ra đường đi ngắn nhất từ điểm bắt đầu đến điểm kết thúc.

- Chúng em đã triển khai thuật toán A* để tìm kiếm đường đi thông qua mê cung. Thuật toán này sử dụng cả thông tin về khoảng cách thực tế từ mỗi điểm đến điểm kết thúc (heuristic) và chi phí đã đi từ điểm bắt đầu đến mỗi điểm để xác định đường đi tốt nhất. Chương trình sử dụng một PriorityQueue để xử lý các node và lưu trữ thông tin về parent node và chi phí tới từng node. Kết quả cuối cùng là một đường đi ngắn nhất được hiển thị trực quan trên mê cung ban đầu.

# Các công nghệ liên quan đến dự án Maze Solver bao gồm:

# Ngôn ngữ lập trình:

- Python: Dự án Maze Solver được viết bằng ngôn ngữ lập trình Python. Python được chọn vì tính đơn giản, dễ đọc và dễ hiểu, cũng như sự phổ biến và hỗ trợ mạnh mẽ từ cộng đồng lập trình Python.

# Các thư viện và module:

- queue: Thư viện Python được sử dụng để triển khai cấu trúc hàng đợi ưu tiên (PriorityQueue) trong thuật toán A*.
- collections: Thư viện Python cung cấp các cấu trúc dữ liệu phổ biến như defaultdict, được sử dụng trong dự án để lưu trữ thông tin về parent node và cost đến node.
- tkinter: Thư viện giao diện đồ họa.
- time: Thư viện được sử dụng để tạo độ trễ trong quá trình vẽ đường đi trên giao diện.
- messagebox: Sử dụng để hiển thị hộp thoại thông báo.

# Hướng dẫn sử dụng và Cách thức hoạt động

Bước 1: Nhập ma trận mê cung vào chương trình, có thể sử dụng mê cung mặc định trong chương trình.

Bước 2: Chạy chương trình.

Sử dụng code chạy trên môi trường Visual Studio Code(một trình chỉnh sửa mã nguồn mã nguồn mở và miễn phí, được phát triển bởi Microsoft).

1.	Hàm generate_maze(rows, cols): Tạo một mê cung ngẫu nhiên với số hàng và số cột cho trước.
2.	Hàm draw_maze(maze): In ra mê cung ban đầu trên màn hình. Mỗi ký tự trong mê cung được biểu diễn bằng các biểu tượng tương ứng(⬜, ⬛, 👸, 🎯, 🟥).
3.	Hàm get_start_and_goal(maze): Tìm và trả về vị trí của ô bắt đầu (start) và ô đích (goal) trong mê cung.
4.	Hàm heuristic(node, goal): Tính toán giá trị heuristic từ một node đến goal. Trong trường hợp này, giá trị heuristic được tính bằng khoảng cách Manhattan giữa node và goal.
5.	Hàm a_star(maze, start, goal): Thực hiện thuật toán A* để tìm đường đi ngắn nhất từ ô bắt đầu (start) đến ô đích (goal) trong mê cung.

Bước 3: Kết quả sẽ được hiển thị trên màn hình.

Sẽ in ra hình ảnh mê cung ban đầu và mê cung đã tìm được đường đi tương ứng bằng A*. Nếu không tìm thấy đường đi, in thông báo "Không tìm thấy đường đi từ start đến goal" và vẽ mê cung ban đầu.

# Mô tả thuật toán A* đã được sử dụng cho code

- Thuật toán A* là thuật toán tìm đường đi trong biểu đồ. Khi áp dụng vào bài toán tìm đường đi ngắn nhất trong mê cung, A* sẽ lần lượt xét các ô lân cận của ô hiện tại để tìm đường đi ngắn nhất từ điểm xuất phát đến điểm kết thúc.

- Trong quá trình tìm kiếm, A* sử dụng hàm heuristic để ước tính khoảng cách từ các ô lân cận đến điểm cuối. Hàm heuristic dùng để đánh giá độ ưu tiên của các ô lân cận, giúp thuật toán tìm đường đi ngắn nhất trong thời gian ngắn nhất.

1. Khởi tạo các biến và cấu trúc dữ liệu:

- Tạo một PriorityQueue để lưu trữ các node cần xét, sắp xếp theo ưu tiên dựa trên chi phí đã đi qua và ước lượng khoảng cách còn lại (priority).
- Tạo một set để lưu trữ các node đã xét.
- Tạo hai dictionary: came_from để lưu trữ thông tin về parent node của mỗi node và cost_so_far để lưu trữ chi phí đã đi qua từ điểm bắt đầu đến mỗi node.

2. Đưa node bắt đầu vào hàng đợi ưu tiên với chi phí đã đi qua là 0 và ưu tiên là ước lượng khoảng cách từ node bắt đầu đến điểm kết thúc.

3. Lặp cho đến khi hàng đợi ưu tiên trống:

- Lấy ra node có ưu tiên thấp nhất từ hàng đợi ưu tiên.
- Nếu node hiện tại là điểm kết thúc, đường đi từ điểm bắt đầu đến điểm kết thúc đã được tìm thấy. Kết thúc vòng lặp.
- Đánh dấu node hiện tại là đã xét bằng cách thêm nó vào tập hợp các node đã xét.

4. Kiểm tra các node láng giềng của node hiện tại:

- Tính toán chi phí mới từ điểm bắt đầu đến node láng giềng thông qua node hiện tại.
- Nếu node láng giềng chưa được xét hoặc chi phí mới nhỏ hơn chi phí đã tính trước đó:
- Cập nhật thông tin về parent node và chi phí cho node láng giềng.
- Tính toán ưu tiên (priority) cho node láng giềng dựa trên chi phí mới và ước lượng khoảng cách còn lại đến điểm kết thúc.
- Đưa node láng giềng vào hàng đợi ưu tiên.

5. Nếu đường đi từ điểm bắt đầu đến điểm kết thúc đã tìm thấy (node kết thúc), thuật toán A* kết thúc.

6. Tạo đường đi từ node bắt đầu đến node kết thúc:

- Bắt đầu từ node kết thúc, theo dấu chỉ của parent node, đi ngược lại để xác định các node trên đường đi.
- Lưu các node này vào một danh sách đường đi.
- Đảo ngược danh sách đường đi để có thứ tự từ node bắt đầu đến node kết thúc.

7. Trả về đường đi tìm thấy.

Trong thuật toán A*, việc lựa chọn ước lượng khoảng cách còn lại (heuristic) có vai trò quan trọng trong việc đánh giá độ ưu tiên của các node. Trong dự án Maze Solver, khoảng cách Manhattan (Manhattan distance) được sử dụng làm hàm heuristic. Nó tính toán khoảng cách theo số bước ngang và bước dọc từ một node đến node kết thúc.

# Kết luận 
Trong bài toán này đã giúp nhóm em tự mình giải quyết được bài toán thực tế tìm kiếm đường đi trong mê cung với chi phí nhỏ nhất giữa hai điểm ta đã biết. Nếu rộng ra là ta sẽ có thể ứng dụng được trong việc xác định được các tuyến đường tốt nhất để đi trên bản đồ khi biết điểm bắt đầu và điểm kết thúc, hay tìm đường đi cho robot vượt chướng ngại vật và tìm đường về đích nhanh nhất,… 
Qua đây chúng em đã học được thêm rất nhiều kiến thức để phục vụ cho việc học tập và công việc sau này. 

