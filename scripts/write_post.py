import sqlite3
import os

def get_brain_context(product_name="30 Ngày Video Ngắn Masterclass"):
    # Xác định đường dẫn tương đối từ vị trí tệp script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Nếu script nằm trong /scripts, database sẽ ở ../database/brain.db
    # Nếu script nằm ở root (hiện tại), database sẽ ở ./brain.db
    # Chúng ta sẽ hỗ trợ cả hai trường hợp hoặc giả định cấu trúc mới
    db_path = os.path.join(current_dir, '..', 'database', 'brain.db')
    if not os.path.exists(db_path):
        db_path = os.path.join(current_dir, 'brain.db') # Trường hợp chưa di chuyển
        
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Get Brand Voice
    cursor.execute("SELECT content FROM brand_voice LIMIT 1")
    brand_voice = cursor.fetchone()[0]

    # Get Product Info
    cursor.execute("SELECT content FROM business WHERE title LIKE ?", (f'%{product_name}%',))
    product_info = cursor.fetchone()
    product_info = product_info[0] if product_info else "Thông tin sản phẩm đang được cập nhật..."

    # Get relevant Knowledge
    cursor.execute("SELECT content FROM knowledge LIMIT 2")
    knowledge = "\n".join([row[0] for row in cursor.fetchall()])

    conn.close()
    
    return {
        "brand_voice": brand_voice,
        "product_info": product_info,
        "knowledge": knowledge
    }

def write_dynamic_post(topic="30 Ngày Video Ngắn"):
    context = get_brain_context(topic)
    
    # Đây là nơi logic "Generative" sẽ diễn ra. 
    # Trong môi trường này, ta sẽ in ra Brief để AI Agent (Antigravity) có thể đọc và viết bài.
    
    print("--- CONTEXT BRIEF FOR AI ---")
    print(f"BRAND VOICE:\n{context['brand_voice']}")
    print(f"PRODUCT INFO:\n{context['product_info']}")
    print(f"KNOWLEDGE BASE:\n{context['knowledge']}")
    print("----------------------------")
    
    print(f"\n[Hệ thống] Đang chờ AI Agent xử lý và tinh chỉnh ngôn từ cho bài viết về: {topic}")

if __name__ == "__main__":
    write_dynamic_post()
