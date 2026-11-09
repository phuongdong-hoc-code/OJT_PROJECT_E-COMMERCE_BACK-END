-- Tạo database app_db + bảng items + dữ liệu mẫu.
-- Cách chạy bằng MySQL Workbench:
--   File > Open SQL Script... > chọn file này > bấm nút tia sét (Execute) > Refresh ô SCHEMAS.
-- Chạy lại nhiều lần không lỗi (đã có thì bỏ qua), chỉ là dữ liệu mẫu sẽ bị thêm lặp.

SET NAMES utf8mb4; -- để tiếng Việt không bị lỗi font

CREATE DATABASE IF NOT EXISTS app_db
  CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE app_db;

CREATE TABLE IF NOT EXISTS items (
  id          INT AUTO_INCREMENT PRIMARY KEY,
  name        VARCHAR(255) NOT NULL,
  description TEXT NULL,
  price       DECIMAL(12, 2) NOT NULL DEFAULT 0,
  low_stock_threshold INT NOT NULL DEFAULT 5,
  created_at  DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at  DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS stock_logs (
  id            INT AUTO_INCREMENT PRIMARY KEY,
  product_id    INT NOT NULL,
  movement_type ENUM('NHẬP', 'BÁN', 'HUỶ ĐƠN', 'ĐIỀU CHỈNH') NOT NULL,
  quantity      INT NOT NULL,
  stock_after   INT NOT NULL,
  order_code    VARCHAR(50) NULL,
  note          TEXT NULL,
  performed_by  VARCHAR(100) NOT NULL,
  created_at    DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  INDEX ix_stock_logs_product_id (product_id),
  INDEX ix_stock_logs_order_code (order_code),
  CONSTRAINT fk_stock_logs_product_id
    FOREIGN KEY (product_id) REFERENCES items(id) ON DELETE RESTRICT,
  CONSTRAINT ck_stock_logs_quantity_nonzero CHECK (quantity <> 0),
  CONSTRAINT ck_stock_logs_stock_after_nonnegative CHECK (stock_after >= 0)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO items (name, description, price) VALUES
  ('Cơm rang dưa bò', 'Món mẫu để kiểm tra API', 45000),
  ('Trà đá', 'Dữ liệu mẫu số 2', 5000);
