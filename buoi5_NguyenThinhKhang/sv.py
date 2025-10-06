import sys
import os
import io
from lxml import etree


sys.stdout.reconfigure(encoding='utf-8')
# Đọc file sv.xml
tree = etree.parse("sv.xml")

# 1. Lấy tất cả sinh viên
print("1. Tất cả sinh viên:")
print("".join(etree.tostring(s, encoding="unicode") for s in tree.xpath("/school/student")))

# 2. Liệt kê tên tất cả sinh viên
print("\n2. Tên tất cả sinh viên:")
print(tree.xpath("/school/student/name/text()"))

# 3. Lấy tất cả id của sinh viên
print("\n3. ID của tất cả sinh viên:")
print(tree.xpath("/school/student/id/text()"))

# 4. Lấy ngày sinh của sinh viên có id = 'SV01'
print("\n4. Ngày sinh của SV01:")
print(tree.xpath("/school/student[id='SV01']/date/text()"))

# 5. Lấy các khóa học
print("\n5. Các khóa học:")
print(tree.xpath("/school/enrollment/course/text()"))

# 6. Lấy toàn bộ thông tin của sinh viên đầu tiên
print("\n6. Sinh viên đầu tiên:")
print(etree.tostring(tree.xpath("/school/student[1]")[0], encoding="unicode"))

# 7. Lấy mã sinh viên đăng ký khóa học 'Vatly203'
print("\n7. Mã sinh viên học Vatly203:")
print(tree.xpath("/school/enrollment[course='Vatly203']/studentRef/text()"))

# 8. Lấy tên sinh viên học môn 'Toan101'
print("\n8. Tên sinh viên học Toan101:")
print(tree.xpath("/school/student[id=/school/enrollment[course='Toan101']/studentRef]/name/text()"))

# 9. Lấy tên sinh viên học môn 'Vatly203'
print("\n9. Tên sinh viên học Vatly203:")
print(tree.xpath("/school/student[id=/school/enrollment[course='Vatly203']/studentRef]/name/text()"))

# 10. Lấy ngày sinh của sinh viên có id='SV01'
print("\n10. Ngày sinh SV01:")
print(tree.xpath("/school/student[id='SV01']/date/text()"))

# 11. Lấy tên và ngày sinh của mọi sinh viên sinh năm 1997
print("\n11. Tên và ngày sinh sinh viên năm 1997:")
students_1997 = tree.xpath("/school/student[starts-with(date,'1997')]")
print([s.xpath("concat(name/text(),' - ',date/text())")[0] for s in students_1997])

# 12. Lấy tên của sinh viên có ngày sinh trước năm 1998
print("\n12. Tên sinh viên sinh trước 1998:")
print(tree.xpath("/school/student[number(substring(date,1,4)) < 1998]/name/text()"))

# 13. Đếm tổng số sinh viên
print("\n13. Tổng số sinh viên:")
print(tree.xpath("count(/school/student)"))

# EX.(thêm 2 sinh viên chưa có enrollment)
print(tree.xpath("/school/student[not(id = /school/enrollment/studentRef)]"))

# 14. Lấy phần tử <date> anh em ngay sau <name> của SV01
print("\n14. Thẻ <date> ngay sau <name> của SV01:")
print(tree.xpath("/school/student[id='SV01']/name/following-sibling::date/text()"))

# 15. Lấy phần tử <id> anh em ngay trước <name> của SV02
print("\n15. Thẻ <id> ngay trước <name> của SV02:")
print(tree.xpath("/school/student[id='SV02']/name/preceding-sibling::id/text()"))

# 16. Lấy toàn bộ node <course> trong cùng một <enrollment> với studentRef='SV03'
print("\n16. Môn học của SV03:")
print(tree.xpath("/school/enrollment[studentRef='SV03']/course/text()"))

# 17. Lấy sinh viên có họ là “Trần”
print("\n17. Sinh viên có họ Trần:")
print(tree.xpath("/school/student[starts-with(name,'Trần')]/name/text()"))

# 18. Lấy năm sinh của sinh viên SV01
print("\n18. Năm sinh SV01:")
print(tree.xpath("substring(/school/student[id='SV01']/date/text(),1,4)"))



