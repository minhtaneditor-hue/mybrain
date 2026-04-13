import sqlite3
import os
from datetime import datetime

def generate_content(phase=None, day=None):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(current_dir, '..', 'database', 'brain.db')
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Lấy Brand Voice để tham chiếu
    cursor.execute("SELECT content FROM knowledge WHERE title = 'Brand Voice'")
    brand_voice = cursor.fetchone()
    brand_voice = brand_voice[0] if brand_voice else "Minimalist, Authentic, Expert."
    
    # Lấy Wedding Insights
    cursor.execute("SELECT title, content FROM knowledge WHERE title LIKE '%Wedding%'")
    insights = cursor.fetchall()
    
    print("\n--- CÔNG CỤ TẠO NỘI DUNG RA MẮT TIỆC CƯỚI (21 NGÀY) ---")
    print(f"Brand Voice active: {brand_voice[:50]}...")
    print(f"Insights found: {len(insights)}")
    
    print("\n[BẢN THẢO GỢI Ý CHO NGÀY CỦA BẠN]")
    print("-" * 50)
    
    # Logic tạo bản thảo (Drafting logic)
    # Đây là phiên bản đơn giản minh họa cách AI 'Brain' kết hợp dữ liệu
    if day:
        print(f"Đang tạo nội dung cho NGÀY {day}...")
        # Tìm kiếm kịch bản mẫu từ knowledge hoặc templates
        # (Trong thực tế AI sẽ xử lý LLM ở đây, ở cấp độ script chúng ta xuất cấu trúc)
        print("\n[KỊCH BẢN GỢI Ý]")
        print("1. Hook: Đánh vào một trong các Wedding Pain Points.")
        print("2. Body: Phân tích giải pháp theo Option bạn đã chọn.")
        print("3. CTA: Lời kêu gọi hành động dẫn về bộ Wedding Machine.")
    
    conn.close()

if __name__ == "__main__":
    # Chạy thử
    generate_content(day=1)
