#!/bin/bash

# Nhập tên người dùng cần kiểm tra mật khẩu
read -p "Nhập tên user: " USERNAME

# Kiểm tra nếu user tồn tại trên hệ thống
if id "$USERNAME" >/dev/null 2>&1; then
    echo "User '$USERNAME' tồn tại trên hệ thống."

    while true; do
        # Yêu cầu nhập mật khẩu của user
        read -s -p "Nhập mật khẩu của user: " PASSWORD
        echo

        # Kiểm tra mật khẩu bằng cách sử dụng `su` để đăng nhập tạm thời
        echo "$PASSWORD" | su -c "exit" "$USERNAME" >/dev/null 2>&1

        # Kiểm tra kết quả của lệnh su
        if [ $? -eq 0 ]; then
            echo "Mật khẩu đúng."
            echo "true"
            break
        else
            echo "Mật khẩu sai. Vui lòng thử lại."
            echo "false"
        fi
    done

else
    echo "User '$USERNAME' không tồn tại trên hệ thống."
fi
