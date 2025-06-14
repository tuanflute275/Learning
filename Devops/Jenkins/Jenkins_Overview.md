
# TỔNG QUAN VỀ JENKINS

**Jenkins** là một công cụ mã nguồn mở được sử dụng để tự động hóa các quy trình phát triển phần mềm, đặc biệt là các tác vụ liên quan đến tích hợp liên tục (CI) và triển khai liên tục (CD). Jenkins giúp phát triển và triển khai phần mềm nhanh chóng, chính xác và dễ dàng bằng cách tự động hóa các tác vụ xây dựng, kiểm thử và triển khai.

Jenkins được sử dụng rộng rãi trong các công ty phát triển phần mềm để tối ưu hóa quy trình phát triển và giảm thiểu các lỗi do quá trình thủ công.

---

# CÁC KHÁI NIỆM CƠ BẢN VỀ JENKINS

## 1. **Continuous Integration (CI)**

- **Continuous Integration (CI)** là quá trình tự động hóa việc tích hợp mã nguồn từ nhiều lập trình viên vào một kho mã nguồn chung. Jenkins giúp tích hợp mã nguồn vào repository một cách thường xuyên (ví dụ: mỗi khi có sự thay đổi trong mã nguồn) và kiểm tra tự động các lỗi trong mã.

## 2. **Continuous Deployment (CD)**

- **Continuous Deployment (CD)** là quá trình tự động hóa việc triển khai phần mềm vào môi trường sản xuất. Jenkins hỗ trợ việc triển khai phần mềm lên môi trường máy chủ hoặc cloud mỗi khi có phiên bản mới được kiểm tra thành công.

## 3. **Pipeline**

- **Pipeline** trong Jenkins là một chuỗi các tác vụ được tự động thực hiện trong một quy trình CI/CD. Pipeline giúp kiểm soát việc xây dựng, kiểm thử, và triển khai phần mềm một cách tự động.

## 4. **Job**

- **Job** là một tác vụ đơn lẻ trong Jenkins, ví dụ như xây dựng (build) mã nguồn, chạy kiểm thử, triển khai ứng dụng, v.v. Một job có thể được cấu hình để thực hiện một số lệnh hoặc chương trình tự động.

## 5. **Plugin**

- **Plugin** là các phần mở rộng cho Jenkins để cung cấp các chức năng bổ sung. Jenkins có rất nhiều plugin hỗ trợ các công cụ và công nghệ khác nhau như Git, Maven, Docker, AWS, v.v.

---

# CÁC CÂU LỆNH THƯỜNG DÙNG TRONG JENKINS

## 1. **Cài đặt Jenkins**

Trên **Ubuntu**:
```bash
sudo apt update
sudo apt install openjdk-11-jdk
wget -q -O - https://pkg.jenkins.io/debian/jenkins.io.key | sudo apt-key add -
sudo sh -c 'echo deb http://pkg.jenkins.io/debian/ / > /etc/apt/sources.list.d/jenkins.list'
sudo apt update
sudo apt install jenkins
```

Trên **Windows**:
Tải và cài đặt Jenkins từ trang chính thức: [Jenkins Official](https://www.jenkins.io/download/).

## 2. **Khởi động Jenkins**

Trên **Ubuntu**:
```bash
sudo systemctl start jenkins
```

Trên **Windows**:
Dịch vụ Jenkins sẽ tự động bắt đầu sau khi cài đặt.

## 3. **Truy cập Jenkins**

Sau khi cài đặt và khởi động Jenkins, bạn có thể truy cập Jenkins qua trình duyệt tại địa chỉ:

```
http://localhost:8080
```

## 4. **Cấu hình Jenkins**

Khi lần đầu tiên truy cập Jenkins, bạn sẽ cần phải cung cấp một mã khóa (unlock key) được tìm thấy trong tệp `/var/lib/jenkins/secrets/initialAdminPassword` trên hệ thống Linux hoặc tại `C:\Program Files (x86)\Jenkins\secrets\initialAdminPassword` trên Windows.

## 5. **Cài đặt Plugin**

- Để cài đặt các plugin trong Jenkins, vào **Manage Jenkins** > **Manage Plugins**. Tại đây bạn có thể tìm kiếm và cài đặt các plugin cần thiết.

## 6. **Tạo Job mới**

Để tạo một job trong Jenkins, bạn có thể vào trang chủ Jenkins, chọn **New Item**, đặt tên cho job, sau đó chọn loại job mà bạn muốn tạo (ví dụ: Freestyle project, Pipeline).

## 7. **Chạy Job**

Sau khi tạo job, bạn có thể chạy job bằng cách nhấn vào job và chọn **Build Now**.

## 8. **Cấu hình Pipeline**

Pipeline trong Jenkins có thể được cấu hình thông qua **Jenkinsfile**, đây là một tập tin cấu hình được lưu trong mã nguồn để định nghĩa quy trình xây dựng và triển khai. Một ví dụ cơ bản của Jenkinsfile:

```groovy
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building...'
            }
        }
        stage('Test') {
            steps {
                echo 'Running tests...'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
    }
}
```

## 9. **Quản lý Dịch vụ Jenkins**

- **Khởi động lại Jenkins**:
```bash
sudo systemctl restart jenkins
```

- **Dừng Jenkins**:
```bash
sudo systemctl stop jenkins
```

---

# LỢI ÍCH CỦA JENKINS

## 1. **Tự động hóa quy trình phát triển phần mềm**

Jenkins giúp tự động hóa toàn bộ quy trình phát triển phần mềm, từ việc xây dựng mã nguồn, kiểm thử đến triển khai ứng dụng. Điều này giúp giảm thiểu lỗi và tăng tốc quá trình phát triển.

## 2. **Hỗ trợ nhiều công cụ và công nghệ**

Jenkins hỗ trợ tích hợp với rất nhiều công cụ phát triển như Git, Maven, Docker, Kubernetes, AWS, và nhiều hơn nữa thông qua các plugin.

## 3. **Khả năng mở rộng linh hoạt**

Jenkins có thể mở rộng và tùy chỉnh để phù hợp với các yêu cầu phát triển của tổ chức. Bạn có thể thêm các node (máy chủ Jenkins slave) để tăng cường khả năng xử lý và phân phối các job.

## 4. **Dễ dàng cài đặt và cấu hình**

Jenkins dễ dàng cài đặt và có giao diện người dùng trực quan. Nó cũng cung cấp một API mạnh mẽ để tích hợp với các công cụ khác.

## 5. **Hỗ trợ CI/CD**

Jenkins là công cụ phổ biến nhất cho quy trình **Continuous Integration (CI)** và **Continuous Deployment (CD)**, giúp phần mềm được kiểm thử và triển khai một cách tự động và liên tục.

---

# ỨNG DỤNG CỦA JENKINS

- **Tích hợp liên tục (CI):** Jenkins được sử dụng rộng rãi trong việc kiểm tra mã nguồn và tích hợp các thay đổi vào repository chính một cách liên tục.
- **Triển khai liên tục (CD):** Jenkins giúp tự động triển khai các bản cập nhật lên môi trường sản xuất hoặc môi trường thử nghiệm.
- **Tự động hóa các tác vụ:** Jenkins có thể được sử dụng để tự động hóa các tác vụ khác ngoài việc xây dựng và triển khai phần mềm, chẳng hạn như quét bảo mật hoặc sao lưu dữ liệu.
- **Phát triển ứng dụng microservices:** Jenkins hỗ trợ tích hợp với Docker và Kubernetes, giúp triển khai các ứng dụng microservices.

---
