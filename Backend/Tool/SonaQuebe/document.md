# Hướng dẫn sử dụng SonarQube

SonarQube là một công cụ phân tích mã nguồn tự động giúp phát hiện các vấn đề về chất lượng mã, bảo mật, và khả năng bảo trì. Bài viết này cung cấp hướng dẫn chi tiết về cách sử dụng SonarQube, lưu ý khi sử dụng, cùng một số kỹ năng và kinh nghiệm để tận dụng tối đa công cụ này.

## 1. Cài đặt và cấu hình SonarQube

### 1.1. Cài đặt SonarQube

#### Trên Windows:

1. **Tải SonarQube** từ [SonarQube Downloads](https://www.sonarqube.org/downloads/).
2. **Giải nén** tệp tải về vào thư mục mà bạn muốn cài đặt SonarQube.
3. **Cài đặt Java**: SonarQube yêu cầu **JDK** (Java Development Kit) để chạy. Cài đặt **JDK** và đảm bảo biến môi trường `JAVA_HOME` được thiết lập đúng.
   từ [Oracle JDK Downloads](https://www.oracle.com/java/technologies/javase/jdk17-archive-downloads.html).
4. **Khởi động SonarQube**:

   - Mở **Command Prompt** và di chuyển đến thư mục `bin\windows-x86-64` trong thư mục cài đặt SonarQube.
   - Chạy lệnh:
     ```sh
     StartSonar.bat
     ```
   - Sau khi SonarQube khởi động, truy cập vào giao diện web của SonarQube tại [http://localhost:9000](http://localhost:9000).

   > **Tạo service chạy ngầm cho SonarQube**:

   - Tại thư mục `bin\windows-x86-64`, chạy lần lượt:
     - `StartSonar.bat install`
     - Mở `services.msc`
     - Tìm đến service của SonarQube và khởi động (start).

### 1.2. Cài đặt SonarScanner

SonarScanner là công cụ dùng để phân tích mã nguồn và gửi kết quả đến SonarQube.

1. **Tải SonarScanner** từ [SonarScanner Downloads](https://docs.sonarqube.org/latest/analysis/scan/sonarscanner/).
2. **Cài đặt SonarScanner** và thiết lập biến môi trường `SONAR_SCANNER_HOME`.

### 1.3. Cấu hình dự án trong SonarQube

1. **Tạo một project mới trong SonarQube**:
   - Từ giao diện SonarQube, chọn **Create Project** ở góc phải trên cùng, chọn **Local project**.
   - Điền thông tin và nhấn **Next**.
   - Chọn **Use the global settings** (Chọn đường cơ sở cho mã mới cho dự án này -> Sử dụng cài đặt toàn cầu).
   - Tiếp tục với các bước sau đó và chọn **Generate a project token**.
   - Chọn .NET -> **.NET Core** để tiếp tục.

## 2. Chạy các câu lệnh để quét code

> Xem thông tin tại nơi có tiêu đề: Install the SonarScanner .NET Core Global Tool

## 1. Cài đặt SonarScanner .NET Core Global Tool

Trước khi bắt đầu quét mã, bạn cần cài đặt **SonarScanner .NET Core Global Tool**. Để làm điều này, hãy chạy lệnh sau trong terminal hoặc Command Prompt:

```bash
dotnet tool install --global dotnet-sonarscanner
```

Truy cập vào dự án .NET hiện tại `cd path/to/your/project`

Bắt đầu quét mã nguồn

```bash
dotnet sonarscanner begin /k:"BE-khodulieumo-API" /d:sonar.host.url="http://localhost:9000"  /d:sonar.token="sqp_c621dad289dc430246ac352b1f42ac56210acdd6"
```

Build mã nguồn

```bash
dotnet build
```

Kết thúc quét mã

```bash
dotnet sonarscanner end /d:sonar.token="sqp_c621dad289dc430246ac352b1f42ac56210acdd6"
```

# Các mức độ bảo mật trong SonarQube

## A (Excellent)

**Ý nghĩa**: Đây là mức độ tốt nhất, cho thấy mã nguồn của bạn không có bất kỳ vấn đề bảo mật nào, hoặc tất cả các vấn đề đã được xử lý hoàn toàn. Mã của bạn hoàn toàn an toàn và không có vấn đề nghiêm trọng.

## B (Good)

**Ý nghĩa**: Mã của bạn có chất lượng bảo mật tốt, mặc dù có thể tồn tại một số vấn đề nhỏ nhưng không ảnh hưởng nghiêm trọng đến bảo mật. Đây là mức độ bạn muốn hướng tới trong quá trình phát triển.

## C (Average)

**Ý nghĩa**: Mã của bạn có thể có một số vấn đề bảo mật, nhưng không phải là vấn đề nghiêm trọng. Tuy nhiên, bạn nên giải quyết những vấn đề này càng sớm càng tốt để tránh các nguy cơ bảo mật trong tương lai.

## D (Poor)

**Ý nghĩa**: Mã nguồn của bạn có nhiều vấn đề bảo mật, một số vấn đề có thể tạo ra lỗ hổng bảo mật nghiêm trọng hoặc tiềm ẩn rủi ro. Bạn cần phải xem xét và khắc phục các vấn đề này ngay lập tức.

## E (Critical)

**Ý nghĩa**: Đây là mức độ xấu nhất, cho thấy mã nguồn của bạn có nhiều vấn đề bảo mật nghiêm trọng, có thể tạo ra các lỗ hổng bảo mật rất lớn hoặc đe dọa tính toàn vẹn của ứng dụng. Mã nguồn của bạn cần phải được xử lý ngay lập tức.

---

### Tóm tắt các mức độ bảo mật:

- **A**: Xuất sắc – Không có vấn đề bảo mật.
- **B**: Tốt – Có một số vấn đề nhỏ nhưng không nghiêm trọng.
- **C**: Trung bình – Có một số vấn đề cần phải xử lý.
- **D**: Kém – Nhiều vấn đề bảo mật cần được sửa chữa ngay lập tức.
- **E**: Nghiêm trọng – Các vấn đề bảo mật rất nghiêm trọng cần phải được giải quyết ngay lập tức.

# Tài liệu tham khảo

[SonarQube Documentation](https://docs.sonarsource.com/sonarqube-server/latest/)

[SonarQube Community](https://community.sonarsource.com/)
