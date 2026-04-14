# SOP MASTER: AI CODING AGENT (10-DAY SYSTEM)

Tài liệu này tổng hợp toàn bộ quy trình xây dựng Website, AI Brain và Hệ thống Bán hàng tự động trong lộ trình **21 Ngày**. Đây là hướng dẫn tác chiến cho AI Agent để thực thi công việc theo triết lý "AI-First".

## 📅 LỘ TRÌNH 21 NGÀY (ROADMAP OVERVIEW)
- **Tuần 1: Nền tảng & Content** (Day 1 - 7): Setup, Landing Page, AI Brain, Traffic.
- **Tuần 2: Hệ thống & Chuyển đổi** (Day 8 - 14): AI Sales Agent, SePay, CRM, Optimization.
- **Tuần 3: Tự động hóa & Scaling** (Day 15 - 21): Advanced Automation, Scaling, Management.

---

## 💡 TƯ DUY CỐT LÕI (AI-FIRST)
1. **Ông chủ & Nhân viên**: Bạn là "Người kiểm duyệt", AI là "Người thực thi". Đừng tự làm, hãy ra lệnh rõ ràng và bắt AI sửa đến khi ưng ý.
2. **Context is King**: Agent chỉ giỏi khi có bối cảnh. File `README.md` chính là "não" của Workspace.
3. **Delegate, Don't Do**: 1 câu lệnh > 100 dòng code tự gõ.
4. **Data In, Data Out**: Rác vào = Rác ra. Dữ liệu tốt = Kết quả tốt.
5. **Iterate Fast**: Không cần hoàn hảo, cần chạy được trước. Sửa dần từng vòng.

---

## 🛠 MODULE 1: THIẾT LẬP MÔI TRƯỜNG & CẤU TRÚC (Day 1 & 7)

### 1. Công cụ bắt buộc
- Claude Desktop / VS Code.
- Antigravity AI Agent.
- SQLite Browser (để xem database).

### 2. Cấu trúc Workspace "Sạch"
Mỗi dự án phải là một thư mục riêng biệt. Cấu trúc chuẩn:
```
my-workspace/
├── README.md (Bối cảnh, mục tiêu, quy tắc ưu tiên)
├── tasks.md (Bảng theo dõi việc cần làm, deadline, trạng thái)
├── weekly-goals.md (3-5 mục tiêu tuần)
├── projects/ (Chi tiết từng dự án nhỏ)
├── meetings/ (Ghi chú họp)
└── archive/ (Nơi lưu trữ việc đã xong)
```

---

## 🎨 MODULE 2: NỘI DUNG & GIAO DIỆN (Day 2)

### 1. Copywriting & Context
Không tự nghĩ nội dung. Hãy ra lệnh cho AI đóng vai chuyên gia Marketing để viết:
- Tiêu đề (Headline), Vấn đề (Pain Points), Giải pháp, Lợi ích, CTA.

### 2. Visual Prompting (Sao chép thiết kế)
Dùng hình ảnh thay vì lời nói. 
- Chụp ảnh màn hình trang web mẫu bạn thích.
- Tải lên và yêu cầu AI: "Dựa trên phong cách, màu sắc và bố cục của ảnh này, hãy tạo landing page cho tôi."

---

## 🚀 MODULE 3: TRIỂN KHAI THỰC TẾ & TRAFFIC (Day 3 & 4)

### 1. Tên miền & Hosting
- Mua domain thật (ưu tiên .vn hoặc .com).
- Deploy lên Vercel, Netlify hoặc GitHub Pages (miễn phí) hoặc VPS cá nhân.

### 2. Kênh kéo Traffic
- Chọn 1 kênh duy nhất (Facebook/Zalo/TikTok).
- Dùng AI viết 3 bài đăng theo 3 góc độ khác nhau.
- CTA rõ ràng dẫn về link website.

---

