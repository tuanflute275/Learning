
# TỔNG QUAN VỀ LINUX

**Linux** là một hệ điều hành mã nguồn mở được phát triển bởi **Linus Torvalds** vào năm 1991. Linux dựa trên kernel (nhân hệ điều hành) Linux và là một phần của hệ thống phần mềm mã nguồn mở. Các hệ điều hành Linux được sử dụng rộng rãi trong máy chủ, máy tính để bàn, và các thiết bị nhúng do tính linh hoạt, bảo mật và ổn định cao.

Linux cũng có một cộng đồng lớn và rất nhiều bản phân phối (distribution) khác nhau, bao gồm Ubuntu, CentOS, Debian, Fedora, và nhiều hơn nữa.

---

# CÁC KHÁI NIỆM CƠ BẢN VỀ LINUX

## 1. **Kernel**

- **Kernel** là phần lõi của hệ điều hành, chịu trách nhiệm quản lý phần cứng của máy tính và cung cấp các dịch vụ cho các phần mềm chạy trên hệ thống. Kernel Linux là mã nguồn mở và được phát triển cộng đồng.

## 2. **Shell**

- **Shell** là giao diện dòng lệnh giúp người dùng tương tác với hệ điều hành. Trong Linux, **Bash** là shell mặc định được sử dụng. Shell cho phép bạn thực thi các lệnh để quản lý hệ thống.

## 3. **File System**

- Linux sử dụng một hệ thống tệp dạng cây (tree structure), trong đó tất cả các tệp đều bắt đầu từ thư mục gốc (root directory `/`). Các thư mục quan trọng bao gồm:
  - `/bin`: Chứa các tệp thực thi hệ thống.
  - `/home`: Chứa thư mục người dùng.
  - `/etc`: Chứa các tệp cấu hình hệ thống.
  - `/var`: Chứa các tệp dữ liệu thay đổi thường xuyên (log, cache).
  - `/tmp`: Chứa các tệp tạm thời.

## 4. **Permissions (Quyền truy cập)**

- Linux là một hệ điều hành đa người dùng và dựa vào hệ thống quyền truy cập (file permissions) để bảo mật. Các quyền truy cập cơ bản bao gồm:
  - **r**: Đọc (read).
  - **w**: Ghi (write).
  - **x**: Thực thi (execute).

Mỗi tệp hoặc thư mục có ba nhóm quyền: **owner (chủ sở hữu)**, **group (nhóm)**, và **others (khác)**.

## 5. **Processes**

- **Process** là một chương trình đang chạy. Linux có thể chạy nhiều process đồng thời, và mỗi process được gán một ID (PID). Bạn có thể kiểm tra các process đang chạy bằng lệnh `ps` hoặc `top`.

## 6. **Package Management**

- Linux sử dụng các công cụ quản lý gói để cài đặt, cập nhật, và xóa phần mềm. Các công cụ phổ biến bao gồm:
  - **APT** (Debian, Ubuntu): `apt-get`, `apt-cache`.
  - **YUM** (CentOS, Fedora): `yum install`, `yum update`.
  - **DNF** (Fedora, RHEL 8+): `dnf install`, `dnf update`.

---

# CÁC CÂU LỆNH THƯỜNG DÙNG TRONG LINUX

## 1. **Cập nhật hệ thống**

Trên **Ubuntu/Debian**:
```bash
sudo apt update
sudo apt upgrade
```

Trên **CentOS/RHEL**:
```bash
sudo yum update
```

## 2. **Quản lý tệp**

- **Liệt kê tệp trong thư mục**:
```bash
ls
```

- **Chuyển đến thư mục**:
```bash
cd /path/to/directory
```

- **Tạo một thư mục mới**:
```bash
mkdir new_directory
```

- **Xóa một tệp**:
```bash
rm file_name
```

- **Xóa một thư mục và tất cả nội dung bên trong**:
```bash
rm -r directory_name
```

## 3. **Quản lý quyền truy cập**

