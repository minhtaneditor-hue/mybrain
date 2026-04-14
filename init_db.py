import sqlite3
import os

def init_db():
    db_path = 'brain.db'
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create tables
    tables = {
        'knowledge': ['id INTEGER PRIMARY KEY AUTOINCREMENT', 'title TEXT', 'content TEXT', 'created_at DATETIME DEFAULT CURRENT_TIMESTAMP'],
        'business': ['id INTEGER PRIMARY KEY AUTOINCREMENT', 'title TEXT', 'content TEXT', 'created_at DATETIME DEFAULT CURRENT_TIMESTAMP'],
        'brand_voice': ['id INTEGER PRIMARY KEY AUTOINCREMENT', 'title TEXT', 'content TEXT', 'created_at DATETIME DEFAULT CURRENT_TIMESTAMP']
    }

    for table_name, columns in tables.items():
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(columns)})")
    
    # Add sample data
    sample_data = {
        'knowledge': [
            ('Nguyên lý 80/20', '80% kết quả đến từ 20% nỗ lực quan trọng nhất.'),
            ('Kỹ thuật Feynman', 'Để hiểu một vấn đề, hãy giải thích nó thật đơn giản cho một đứa trẻ.')
        ],
        'business': [
            ('Sản phẩm A', 'Khóa học xây dựng bộ não thứ 2 với AI.'),
            ('Khách hàng tiềm năng', 'Những người muốn tối ưu hiệu suất làm việc bằng công nghệ.')
        ],
        'brand_voice': [
            ('Tone giọng mục tiêu', 'Gần gũi, thực tế, tập trung vào kết quả.'),
            ('Giá trị cốt lõi', 'Chia sẻ kiến thức thực chiến, không nói lý thuyết suông.')
        ]
    }

    for table_name, data in sample_data.items():
        # Check if data already exists to avoid duplicates
        cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
        if cursor.fetchone()[0] == 0:
            cursor.executemany(f"INSERT INTO {table_name} (title, content) VALUES (?, ?)", data)

    conn.commit()
    conn.close()
    print(f"Successfully initialized {db_path} with tables and sample data.")

if __name__ == "__main__":
    init_db()
