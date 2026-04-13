import os
import subprocess
from datetime import datetime

def run_command(command, cwd=None):
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True, cwd=cwd)
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Lỗi: {e.stderr}")
        return False

def sync():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.join(current_dir, '..')
    
    print(f"--- Bắt đầu đồng bộ hằng ngày: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---")
    
    # 1. Git Pull
    print("1. Đang lấy dữ liệu mới từ GitHub...")
    run_command("git pull origin main", cwd=project_root)
    
    # 2. Cập nhật Brain từ tệp cục bộ
    print("\n2. Đang nạp kiến thức mới vào bộ não (SQLite)...")
    run_command("python3 scripts/update_brain.py", cwd=project_root)
    
    # 3. Git Push
    print("\n3. Đang lưu trữ và đẩy dữ liệu lên GitHub...")
    run_command("git add .", cwd=project_root)
    # Kiểm tra xem có gì thay đổi không để tránh lỗi empty commit
    status = subprocess.run("git status --porcelain", shell=True, capture_output=True, text=True, cwd=project_root).stdout
    if status:
        commit_msg = f"Daily Update: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        run_command(f'git commit -m "{commit_msg}"', cwd=project_root)
        run_command("git push origin main", cwd=project_root)
        print("--- Đã đồng bộ và lưu trữ thành công! ---")
    else:
        print("--- Không có thay đổi nào để cập nhật. ---")

if __name__ == "__main__":
    sync()
