from lxml import etree
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Đọc file XML
tree = etree.parse("quanlybanan.xml")

# 1. Lấy tất cả bàn
print("1. Tất cả bàn:")
print(tree.xpath("/QUANLY/BANS/BAN"))

# 2. Lấy tất cả nhân viên
print("\n2. Tất cả nhân viên:")
print(tree.xpath("/QUANLY/NHANVIENS/NHANVIEN"))

# 3. Lấy tất cả tên món
print("\n3. Tất cả tên món:")
print(tree.xpath("/QUANLY/MONS/MON/TENMON/text()"))

# 4. Lấy tên nhân viên có mã NV02
print("\n4. Tên nhân viên có mã NV02:")
print(tree.xpath("/QUANLY/NHANVIENS/NHANVIEN[MANV='NV02']/TENV/text()"))

# 5. Lấy tên và số điện thoại của nhân viên NV03
print("\n5. Tên và SĐT của NV03:")
# print(tree.xpath("/QUANLY/NHANVIENS/NHANVIEN[MANV='NV03']/concat(TENV/text(),' - ',SDT/text())"))
ten = tree.xpath("/QUANLY/NHANVIENS/NHANVIEN[MANV='NV03']/TENV/text()")[0]
sdt = tree.xpath("/QUANLY/NHANVIENS/NHANVIEN[MANV='NV03']/SDT/text()")[0]
print(f"{ten} - {sdt}")

# 6. Lấy tên món có giá > 50000
print("\n6. Món có giá > 50,000:")
print(tree.xpath("/QUANLY/MONS/MON[number(GIA) > 50000]/TENMON/text()"))

# 7. Lấy số bàn của hóa đơn HD03
print("\n7. Số bàn của hóa đơn HD03:")
print(tree.xpath("/QUANLY/HOADONS/HOADON[SOHD='HD03']/SOBAN/text()"))

# 8. Lấy tên món có mã M02
print("\n8. Tên món có mã M02:")
print(tree.xpath("/QUANLY/MONS/MON[MAMON='M02']/TENMON/text()"))

# 9. Lấy ngày lập của hóa đơn HD03
print("\n9. Ngày lập hóa đơn HD03:")
print(tree.xpath("/QUANLY/HOADONS/HOADON[SOHD='HD03']/NGAYLAP/text()"))

# 10. Lấy tất cả mã món trong hóa đơn HD01
print("\n10. Mã món trong HD01:")
print(tree.xpath("/QUANLY/HOADONS/HOADON[SOHD='HD01']/CTHDS/CTHD/MAMON/text()"))

# 11. Lấy tên món trong hóa đơn HD01
print("\n11. Tên món trong HD01:")
print(tree.xpath("/QUANLY/MONS/MON[MAMON = /QUANLY/HOADONS/HOADON[SOHD='HD01']/CTHDS/CTHD/MAMON]/TENMON/text()"))

# 12. Lấy tên nhân viên lập hóa đơn HD02
print("\n12. Tên nhân viên lập hóa đơn HD02:")
print(tree.xpath("/QUANLY/NHANVIENS/NHANVIEN[MANV = /QUANLY/HOADONS/HOADON[SOHD='HD02']/MANV]/TENV/text()"))

# 13. Đếm số bàn
print("\n13. Số bàn:")
print(tree.xpath("count(/QUANLY/BANS/BAN)"))

# 14. Đếm số hóa đơn lập bởi NV01
print("\n14. Số hóa đơn lập bởi NV01:")
print(tree.xpath("count(/QUANLY/HOADONS/HOADON[MANV='NV01'])"))

# 15. Lấy tên tất cả món có trong hóa đơn của bàn số 2
print("\n15. Tên món trong hóa đơn của bàn 2:")
print(tree.xpath("/QUANLY/MONS/MON[MAMON = /QUANLY/HOADONS/HOADON[SOBAN='2']/CTHDS/CTHD/MAMON]/TENMON/text()"))

# 16. Lấy tất cả nhân viên từng lập hóa đơn cho bàn số 3
print("\n16. Nhân viên từng lập hóa đơn cho bàn 3:")
print(tree.xpath("/QUANLY/NHANVIENS/NHANVIEN[MANV = /QUANLY/HOADONS/HOADON[SOBAN='3']/MANV]/TENV/text()"))

# 17. Lấy tất cả hóa đơn mà nhân viên nữ lập
print("\n17. Hóa đơn nhân viên nữ lập:")
print(tree.xpath("/QUANLY/HOADONS/HOADON[MANV = /QUANLY/NHANVIENS/NHANVIEN[GIOITINH='Nữ']/MANV]/SOHD/text()"))

# 18. Lấy tất cả nhân viên từng phục vụ bàn số 1
print("\n18. Nhân viên phục vụ bàn 1:")
print(tree.xpath("/QUANLY/NHANVIENS/NHANVIEN[MANV = /QUANLY/HOADONS/HOADON[SOBAN='1']/MANV]/TENV/text()"))

# 19. Lấy tất cả món được gọi nhiều hơn 1 lần trong các hóa đơn
print("\n19. Món được gọi >1 lần:")
print(tree.xpath("/QUANLY/MONS/MON[MAMON = /QUANLY/HOADONS/HOADON/CTHDS/CTHD[number(SOLUONG) > 1]/MAMON]/TENMON/text()"))

# 20. Lấy tên bàn + ngày lập hóa đơn tương ứng SOHD='HD02'
print("\n20. Tên bàn và ngày lập HD02:")
print(tree.xpath("concat(/QUANLY/BANS/BAN[SOBAN = /QUANLY/HOADONS/HOADON[SOHD='HD02']/SOBAN]/TENBAN/text(),' - ',/QUANLY/HOADONS/HOADON[SOHD='HD02']/NGAYLAP/text())"))
