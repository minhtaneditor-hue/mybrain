import sqlite3
import os
from datetime import datetime

def ingest_knowledge():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(current_dir, '..', 'database', 'brain.db')
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    knowledge_items = [
        ("Wedding Pain Points", "Hungry guests (slow service), lack of privacy, physical friction (parking/restrooms), hidden costs."),
        ("Wedding Trends 2024-2025", "Gen Z/Alpha authenticity over glamour, shift to Micro-weddings, environmental impact (eco-friendly decor/menu)."),
        ("Wedding Marketing Framework (Viral)", "Top of funnel: BTS videos, transparency in 'tasting' sessions, authentic 'Eat with the groom' content."),
        ("Wedding Marketing Framework (Skill)", "Middle of funnel: 21-day wedding planning checklists, budget calculation tools to empower the couple."),
        ("Wedding Marketing Framework (Income)", "Bottom of funnel: Video sales stories, success cases of smooth weddings, automated follow-up systems.")
    ]
    
    count = 0
    for title, content in knowledge_items:
        # Avoid duplication
        cursor.execute("SELECT id FROM knowledge WHERE title = ?", (title,))
        if not cursor.fetchone():
            cursor.execute("INSERT INTO knowledge (title, content) VALUES (?, ?)", (title, content))
            count += 1
            
    conn.commit()
    conn.close()
    print(f"--- Đã nạp {count} kiến thức mới về Marketing Tiệc Cưới vào bộ não! ---")

if __name__ == "__main__":
    ingest_knowledge()
