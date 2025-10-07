from lxml import etree
import mysql.connector
import sys

sys.stdout.reconfigure(encoding='utf-8')

# ======== 1. Đọc & kiểm tra XML - XSD ========
xml_tree = etree.parse("product.xml")
xsd_tree = etree.parse("product.xsd")
schema = etree.XMLSchema(xsd_tree)

if not schema.validate(xml_tree):
    print("❌ XML không hợp lệ với XSD!")
    print(schema.error_log.last_error)
    sys.exit()
else:
    print("✅ XML hợp lệ với XSD, bắt đầu xử lý dữ liệu...")

# ======== 2. Kết nối MySQL ========
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="th_xml"
    )
    cursor = conn.cursor()
    print("✅ Kết nối MySQL thành công.")
except Exception as e:
    print("❌ Lỗi khi kết nối MySQL:", e)
    sys.exit()

# ======== 3. Tạo bảng nếu chưa có ========
cursor.execute("""
CREATE TABLE IF NOT EXISTS categories (
    id VARCHAR(10) PRIMARY KEY,
    name VARCHAR(100)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id VARCHAR(10) PRIMARY KEY,
    name VARCHAR(100),
    price DECIMAL(10,2),
    currency VARCHAR(10),
    stock INT,
    categoryRef VARCHAR(10),
    FOREIGN KEY (categoryRef) REFERENCES categories(id)
)
""")
conn.commit()

# ======== 4. Lấy dữ liệu từ XML bằng XPath thuần ========

# 📂 Danh mục
cat_ids = xml_tree.xpath("/catalog/categories/category/@id")
cat_names = xml_tree.xpath("/catalog/categories/category/text()")

print("\n📂 Danh mục có trong XML:")
for i, name in zip(cat_ids, cat_names):
    print(f"  - {i}: {name}")
    cursor.execute("""
        INSERT INTO categories (id, name)
        VALUES (%s, %s)
        ON DUPLICATE KEY UPDATE name = VALUES(name)
    """, (i, name.strip()))
conn.commit()

# 🛒 Sản phẩm
prod_ids = xml_tree.xpath("/catalog/products/product/@id")
prod_refs = xml_tree.xpath("/catalog/products/product/@categoryRef")
prod_names = xml_tree.xpath("/catalog/products/product/name/text()")
prod_prices = xml_tree.xpath("/catalog/products/product/price/text()")
prod_currs = xml_tree.xpath("/catalog/products/product/price/@currency")
prod_stocks = xml_tree.xpath("/catalog/products/product/stock/text()")

print("\n🛒 Sản phẩm có trong XML:")
for pid, ref, name, price, curr, stock in zip(
    prod_ids, prod_refs, prod_names, prod_prices, prod_currs, prod_stocks
):
    print(f"  - {pid}: {name} ({price} {curr}), tồn: {stock}, loại: {ref}")
    cursor.execute("""
        INSERT INTO products (id, name, price, currency, stock, categoryRef)
        VALUES (%s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            name = VALUES(name),
            price = VALUES(price),
            currency = VALUES(currency),
            stock = VALUES(stock),
            categoryRef = VALUES(categoryRef)
    """, (pid, name.strip(), float(price), curr, int(stock), ref))
conn.commit()

# ======== 5. Kiểm tra dữ liệu ========
cursor.execute("SELECT * FROM categories")
print("\n📋 Bảng categories:")
for row in cursor.fetchall():
    print(row)

cursor.execute("SELECT * FROM products")
print("\n📋 Bảng products:")
for row in cursor.fetchall():
    print(row)

# ======== 6. Đóng kết nối ========
cursor.close()
conn.close()
print("\n✅ Dữ liệu đã được lưu thành công!")
