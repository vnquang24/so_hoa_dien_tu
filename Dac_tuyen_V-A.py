import matplotlib.pyplot as plt
import numpy as np

# Hằng số
V_BE = 0.7  # Điện áp base-emitter (V)
V_T = 26e-3  # Điện áp nhiệt độ (V)
beta = 100  # Hệ số khuếch đại dòng base

# Các giá trị dòng base (uA)
i_B_values = np.array([5, 10, 15, 20, 25, 30]) * 1e-6  # Chuyển đổi từ uA sang A

# Các giá trị điện áp collector-emitter (V)
V_CE_values = np.linspace(0, 12, 500)  # Tạo một dãy giá trị từ 0 đến 12 với 500 điểm

# Vẽ đặc tính V-A
plt.figure()
for i_B in i_B_values:
    # Tính dòng collector (I_C) sử dụng mô hình tuyến tính từng đoạn
    i_C_values = np.where(V_CE_values < V_BE, i_B * (V_CE_values / V_BE), i_B * beta)
    plt.plot(V_CE_values, i_C_values * 1e3, label=f'i_B = {round(i_B * 1e6)} uA')  # Chuyển đổi từ A sang mA và thêm chú thích

plt.xlabel('Điện áp Collector-Emitter V_CE (V)')
plt.ylabel('Dòng Collector I_C (mA)')
plt.title('Đặc tính V-A')
plt.grid(True)
plt.ylim(0, 3.2)  # Giới hạn phạm vi của trục y để tập trung vào khu vực quan tâm

# Chú thích thêm điểm 0.7V trên trục hoành
plt.annotate('0.7V', xy=(0.7, 0), xytext=(0.7, -0.3), arrowprops=dict(facecolor='black', shrink=0.05))

# Di chuyển chú thích của i_B xuống góc dưới bên phải
plt.legend(loc='lower right')

plt.show()