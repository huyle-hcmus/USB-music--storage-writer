import serial
import struct

# Cổng UART - điều chỉnh theo cấu hình
uart_port = 'COM5'
uart_baudrate = 115200

# Tên tập tin âm thanh WAV
audio_file_path = 'music.wav'

# Mở cổng UART
ser = serial.Serial(uart_port, uart_baudrate)

# Đọc dữ liệu từ tập tin và gửi qua UART
audio_file = open(audio_file_path, 'rb+')

# Đọc thông tin header
riff_chunk = audio_file.read(12)
fmt_chunk = audio_file.read(24)

# Tính kích thước dữ liệu
data_chunk_id = audio_file.read(4)
data_chunk_size = struct.unpack('<I', audio_file.read(4))[0]

# Cập nhật kích thước dữ liệu
new_data_chunk_size = len(audio_file.read())
audio_file.seek(40)  # Chuyển con trỏ đến vị trí byte 40 (sau fmt chunk và trước data chunk)
audio_file.write(struct.pack('<I', new_data_chunk_size))  # Ghi kích thước mới

# Đóng tập tin và mở lại để cập nhật kích thước dữ liệu
audio_file.seek(0)  # Chuyển con trỏ về đầu file
data = audio_file.read()  # Đọc lại toàn bộ dữ liệu
ser.write(data)  # Gửi qua UART

# Đóng tập tin
audio_file.close()

# Đóng cổng UART
ser.close()