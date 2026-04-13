import sqlite3

def update_brain():
    conn = sqlite3.connect('/Volumes/Disk1/TAN /my-brain/brain.db')
    cursor = conn.cursor()

    # 1. Cập nhật Brand Voice chi tiết
    brand_voice_content = """
    === BRAND VOICE: LÊ MINH TẤN ===
    ● TƯ DUY: Video là tài sản (Asset). Mục tiêu là xây dựng Trust và chuyển đổi Sales tự động.
    ● ĐỊNH DẠNG: Minimalist, mỗi câu một dòng, khoảng trắng rộng.
    ● CẤU TRÚC: 
      1. Hook: Luôn bắt đầu bằng một con số nghịch lý hoặc một sự thật lật ngược vấn đề.
      2. Format: Mỗi câu một dòng.
      3. Ngôn ngữ: Peer-to-peer (Anh chị em/Bạn - Mình). Không dạy đời.
      4. Chân thực: Đưa yếu tố gia đình và trải nghiệm TV Editor thực tế.
    ● TỪ NGỮ CẤM DÙNG: Không dùng "anh em", dùng "anh chị em" hoặc "mọi người".
    """
    cursor.execute("DELETE FROM brand_voice")
    cursor.execute("INSERT INTO brand_voice (title, content) VALUES (?, ?)", 
                   ("Chi tiết Brand Voice", brand_voice_content))

    # 2. Thêm thông tin sản phẩm 30-Day Masterclass
    business_30day = """
    Tên: 30 Ngày Video Ngắn Masterclass.
    Mục tiêu: Hoàn thành 10 video trong 30 ngày để xây dựng thói quen.
    Chi phí: 300.000đ (Dạng tiền cọc hoàn lại).
    Cam kết: Hoàn 100% tiền cọc nếu làm đủ 10 video + 1 video feedback.
    Giá trị cốt lõi: Hỗ trợ 1-1 về kịch bản, quay, dựng và chữa bài trực tiếp.
    Đối tượng: Người sợ bắt đầu, người hay trì hoãn, Experts muốn xây dựng thương hiệu cá nhân qua Video.
    """
    cursor.execute("INSERT INTO business (title, content) VALUES (?, ?)", 
                   ("30 Ngày Video Ngắn Masterclass", business_30day))

    # 3. Thêm Framework 3 tầng (Viral-Skill-Income) vào knowledge
    framework_content = """
    Framework 3 tầng (Viral-Skill-Income):
    - Tầng Viral (Friction): Sản phẩm mồi (vd: 7 ngày 199k) để "mua" niềm tin và giảm ma sát kỹ thuật.
    - Tầng Skill (How-to): Dạy kỹ năng cụ thể, giúp khách hàng có kết quả ngay (Quick Win).
    - Tầng Income (High-end): Xây dựng hệ thống Video Sales tự động 24/7 để tạo thu nhập bền vững.
    """
    cursor.execute("INSERT INTO knowledge (title, content) VALUES (?, ?)", 
                   ("Framework 3 tầng", framework_content))

    conn.commit()
    conn.close()
    print("Đã cập nhật Brand Voice và Sản phẩm 30-Day vào brain.db!")

if __name__ == "__main__":
    update_brain()
