from selenium import webdriver
import time

# Khởi tạo trình duyệt
driver = webdriver.Chrome()

# Tạo một dictionary chứa session ID
session_id = {'name': 'sessionid', 'value': 'cad813be4f5d43746dc04030a2d8701b'}

# Mở trang web cần đăng nhập
driver.get("https://www.tiktok.com/")

# Thêm session ID vào trình duyệt
driver.add_cookie(session_id)

# Tải lại trang để áp dụng cookie
driver.refresh()

# Kiểm tra xem đã đăng nhập thành công hay không
# (Bạn cần cung cấp cách xác định đăng nhập thành công dựa trên trang web)
# Ví dụ: logged_in = driver.find_element_by_xpath("//some_xpath_expression").text
# print(logged_in)

time.sleep(50)

# Đóng trình duyệt
driver.quit()
