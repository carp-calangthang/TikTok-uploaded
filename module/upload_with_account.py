import datetime
import webbrowser

def get_user_input():
    print("Nhập các giờ bạn muốn kiểm tra (nhập done để kết thúc):")
    hours = []
    while True:
        user_input = input("Nhập giờ và phút (hh:mm): ")
        if user_input.lower() == 'done':
            break
        try:
            user_time = datetime.datetime.strptime(user_input, "%H:%M")
            hours.append((user_time.hour, user_time.minute))
        except ValueError:
            print("Thời gian không hợp lệ. Vui lòng nhập lại.")
    return hours

def check_hours(user_hours):
    while True:
        current_time = datetime.datetime.now()
        current_hour = current_time.hour
        current_minute = current_time.minute
        for hour, minute in user_hours:
            if current_hour == hour and current_minute == minute:
                print(f"Bây giờ là {hour}:{minute}! Mở YouTube...")
                webbrowser.open("https://www.youtube.com")
                user_hours.remove((hour, minute))  # Đảm bảo chỉ mở một lần khi giờ trùng
        if not user_hours:
            print("Đã kiểm tra hết các giờ bạn nhập.")
            break

if __name__ == "__main__":
    user_hours = get_user_input()
    check_hours(user_hours)
    
    
