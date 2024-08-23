import requests
import pandas as pd

# Tạo danh sách để lưu dữ liệu
data = []

for i in range(26000001, 26001000):
    scraping_url = f"https://dantri.com.vn/thpt/1/0/99/{i}/2024/0.2/search-gradle.htm"
    payload = {}
    header = {}
    respond = requests.get(scraping_url, headers=header, data=payload)
    
    try:
        info = respond.json()['student']
        diem = {
            "SBD": info['sbd'],
            "Toan": info['toan'],
            "Van": info['van'],
            "NgoaiNgu": info['ngoaiNgu'],
            "VatLy": info['vatLy'],
            "HoaHoc": info['hoaHoc'],
            "SinhHoc": info['sinhHoc'],
            "DiemTBTuNhien": info['diemTBTuNhien'],
            "LichSu": info['lichSu'],
            "DiaLy": info['diaLy'],
            "GDCD": info['gdcd'],
            "DiemTBXaHoi": info['diemTBXaHoi']
        }
        data.append(diem)
    except KeyError:
        print(f"Không tìm thấy dữ liệu cho SBD {i}")

# Chuyển danh sách thành DataFrame
df = pd.DataFrame(data)

# Lưu DataFrame vào file Excel
df.to_excel("ketqua_diemthi.xlsx", index=False)