## 🧠 MODULE 4: AI BRAIN & CÁ NHÂN HÓA (Day 5 & 6)

### 1. Bộ não SQLite (`brain.db`)
Tạo database SQLite với 3 bảng cốt lõi:
- `knowledge`: Lưu bài học, insight.
- `business`: Sản phẩm, khách hàng.
- `brand_voice`: **QUAN TRỌNG NHẤT**. Lưu tone, style, từ hay dùng/không dùng.

### 2. Brand Voice Integration
Dạy AI "giọng" của bạn bằng cách:
- Cung cấp ít nhất 2-3 bài viết thật của bạn.
- Bổ sung quy tắc viết (ngắn gọn, thẳng thắn, không dùng từ corporate).

---

## 🤖 MODULE 5: NHÂN VIÊN BÁN HÀNG AI (Day 9)

### 1. Kho dữ liệu nhân viên (`/data`)
Tạo các thư mục con trong dự án website:
- `/data/products`: Thông tin chi tiết sản phẩm & giá.
- `/data/faq`: Câu hỏi thường gặp.
- `/data/customers`: Feedback & câu chuyện thật.
- `/data/objections`: Cách xử lý khi khách từ chối.

### 2. Chatbot Script
Yêu cầu Agent đọc toàn bộ `/data` và `brain.db` để viết `sales_script.md`.
Gắn Chatbot vào website với các nút bấm tự động dựa trên kịch bản.

---

## 💰 MODULE 6: HỆ THỐNG CRM & THANH TOÁN (Day 10)

### 1. Tích hợp SePay
- Kết nối ngân hàng qua SePay để nhận tiền tự động qua QR.
- AI đọc tài liệu `docs.sepay.vn` để viết code callback/webhook.

### 2. Admin Panel & CRM
Tạo trang `/admin` (đơn giản, không cần backend phức tạp) để quản lý:
- **Sản phẩm**: Thêm/Xóa/Sửa.
- **Khách hàng**: Import từ waitlist.
- **Đơn hàng**: Tự động chuyển trạng thái từ `pending` sang `success` khi có tiền về.

---

## 📝 BẢNG THEO DÕI THÔNG MINH (`brain_score.md`)
Mỗi tối điền vào 4 cột:
1. Bài AI viết giống giọng tôi mấy điểm (1-10)?
2. Phản hồi khách hàng?
3. Đã thêm gì vào Brand Voice hôm nay?
4. Nhận xét ngắn.

---

## 📈 TẦM NHÌN TIẾP THEO (DAYS 11-21)

### [NGÀY 11] - ĐANG CẬP NHẬT...
*(Dán nội dung SOP Ngày 11 của bạn vào đây)*

### [NGÀY 12] - ĐANG CẬP NHẬT...
*(Dán nội dung SOP Ngày 12 của bạn vào đây)*

### [NGÀY 13] - ĐANG CẬP NHẬT...

### [NGÀY 14] - ĐANG CẬP NHẬT...

### [NGÀY 15-21] - GIAI ĐOẠN SCALING & TỰ ĐỘNG HÓA CAO CẤP
*(Sẽ được mở khóa hàng ngày)*

---

## ⚡ MASTER AGENT PROMPT
*Bạn có thể copy đoạn này để bắt đầu một dự án mới với Agent:*

> "Tôi muốn bắt đầu một dự án mới theo SOP MASTER 10-DAY. 
> 1. Hãy đọc file `docs/sop_master_coding_agent.md` để hiểu quy trình.
> 2. Thiết lập cấu trúc thư mục chuẩn (Day 7).
> 3. Chúng ta sẽ bắt đầu từ Phase 1: Context & Copywriting.
> Hãy hướng dẫn tôi từng bước một, mỗi lần chỉ đưa ra 1 nhiệm vụ và chờ tôi xác nhận trước khi tiếp tục."

---
*Ngày cập nhật: 2026-04-14*
*Phiên bản: 1.0 (SOP synthesis)*
