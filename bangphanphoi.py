import pandas as pd

# Đọc dữ liệu từ file Excel
df = pd.read_excel("ketqua_diemthi.xlsx")

# Danh sách các môn học
subjects = ['Toan', 'Van', 'NgoaiNgu', 'VatLy', 'HoaHoc', 'SinhHoc', 'DiemTBTuNhien', 'LichSu', 'DiaLy', 'GDCD', 'DiemTBXaHoi']

# Tạo danh sách lưu các thông tin thống kê
stats = []

for subject in subjects:
    data = df[subject].dropna()
    
    # Tính các thông số thống kê
    mean = data.mean()
    median = data.median()
    std_dev = data.std()
    range_val = data.max() - data.min()
    count = data.count()
    
    # Tính số lượng giá trị ngoại lệ
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1
    outliers = data[(data < (Q1 - 1.5 * IQR)) | (data > (Q3 + 1.5 * IQR))].count()
    
    # Thêm thông tin vào danh sách
    stats.append({
        'Môn học': subject,
        'Trung bình': mean,
        'Trung vị': median,
        'Độ lệch chuẩn': std_dev,
        'Khoảng': range_val,
        'Số lượng học sinh': count,
        'Số lượng giá trị ngoại lệ': outliers
    })

# Chuyển danh sách thành DataFrame
stats_df = pd.DataFrame(stats)

# Lưu DataFrame vào file Excel
stats_df.to_excel("phanduoc_diemtong_hoc.xlsx", index=False)

print("Bảng phân phối chi tiết đã được lưu vào 'phanduoc_diemtong_hoc.xlsx'")
