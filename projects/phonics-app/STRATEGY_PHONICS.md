# CHIẾN LƯỢC SƯ PHẠM: PHONICS ENGLISH APP (CALM DESIGN)

Tài liệu này hệ thống hóa toàn bộ lộ trình học thuật và triết lý đào tạo của ứng dụng, dựa trên các tài liệu nghiên cứu chuẩn Stanford và MIT.

---

## 1. TRIẾT LÝ ĐÀO TẠO (PEDAGOGY PHILOSOPHY)

*   **Calm Design (Thiết kế Bình lặng):** Giảm thiểu tối đa các tác nhân gây xao nhãng (màu sắc quá rực rỡ, âm thanh dồn dập). Tạo môi trường học tập tập trung, không gây nghiện.
*   **Micro-learning:** Mỗi phiên học chỉ kéo dài 5-10 phút để tối ưu hóa khả năng hấp thụ của trẻ 2-6 tuổi.
*   **British Accent (Accent Anh-Anh):** Tập trung vào phát âm chuẩn UK làm nền tảng.
*   **Multi-sensory:** Kết hợp Nghe (âm thanh chất lượng cao) - Nhìn (hình ảnh tối giản) - Chạm (tương tác trực quan).

---

## 2. LỘ TRÌNH HỌC THUẬT (CURRICULUM ROADMAP)

### GIAI ĐOẠN 1: NỀN TẢNG (BASIC PHONICS) - 26 CHÂN TỰ
*   **Mục tiêu:** Nhận diện ký tự và âm tương ứng (Phoneme-Grapheme Mapping).
*   **Nội dung:**
    *   Nhóm âm đơn: a, b, c, d... z.
    *   Cách phát âm chuẩn (Mouth focus): Video/Hình minh họa khẩu hình.
    *   Từ vựng ví dụ: a - apple, b - ball.

### GIAI ĐOẠN 2: GHÉP VẦN CƠ BẢN (BASIC BLENDING)
*   **Mục tiêu:** Hiểu quy tắc ghép 2-3 âm tiết.
*   **Nội dung:**
    *   Ghép 2 âm (VC Blending): 
        *   Nhóm 'a': at, am, an, ap.
        *   Nhóm 'e': ed, en, et.
        *   Nhóm 'i': id, ig, in, ip, it.
        *   Nhóm 'o': og, op, ot.
        *   Nhóm 'u': ug, un, up.
    *   Cấu trúc CVC (Consonant-Vowel-Consonant): c-a-t -> cat, d-o-g -> dog.
    *   Luyện tập: Drag & Drop các âm để tạo thành từ.

### GIAI ĐOẠN 3: PHONICS NÂNG CAO (CVC & DIGRAPHS)
*   **Mục tiêu:** Đọc và ghép hoàn chỉnh các từ 3 chữ cái (CVC) và làm chủ các âm phức hợp.
*   **Nội dung:**
    *   Cấu trúc CVC: Ghép Phụ âm + Nguyên âm + Phụ âm (c-a-t = cat).
    *   Các âm đôi (Digraphs): sh, ch, th, ph...
    *   Âm nguyên âm dài: ai, ee, oa, oo...
    *   Luyện tập: "Sound Sandbox" - Kéo thả các âm tiết để tạo thành từ hoàn chỉnh và nghe máy đọc.

### GIAI ĐOẠN 4: KỸ NĂNG ĐỌC & ĐÁNH GIÁ (SKILLS & ASSESSMENT)
*   **Mục tiêu:** Đọc từ khó (Tricky words) và thực hiện bài kiểm tra cuối chương.
*   **Nội dung:**
    *   Tricky words: the, he, she, was... (những từ không tuân theo quy tắc phonics thông thường).
    *   Bảng tin đánh giá dành cho phụ huynh (Progress Dashboard).

---

## 3. QUY TRÌNH RA MẮT TÍNH NĂNG (RELEASE FLOW)

Sử dụng cơ chế **OTA (Over-The-Air)** qua Firebase Remote Config:
1.  **Chương 1:** Launch mặc định trong App.
2.  **Chương 2-4:** Tải dữ liệu động sau khi trẻ hoàn thành chương trước.
3.  **Cập nhật:** Sửa lỗi phát âm hoặc hình ảnh ngay lập tức mà không cần qua App Store/Play Store (giảm ma sát vận hành).

---
*Dựa theo tài liệu "Nguồn kiến thức" - Minh Tấn Academy.*
