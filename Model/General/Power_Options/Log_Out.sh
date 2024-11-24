#!/bin/bash

# Kiểm tra môi trường desktop
if [[ -z "$XDG_SESSION_ID" ]]; then
    echo "Không phát hiện phiên làm việc đồ họa. Đăng xuất không khả dụng."
    exit 1
fi

# Đăng xuất
echo "Đăng xuất người dùng..."
loginctl terminate-session "$XDG_SESSION_ID"
