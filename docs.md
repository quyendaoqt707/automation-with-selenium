Selenium find element: https://selenium-python.readthedocs.io/locating-elements.html

Một số chú ý: 
 * Tuỳ theo kích thước màn hình mà các element sẽ render ra khác nhau ở ccs kích thuóc màn khác nhau -> phải query css ở màn hình lúc testcase chạy
 * Tìm 1 element luôn phải sủ dụng hàm đợi element đó clicable hoặc hiện diện
 * Có thể dùng xpath để tìm bất kì 1 đoạn text nào đó trên màn hình (dùng để assert)
 * Có thể dùng kết hợp với pyautogui để tự động hoá các thao tác ngoài trình duyệt (liên quan đến windows,..file,...)
