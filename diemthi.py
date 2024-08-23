import requests
for i in range (26000001, 26001000):
    scraping_url= f"https://dantri.com.vn/thpt/1/0/99/{i}/2024/0.2/search-gradle.htm"
    payload={}
    header={}
    respond = requests.request("GET", scraping_url, headers=header, data=payload)
    info = respond.json()['student']
    diem ="SBD {} Toan {} Van {} NgoaiNgu {} VatLy {} HoaHoc {} SinhHoc {} DiemTBTuNhien {} LichSu {} DiaLy {} GDCD {} DiemTBXaHoi {}".format(info['sbd'], info['toan'], info['van'], info['ngoaiNgu'], info['vatLy'], info['hoaHoc'], info['sinhHoc'], info['diemTBTuNhien'], info['lichSu'], info['diaLy'], info['gdcd'], info['diemTBXaHoi'] )
    diemthi=str(diem)
    print(diemthi)