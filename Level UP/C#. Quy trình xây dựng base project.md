# Setup Environment

## Server Setup:

- **Request Server**:
  - Windows Server 2019
  - 2-4GB RAM, Core i5

## Install SQL Server:

- Enable SQL Authentication
- Open port 1433 for remote access

## Install IIS:

- **Websites**:
  - tuanflute275.dev.com
  - tuanflute275.stag.com (Staging - kiểm thử)
  - tuanflute275.prod.com (Production - online)

## Install Hosting Bundle:

1. Modify `web.config`:
   - Set `environment`
   - Enable `log`
2. Add Host entries for Windows:

   - `127.0.0.1 tuanflute275.dev.com`
   - `127.0.0.1 tuanflute275.stag.com`
   - `127.0.0.1 tuanflute275.prod.com`

3. Want to use IP:PORT
4. Open necessary ports

## Folder Structure:

- **WWW**:
  - Backend:
    - Dev | Stag | Prod
  - Frontend:
    - Dev | Stag | Prod
  - BackgroundJob (Chạy ngầm)

_Note_: Never delete or override when publishing new version.

## CI/CD Setup:

- Install:
  - Git SCM
  - .NET SDK
  - Java
  - Jenkins
  - ngrok
- Jenkins Plugins:
  - Install necessary plugins for Jenkins

---

## Environment Setup:

- **Dev**: Swagger UI, run HTTP
- **Stag**: Swagger UI, run HTTP
- **Prod**: Run HTTPS (Use `UseHtst()` to Force SSL)

---

## Project Setup:

### Technologies:

- **CQRS-EventSourcing**: MediatR (CommandBus - QueryBus - EventBus)
  - Domain Event: Local Inmemory
  - IntegrationEvent: Publish to message queue
- **Fluent Validation**: Model validation (request model - domain model)
- **Entity Framework**
- **Dapper**: Use raw SQL queries (`SELECT * FROM table`)
- **Mapper**: Mapping Objects
- **JSON**: Newtonsoft.Json - System.Text.Json
- **API Versioning**
- **API Documentation**: Swagger UI
- **Security**: JWT
- **Authentication & Authorization**: Identity
- **Databases**: SQL Server, Oracle, MongoDB etc.
- **Redis**
- **Masstransit**: ServiceBus connected to RabbitMQ
- **Logging**: SeriLog
- **Domain Driven Design**
- **Content Negotiation**: (Nội dung api có thể là JSON hoặc XML)
  ...

### Code Structure:

- **Coding Conventions**
- **Unit Testing**: Infrastructure
- **Logging**
- **Authentication & Authorization**: JWT
- **Token Management**: Refresh tokens (issue new tokens), Revoked tokens (revoke and delete tokens) (+ Manage Token: Refresh token (cấp mới token), revoked Token (thu hồi, xóa token))
- **Response Object || Result**: Standardized API response model (Result (Mẫu trả về của API => ResponseObject))
- **Exception Handling**
- **Pagination, Searching, Sorting**
- **API Versioning**

### RESTful API Design:

- [Microsoft Best Practices for API Design](https://learn.microsoft.com/en-us/azure/architecture/best-pratices/api-design)

#### Example Endpoints:

- **GET**: `api/orders` => Get list of orders
- **GET**: `api/orders/{orderId}` => Get order detail
- **POST**: `api/order` => Create an order
- **POST**: `api/orders` => Create array of orders
- **PUT**: `api/orders/{orderId}` => Update an order
- **DELETE**: `api/orders/{orderId}` => Delete an order
- **GET**: `api/customers/{customerId}/orders` => Get orders by customerId

#### Response Codes:

- **200**: OK
- **204**: No Content
- **201**: Created (CreatedAtRoute, CreatedAtAction)
- **400**: Bad Request
- **404**: Not Found
- **401**: Unauthorized
- **403**: Forbidden
- **500**: Internal Server Error

### Asynchronous Programming:

- **Async/Await**: Use `async` and `await` for non-blocking operations
  - **I/O-bound**: File/database operations, network calls
  - **CPU-bound**: Heavy computation

### Caching Strategies:

- **Response Cache**
- **In-memory Cache**
- **Distributed Cache**
- Handle invalid cache when data changes (Kiểm soát sự thay dổi của dữ liệu) (e.g., delete cache key on create, update, or delete operations)

>EX: Create, Update, Delete => delete cache key =>delete data in redis

>Get ==> cache key => get new data in redis

---

## Clean Architecture:

- Domain: Domain model , Bussiness, logic
- Application refrences Domain => Handle use case: MediatR
- Infrastructure refrences Domain => Build setting project
- Infrastructure.EF refrences Domain => Handle connect SQL
- Infrastructure.SMTP refrences Domain => Handle send email
- Infrastructure.EventBus refrences Domain => Handle event
- Infrastructure.MessageBus refrences Domain => Handle rabbitMQ, Kafka
- Infrastructure.Job refrences Domain => Handle background TASK (nghiệp vụ chạy ngầm)
- Persistence
- Presentation refrences Application => COntroller API , ISender - mediatR
- WebAPI refrences Application, Infrastructure, Presentation, Persistence  => Dependendce Injection(DI)
