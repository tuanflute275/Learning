
# TỔNG QUAN VỀ DOCKER

**Docker** là một nền tảng mã nguồn mở giúp phát triển, vận hành và chạy các ứng dụng trong các **container** (containerized applications). Docker giúp đóng gói các ứng dụng và các phần mềm cần thiết vào một môi trường độc lập, giúp ứng dụng chạy nhất quán ở mọi môi trường. Các container của Docker nhẹ, khởi động nhanh và dễ dàng triển khai trên bất kỳ nền tảng nào.

Docker được sử dụng phổ biến trong các dự án phát triển phần mềm, CI/CD, và các môi trường đám mây.

---

# CÁC KHÁI NIỆM CƠ BẢN VỀ DOCKER

## 1. **Container**

- **Container** là một môi trường độc lập được tạo ra để chạy một ứng dụng và các phụ thuộc của nó. Container chia sẻ hệ điều hành của máy chủ nhưng mỗi container có không gian riêng để chạy ứng dụng, giúp giảm thiểu sự phụ thuộc và tăng khả năng tái sử dụng phần mềm.

## 2. **Image**

- **Image** là một mẫu (template) để tạo các container. Một image là một tập hợp các file và cấu hình cần thiết để chạy một ứng dụng. Image có thể được tạo ra từ Dockerfile hoặc tải từ kho Docker Hub.

## 3. **Dockerfile**

- **Dockerfile** là một tệp văn bản chứa các hướng dẫn (instructions) mà Docker sử dụng để xây dựng một image. Dockerfile xác định cách thức cài đặt các phần mềm và cấu hình hệ thống cho ứng dụng bên trong container.

## 4. **Docker Hub**

- **Docker Hub** là một kho lưu trữ trực tuyến cho các Docker images. Bạn có thể tải về các image có sẵn từ Docker Hub hoặc chia sẻ các image của mình với cộng đồng.

## 5. **Docker Engine**

- **Docker Engine** là một phần mềm máy chủ để chạy và quản lý Docker containers. Docker Engine bao gồm một daemon (Docker Daemon), client, và API.

## 6. **Volume**

- **Volume** là một cách để lưu trữ dữ liệu ngoài container, giúp bảo vệ dữ liệu khi container bị xóa hoặc thay đổi. Volume cho phép chia sẻ dữ liệu giữa các container.

---

# CÁC CÂU LỆNH THƯỜNG DÙNG TRONG DOCKER

## 1. **Cài đặt Docker**

Trên **Ubuntu**:
```bash
sudo apt-get update
sudo apt-get install docker.io
```

Trên **Windows**:
Tải và cài đặt Docker Desktop từ trang chính thức: [Docker Official](https://www.docker.com/products/docker-desktop).

## 2. **Kiểm tra phiên bản Docker**

```bash
docker --version
```

## 3. **Chạy Docker Daemon**

Docker daemon (dockerd) phải chạy trên hệ thống để Docker hoạt động.

```bash
sudo systemctl start docker
```

## 4. **Kiểm tra trạng thái Docker**

```bash
sudo systemctl status docker
```

## 5. **Chạy Docker Container**

```bash
docker run -d --name my_container nginx
```

Trong ví dụ trên, Docker sẽ tải image `nginx` từ Docker Hub và chạy nó trong một container với tên `my_container`.

## 6. **Liệt kê các container đang chạy**

```bash
docker ps
```

## 7. **Liệt kê tất cả các container (bao gồm cả container đã dừng)**

```bash
docker ps -a
```

## 8. **Dừng một container**

```bash
docker stop my_container
```

## 9. **Khởi động lại một container**

```bash
docker start my_container
```

## 10. **Xóa một container**

```bash
docker rm my_container
```

## 11. **Tạo Docker Image từ Dockerfile**

```bash
docker build -t my_image .
```

## 12. **Liệt kê các images Docker**

```bash
docker images
```

## 13. **Xóa một Docker Image**

```bash
docker rmi my_image
```

## 14. **Tải một Docker Image từ Docker Hub**

```bash
docker pull ubuntu
```

## 15. **Tạo và chạy container từ một image**

```bash
docker run -it ubuntu bash
```

## 16. **Gắn kết một volume vào container**

```bash
docker run -d -v /host/path:/container/path --name my_container my_image
```

## 17. **Xem nhật ký của container**

```bash
docker logs my_container
```

## 18. **Chạy một lệnh trong container**

```bash
docker exec -it my_container bash
```

---

# LỢI ÍCH CỦA DOCKER

## 1. **Độc lập về môi trường**

Docker giúp bạn đóng gói ứng dụng và tất cả các phụ thuộc vào trong container, giúp ứng dụng chạy nhất quán ở bất kỳ môi trường nào, từ máy tính cá nhân, máy chủ, đến môi trường đám mây.

## 2. **Khởi động nhanh và tiết kiệm tài nguyên**

Các container trong Docker khởi động nhanh chóng và tiêu thụ ít tài nguyên so với các máy ảo truyền thống. Điều này giúp tiết kiệm thời gian và tài nguyên hệ thống khi triển khai các ứng dụng.

## 3. **Tái sử dụng và chia sẻ phần mềm**

Docker cho phép tái sử dụng các image có sẵn từ Docker Hub hoặc tự tạo và chia sẻ các image của mình, giúp tăng tốc quá trình phát triển và triển khai ứng dụng.

## 4. **Khả năng mở rộng**

Docker giúp bạn dễ dàng mở rộng ứng dụng thông qua các container. Việc triển khai các container trên nhiều máy chủ giúp đảm bảo tính khả dụng và hiệu suất cao cho ứng dụng.

## 5. **Quản lý và tự động hóa**

Docker tích hợp tốt với các công cụ CI/CD như Jenkins, giúp tự động hóa quá trình xây dựng, kiểm thử và triển khai ứng dụng.

---

# ỨNG DỤNG CỦA DOCKER

- **Phát triển và thử nghiệm phần mềm:** Docker giúp các lập trình viên phát triển ứng dụng và thử nghiệm trong môi trường đồng nhất, tránh được vấn đề "works on my machine".
- **Triển khai ứng dụng:** Docker giúp triển khai ứng dụng một cách dễ dàng và nhanh chóng trên môi trường máy chủ hoặc đám mây.
- **Ứng dụng microservices:** Docker là một công cụ lý tưởng để triển khai kiến trúc microservices, nơi mỗi service chạy trong một container độc lập.
- **CI/CD (Continuous Integration/Continuous Deployment):** Docker tích hợp tốt với các công cụ CI/CD, giúp tự động hóa quá trình kiểm thử và triển khai phần mềm.
- **Hệ thống phân tán:** Docker có thể được sử dụng trong các hệ thống phân tán, nơi nhiều container làm việc cùng nhau để xử lý yêu cầu.

---
