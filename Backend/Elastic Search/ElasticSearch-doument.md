# TỔNG QUAN VỀ ELASTICSEARCH

Elasticsearch là một công cụ tìm kiếm và phân tích dữ liệu mã nguồn mở, dựa trên Apache Lucene.
Nó được thiết kế để lưu trữ, tìm kiếm và phân tích dữ liệu phi cấu trúc một cách nhanh chóng và hiệu quả.
Ứng dụng phổ biến của Elasticsearch bao gồm:

- Tìm kiếm toàn văn bản (Full-Text Search).
- Phân tích log.
- Phân tích dữ liệu thời gian thực.

---

# CÁC CÂU LỆNH THƯỜNG DÙNG TRONG ELASTICSEARCH

## 1. Kiểm tra trạng thái cluster:
```bash
GET /_cluster/health
```

## 2. Tạo một index mới:
```bash
PUT /ten_index
```

## 3. Xóa một index:
```bash
DELETE /ten_index
```

## 4. Thêm tài liệu vào index:
```bash
POST /ten_index/_doc/
{
    "field1": "value1",
    "field2": "value2"
}
```

## 5. Lấy tài liệu theo ID:
```bash
GET /ten_index/_doc/1
```

## 6. Tìm kiếm tất cả tài liệu trong một index:
```bash
GET /ten_index/_search
```

## 7. Tìm kiếm với điều kiện:
```bash
GET /ten_index/_search
{
  "query": {
    "match": {
      "field1": "value1"
    }
  }
}
```

## 8. Cập nhật tài liệu:
```bash
POST /ten_index/_update/1
{
  "doc": {
    "field1": "new_value"
  }
}
```

## 9. Xóa tài liệu:
```bash
DELETE /ten_index/_doc/1
```

## 10. Lấy thông tin về index:
```bash
GET /ten_index
```

## 11. Tạo mapping cho index:
```bash
PUT /ten_index
{
  "mappings": {
    "properties": {
      "field1": {
        "type": "text"
      },
      "field2": {
        "type": "keyword"
      }
    }
  }
}
```

## 12. Đếm số lượng tài liệu trong index:
```bash
GET /ten_index/_count
```


## 12.5. Xem tất cả các chỉ mục (index):
```bash
GET _cat/indices?v
```

# Trạng thái cột "health" trong chỉ mục:
- **Green**: Hoàn thành tạo cluster (Ok)

- **Yellow**: Một cụm không có cluster (OK)

- **Red**: Cảnh báo bất thường (Not Ok)



# CƠ BẢN VỀ ELASTICSEARCH

Elasticsearch là một công cụ tìm kiếm và phân tích dữ liệu phi cấu trúc (unstructured data), được xây dựng trên nền tảng Apache Lucene. Nó cho phép bạn lưu trữ, tìm kiếm, và phân tích dữ liệu với tốc độ rất nhanh.

- **Cluster:** Một cluster trong Elasticsearch bao gồm nhiều node (máy chủ) làm việc cùng nhau để lưu trữ và xử lý dữ liệu. Mỗi cluster có một tên duy nhất và tất cả các node trong cluster này đều chia sẻ dữ liệu.
   
- **Node:** Một node là một đơn vị (máy chủ) trong cluster, chịu trách nhiệm lưu trữ dữ liệu và thực hiện các tác vụ tìm kiếm hoặc phân tích.

- **Index:** Một index là tập hợp các tài liệu (documents) được lưu trữ. Mỗi index có thể chứa hàng triệu tài liệu và được tổ chức theo cách có thể tìm kiếm và phân tích hiệu quả.

- **Document:** Một document là một đơn vị dữ liệu trong Elasticsearch, tương tự như một bản ghi trong cơ sở dữ liệu. Document là một JSON object chứa các cặp khóa-giá trị.

- **Field:** Các trường trong document (tương tự như các cột trong cơ sở dữ liệu quan hệ). Mỗi trường có một kiểu dữ liệu (text, keyword, date, integer, v.v.).

- **Mapping:** Mapping là cách xác định cấu trúc của các tài liệu trong một index. Nó định nghĩa các trường (fields) và kiểu dữ liệu của chúng.

