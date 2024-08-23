import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu từ file Excel
df = pd.read_excel("ketqua_diemthi.xlsx")


#  Phân tích phân phối điểm
# Histogram cho từng môn học
subjects = ['Toan', 'Van', 'NgoaiNgu', 'VatLy', 'HoaHoc', 'SinhHoc', 'DiemTBTuNhien', 'LichSu', 'DiaLy', 'GDCD', 'DiemTBXaHoi']

for subject in subjects:
    plt.figure(figsize=(8, 6))
    plt.hist(df[subject].dropna(), bins=20, color='skyblue', edgecolor='black')
    plt.title(f'Phân phối điểm - {subject}')
    plt.xlabel('Điểm')
    plt.ylabel('Số lượng học sinh')
    plt.grid(True)
    plt.show()

# Box plot cho từng môn học
plt.figure(figsize=(12, 8))
df[subjects].boxplot()
plt.title('Phân phối điểm qua Box plot')
plt.xticks(rotation=45)
plt.ylabel('Điểm')
plt.grid(True)
plt.show()