- **Thay đổi quyền truy cập của tệp**:
```bash
chmod 755 file_name
```

- **Thay đổi chủ sở hữu tệp**:
```bash
chown user:group file_name
```

## 4. **Quản lý process**

- **Xem các process đang chạy**:
```bash
ps aux
```

- **Kiểm tra các process theo thời gian thực**:
```bash
top
```

- **Dừng một process**:
```bash
kill PID
```

- **Tìm kiếm một process**:
```bash
ps aux | grep process_name
```

## 5. **Tìm kiếm tệp**

- **Tìm kiếm tệp theo tên**:
```bash
find /path/to/search -name "file_name"
```

- **Tìm kiếm nội dung trong tệp**:
```bash
grep "search_term" file_name
```

## 6. **Cài đặt phần mềm**

- **Cài đặt phần mềm trên Ubuntu/Debian**:
```bash
sudo apt install package_name
```

- **Cài đặt phần mềm trên CentOS/RHEL**:
```bash
sudo yum install package_name
```

## 7. **Sử dụng `sudo` để thực thi lệnh với quyền root**

```bash
sudo command
```

## 8. **Kiểm tra dung lượng đĩa**

```bash
df -h
```

## 9. **Kiểm tra bộ nhớ sử dụng**

```bash
free -h
```

## 10. **Tạo và xóa user**

- **Tạo một user mới**:
```bash
sudo adduser username
```

- **Xóa một user**:
```bash
sudo deluser username
```

## 11. **Quản lý dịch vụ**

- **Khởi động dịch vụ**:
```bash
sudo systemctl start service_name
```

- **Dừng dịch vụ**:
```bash
sudo systemctl stop service_name
```

- **Khởi động lại dịch vụ**:
```bash
sudo systemctl restart service_name
```

- **Kiểm tra trạng thái dịch vụ**:
```bash
sudo systemctl status service_name
```

---

# LỢI ÍCH CỦA LINUX

## 1. **Mã nguồn mở và miễn phí**

Linux là hệ điều hành mã nguồn mở, có thể được sử dụng miễn phí và tùy chỉnh theo nhu cầu của người dùng.

## 2. **Bảo mật cao**

Linux có cơ chế bảo mật mạnh mẽ và hệ thống quyền truy cập chặt chẽ, giúp bảo vệ dữ liệu và hệ thống khỏi các mối đe dọa.

## 3. **Ổn định và đáng tin cậy**

Linux rất ổn định và có thể hoạt động liên tục mà không gặp phải các sự cố về hiệu suất, điều này khiến nó trở thành lựa chọn lý tưởng cho các máy chủ.

## 4. **Tính linh hoạt**

Linux có thể chạy trên nhiều loại phần cứng khác nhau, từ máy tính để bàn đến máy chủ và thiết bị nhúng. Các bản phân phối Linux cũng rất linh hoạt, có thể được tối ưu hóa cho từng nhu cầu cụ thể.

## 5. **Cộng đồng hỗ trợ mạnh mẽ**

Linux có một cộng đồng lớn và năng động, giúp người dùng dễ dàng tìm kiếm sự trợ giúp và tài liệu hỗ trợ.

---

# ỨNG DỤNG CỦA LINUX

- **Máy chủ web:** Linux là hệ điều hành phổ biến nhất cho các máy chủ web, với Apache, Nginx và các phần mềm máy chủ web khác chạy trên nền tảng Linux.
- **Khoa học dữ liệu và lập trình:** Linux cung cấp các công cụ mạnh mẽ cho lập trình và khoa học dữ liệu, bao gồm Python, R, và các công cụ lập trình khác.
- **Máy chủ cơ sở dữ liệu:** Các hệ quản trị cơ sở dữ liệu như MySQL, PostgreSQL và MongoDB thường chạy trên Linux.
- **Hệ thống nhúng và IoT:** Linux rất phù hợp cho các hệ thống nhúng, vì nó nhẹ và dễ tùy chỉnh.

---
