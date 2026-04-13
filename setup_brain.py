import sqlite3
from datetime import datetime

def setup_database():
    # Kết nối (hoặc tạo mới) file database
    conn = sqlite3.connect('brain.db')
    cursor = conn.cursor()

    # Tạo bảng knowledge
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS knowledge (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    # Tạo bảng business
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS business (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    # Tạo bảng brand_voice
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS brand_voice (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    # Thêm dữ liệu mẫu vào knowledge
    cursor.execute("INSERT INTO knowledge (title, content) VALUES (?, ?)", 
                   ("Cách học nhanh", "Sử dụng phương pháp Feynman để giải thích vấn đề phức tạp một cách đơn giản."))
    cursor.execute("INSERT INTO knowledge (title, content) VALUES (?, ?)", 
                   ("Nguyên lý 80/20", "Tập trung vào 20% nỗ lực mang lại 80% kết quả."))

    # Thêm dữ liệu mẫu vào business
    cursor.execute("INSERT INTO business (title, content) VALUES (?, ?)", 
                   ("Sản phẩm A", "Khóa học AI dành cho người mới bắt đầu."))
    cursor.execute("INSERT INTO business (title, content) VALUES (?, ?)", 
                   ("Khách hàng mục tiêu", "Những người làm văn phòng muốn tăng năng suất bằng công cụ AI."))

    # Thêm dữ liệu mẫu vào brand_voice
    cursor.execute("INSERT INTO brand_voice (title, content) VALUES (?, ?)", 
                   ("Tone giọng", "Gần gũi, chuyên nghiệp, dễ hiểu."))
    cursor.execute("INSERT INTO brand_voice (title, content) VALUES (?, ?)", 
                   ("Slogan", "Học AI không khó, đã có Antigravity lo."))

    conn.commit()
    conn.close()
    print("Đã tạo thành công brain.db với 3 bảng và dữ liệu mẫu!")

if __name__ == "__main__":
    setup_database()
