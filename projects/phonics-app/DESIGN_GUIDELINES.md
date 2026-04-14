# HƯỚNG DẪN THIẾT KẾ (CALM DESIGN GUIDELINES)

Tài liệu này quy chuẩn hóa giao diện người dùng (UI) và trải nghiệm người dùng (UX) cho ứng dụng Phonics English.

---

## 1. HỆ THỐNG MÀU SẮC (COLOR PALETTE)
Tập trung vào các tông màu Pastel và Natural, tránh sự gắt gao (vibrant) gây kích ứng thị giác.

*   **Primary (Green):** `#A8E6CF` (Mint Green) - Màu của sự phát triển và bình yên. Dùng cho các nút bấm hành động chính.
*   **Secondary (Cream):** `#FDFFAB` (Pale Yellow) - Màu của sự ấm áp. Dùng cho nền các thẻ bài (cards).
*   **Background (Soft Gray/White):** `#F9F9F9` - Tạo không gian thoáng đãng (white space).
*   **Accent (Rose/Blue):** `#FFD3B6` hoặc `#D4A5A5` - Dùng cho các chi tiết nhỏ để phân loại nội dung.

---

## 2. KIỂU CHỮ (TYPOGRAPHY)
Sử dụng các font Sans-serif tròn trịa, dễ đọc cho trẻ nhỏ.

*   **Heading (Lettering):** *Comic Neue* hoặc *Patrick Hand* - Tạo cảm giác viết tay thân thiện.
*   **Body:** *Roboto* hoặc *Inter* - Đảm bảo tính rõ ràng cho phụ huynh.
*   **Chữ cái học:** Phải dùng font có nét chữ chuẩn (ví dụ: chữ 'a' không có móc trên đầu) để trẻ không bị nhầm lẫn khi tập viết.

---

## 3. NGUYÊN TẮC TƯƠNG TÁC (UX PRINCIPLES)

*   **Large Hit Targets:** Toàn bộ các icon và nút bấm phải có kích thước tối thiểu `64x64 dp` để phù hợp với ngón tay nhỏ và khả năng vận động tinh chưa hoàn thiện của trẻ.
*   **Immediate Feedback:** 
    *   Khi chạm vào chữ cái: Phát âm thanh ngay lập tức (Latency < 100ms).
    *   Khi kéo thả đúng: Hiệu ứng rung nhẹ (haptic) và âm thanh khen ngợi dịu dàng.
*   **No High-Pressure Loops:** Không có đồng hồ đếm ngược, không có bảng xếp hạng áp lực. Trẻ học theo nhịp độ riêng.

---

## 4. CẤU TRÚC MÀN HÌNH CHÍNH (KEY SCREENS)

1.  **Home (The Garden):** Hiển thị các chương học dưới dạng các "hạt mầm" hoặc "phòng học" yên tĩnh.
2.  **Lesson Space (The Sandbox):** Không gian trung tâm nơi trẻ tương tác với chữ cái và âm thanh.
3.  **Parent Oasis (Dashboard):** Khu vực dành riêng cho cha mẹ (cần mật khẩu hoặc phép tính đơn giản để vào). Hiển thị:
    *   Thời gian học trong ngày.
    *   Các âm bé đã thuộc.
    *   Nút cập nhật nội dung OTA.

---
*Thiết kế dựa trên nghiên cứu tâm lý học trẻ em - My Brain Project.*
