import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Hàm đọc dữ liệu từ file CSV
def load_data(file_path="D:\Mangmaytinh\Lab2.4\sensor_data.csv"):
    try:
        data = pd.read_csv(file_path, parse_dates=['timestamp'])
        return data
    except Exception as e:
        print("Lỗi đọc dữ liệu:", e)
        return None

# Hàm cập nhật biểu đồ, được gọi định kỳ bởi FuncAnimation
def animate(i):
    data = load_data()
    if data is None or data.empty:
        print("Không có dữ liệu")
        return
    
    x = data['timestamp']
    y_temp = data['temperature']
    y_humid = data['humidity']
    
    plt.cla()  # Xóa biểu đồ cũ
    
    # Vẽ nhiệt độ và độ ẩm
    plt.plot(x, y_temp, label='Temperature (°C)', color='red', marker='o')
    plt.plot(x, y_humid, label='Humidity (%)', color='blue', marker='x')
    
    plt.xticks(rotation=45, ha="right")
    plt.xlabel("Time")
    plt.ylabel("Value")
    plt.title("Real-Time IoT Sensor Data")
    plt.legend(loc="upper left")
    plt.tight_layout()

# Tạo figure cho biểu đồ
fig = plt.figure()

# Thiết lập animation: cập nhật mỗi 5 giây
ani = FuncAnimation(fig, animate, interval=5000)

plt.show()
