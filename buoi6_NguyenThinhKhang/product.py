from lxml import etree

# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Đọc và phân tích file XML
xml_tree = etree.parse("product.xml")

# Đọc và phân tích file XSD
xsd_tree = etree.parse("product.xsd")

# Tạo XMLSchema object
schema = etree.XMLSchema(xsd_tree)

# Kiểm tra hợp lệ
if schema.validate(xml_tree):
    print("✅ XML hợp lệ với XSD.")
else:
    print("❌ XML không hợp lệ với XSD!")
    print(schema.error_log.last_error)

# --- XPath ---

# Tất cả danh mục
print("\n1. Tất cả danh mục:")
print("".join(etree.tostring(c, encoding="unicode") for c in xml_tree.xpath("/catalog/categories/category")))

# Tên tất cả danh mục
print("\n2. Tên tất cả danh mục:")
print(xml_tree.xpath("/catalog/categories/category/text()"))

# ID của tất cả danh mục
print("\n3. ID của tất cả danh mục:")
print(xml_tree.xpath("/catalog/categories/category/@id"))

# Tất cả sản phẩm
print("\n4. Tất cả sản phẩm:")
print("".join(etree.tostring(p, encoding="unicode") for p in xml_tree.xpath("/catalog/products/product")))

# ID của tất cả sản phẩm
print("\n5. ID của tất cả sản phẩm:")
print(xml_tree.xpath("/catalog/products/product/@id"))

# Tên tất cả sản phẩm
print("\n6. Tên tất cả sản phẩm:")
print(xml_tree.xpath("/catalog/products/product/name/text()"))

# Giá tất cả sản phẩm
print("\n7. Giá tất cả sản phẩm:")
print(xml_tree.xpath("/catalog/products/product/price/text()"))

# Thuộc tính tiền tệ của sản phẩm
print("\n8. Tiền tệ của từng sản phẩm:")
print(xml_tree.xpath("/catalog/products/product/price/@currency"))

# Lấy toàn bộ tên và tồn kho của sản phẩm
print("\n9. Tên và tồn kho của sản phẩm:")
names = xml_tree.xpath("/catalog/products/product/name/text()")
stocks = xml_tree.xpath("/catalog/products/product/stock/text()")
for n, s in zip(names, stocks):
    print(f"- {n}: tồn {s} cái")

