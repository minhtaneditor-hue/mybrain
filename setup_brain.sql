-- Setup script for Second Brain (brain.db)
-- Includes: Knowledge (Hormozi & Video), Business (21 Days), and Brand Voice (Tấn)

-- 1. Knowledge Table
CREATE TABLE IF NOT EXISTS knowledge (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    content TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO knowledge (title, content) VALUES 
('Hormozi $100M Offers', 'Tạo ra những lời đề nghị "Grand Slam" mà khách hàng cảm thấy ngu ngốc khi từ chối. Tập trung vào: Kết quả mong đợi, Xác suất thành công cao, Thời gian trễ thấp, và Nỗ lực/Sự hy sinh thấp.'),
('Hormozi $100M Leads', 'Lead là những người bạn có thể liên lạc. Có 4 cách tạo leads: Reach out (1-1), Post content (1-many), Ads (Paid 1-many), Affiliates (Many-many).'),
('Quy luật 80/20 trong Nội dung', '20% nội dung (Video Assets) tạo ra 80% chuyển đổi. Đừng làm nội dung rác, hãy làm tài sản.'),
('The Solo Expert Catalyst', 'Vai trò của người cố vấn là giúp các solo expert thoát khỏi "vùng hỗn loạn" (Chaos) bằng cách quy trình hóa kiến thức thành hệ thống video.');

-- 2. Business Table
CREATE TABLE IF NOT EXISTS business (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    content TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO business (title, content) VALUES 
('21 Ngày Biến Video Thành Tài Sản', 'Chương trình huấn luyện giúp chuyên gia xây dựng hệ thống Video Advisor, tự động hóa quy trình bán hàng và xây dựng thương hiệu cá nhân bền vững.'),
('Expert Branding Starter Kit', 'Bộ công cụ nền tảng để định vị ngách (Niche) và xác định Client Avatar cho các Solopreneur.'),
('Dịch vụ Video Advisor', 'Tư vấn chiến lược nội dung và hỗ trợ kỹ thuật dựng phim chuyên nghiệp cho Coach/Mentor.');

-- 3. Brand Voice Table
CREATE TABLE IF NOT EXISTS brand_voice (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    content TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO brand_voice (title, content) VALUES 
('Tone & Xưng hô', 'Xưng "mình" - gọi "bạn". Tone giọng Coach đi trước, đồng cảm, peer-to-peer. Không dạy đời, chỉ chia sẻ trải nghiệm.'),
('Quy tắc viết (Rhythm)', 'Sử dụng câu dài, liền mạch, có chiều sâu. Ngắt dòng có chủ đích để dẫn dắt nhịp đọc. Tuân thủ: Hook -> Mở bài -> Thân bài -> Kết bài.'),
('Keywords / Concept', 'Video là Tài sản (Video as an Asset), Solo Expert, Hệ thống bán hàng tự động, Lộ trình tác chiến, Đòn bẩy, Vũ khí, Dòng tiền.'),
('Audience Persona', 'The Resourceful Solopreneur (25-35 tuổi). Đang có nhiều kiến thức nhưng "hấp hối" vì không có hệ thống, phải đổi thời gian lấy tiền.'),
('Vibe mục tiêu', 'Trực diện, thực tế, thấu hiểu những cảm xúc "xấu" (burnout, mông lung) để xây dựng lòng tin tuyệt đối.');
