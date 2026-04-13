import sqlite3
import os

def update_brain():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(current_dir, '..', 'database', 'brain.db')
    if not os.path.exists(os.path.dirname(db_path)):
        db_path = os.path.join(current_dir, 'brain.db')
        
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # 1. Cập nhật Brand Voice từ file docs/brand_voice.txt
    bv_file = os.path.join(current_dir, '..', 'docs', 'brand_voice.txt')
    if os.path.exists(bv_file):
        with open(bv_file, 'r', encoding='utf-8') as f:
            brand_voice_content = f.read()
        cursor.execute("DELETE FROM brand_voice")
        cursor.execute("INSERT INTO brand_voice (title, content) VALUES (?, ?)", 
                       ("Chi tiết Brand Voice", brand_voice_content))
        print(f"Đã cập nhật Brand Voice từ {os.path.basename(bv_file)}")

    # 2. Thêm bài viết mới từ docs/post.txt vào knowledge (nếu chưa có)
    post_file = os.path.join(current_dir, '..', 'docs', 'post.txt')
    if os.path.exists(post_file):
        with open(post_file, 'r', encoding='utf-8') as f:
            post_content = f.read()
        
        # Kiểm tra xem nội dung bài này đã tồn tại trong knowledge chưa
        cursor.execute("SELECT id FROM knowledge WHERE content = ?", (post_content,))
        if not cursor.fetchone():
            cursor.execute("INSERT INTO knowledge (title, content) VALUES (?, ?)", 
                           ("Bài viết mới - " + datetime.now().strftime("%d/%m/%Y"), post_content))
            print("Đã thêm bài viết mới vào Knowledge Base")

    conn.commit()
    conn.close()
    print("--- Hoàn tất cập nhật Brain ---")

if __name__ == "__main__":
    update_brain()