# CÁC KHÁI NIỆM QUAN TRỌNG

- **Shards và Replicas:** Elasticsearch chia các index thành các phần nhỏ gọi là **shards** để phân tán và tối ưu hóa hiệu suất. Mỗi shard có thể có một hoặc nhiều bản sao gọi là **replicas** để đảm bảo tính sẵn sàng và an toàn dữ liệu.
   
- **Query DSL:** Elasticsearch sử dụng một ngôn ngữ truy vấn JSON mạnh mẽ, được gọi là **Query DSL**. Điều này giúp bạn xây dựng các truy vấn phức tạp để tìm kiếm hoặc phân tích dữ liệu.

# CÁC BƯỚC CƠ BẢN KHI LÀM VIỆC VỚI ELASTICSEARCH

- **Tạo Index:** Đầu tiên, bạn tạo một index để lưu trữ tài liệu. Mỗi index có thể có nhiều tài liệu và các trường dữ liệu.
   
- **Thêm dữ liệu:** Sau khi tạo index, bạn có thể thêm dữ liệu vào Elasticsearch dưới dạng các tài liệu.
   
- **Tìm kiếm:** Sử dụng các truy vấn (query) để tìm kiếm trong các tài liệu đã được lưu trữ trong index.
   
- **Cập nhật và xóa:** Bạn có thể cập nhật hoặc xóa các tài liệu dựa trên ID của chúng.

# CÁC VÍ DỤ VỀ QUERY DSL

- **Match Query:** Tìm các tài liệu mà trường "field1" chứa giá trị "value1".
  ```json
  {
    "query": {
      "match": {
        "field1": "value1"
      }
    }
  }
  ```

- **Term Query:** Tìm các tài liệu có trường "field1" chính xác với giá trị "value1".
  ```json
  {
    "query": {
      "term": {
        "field1": "value1"
      }
    }
  }
  ```

- **Range Query:** Tìm các tài liệu mà giá trị của trường "date" nằm trong một khoảng thời gian nhất định.
  ```json
  {
    "query": {
      "range": {
        "date": {
          "gte": "2023-01-01",
          "lte": "2023-12-31"
        }
      }
    }
  }
  ```

# CÀI ĐẶT VÀ CẤU HÌNH

- **Cài đặt Elasticsearch:** Bạn có thể cài đặt Elasticsearch trên các hệ điều hành như Linux, macOS hoặc Windows. Việc cài đặt khá đơn giản và bạn có thể làm theo hướng dẫn trên trang chủ của Elasticsearch.
   
- **Cấu hình Elasticsearch:** Bạn có thể cấu hình các tham số như số lượng shards, replicas, cấu hình bộ nhớ, và các tham số khác để tối ưu hóa hiệu suất của Elasticsearch.

# CÁC CÔNG CỤ LIÊN QUAN

- **Kibana:** Một công cụ để trực quan hóa và phân tích dữ liệu từ Elasticsearch. Kibana cung cấp giao diện web để tìm kiếm, phân tích và trực quan hóa dữ liệu.

- **Logstash:** Một công cụ để thu thập, xử lý và gửi dữ liệu vào Elasticsearch. Logstash hỗ trợ nhiều loại đầu vào và đầu ra khác nhau.

- **Beats:** Một bộ công cụ nhẹ để gửi dữ liệu vào Elasticsearch. Các Beats chuyên biệt cho các loại dữ liệu như log, metrics, và hơn thế nữa.

# ỨNG DỤNG CỦA ELASTICSEARCH

- **Tìm kiếm web:** Elasticsearch được sử dụng rộng rãi trong việc tìm kiếm trên các website lớn và các hệ thống tìm kiếm sản phẩm, bài viết, v.v.
   
- **Phân tích dữ liệu log:** Elasticsearch rất mạnh mẽ trong việc thu thập và phân tích log từ các hệ thống, giúp phát hiện lỗi và giám sát hệ thống.
   
- **Phân tích thời gian thực:** Elasticsearch có thể xử lý dữ liệu theo thời gian thực, rất hữu ích cho các ứng dụng cần phân tích dữ liệu mới ngay lập tức.
