# PHP CRUD App (with MySQL)

A simple PHP CRUD (Create, Read, Update, Delete) application using **MySQL (MariaDB)** and PHP’s built-in server. Great for learning PHP + database interactions without needing Apache or full-stack frameworks.

---

## 🚀 Features

- ✅ Create new records
- 📋 Read/list records
- ✏️ Update entries
- ❌ Delete entries
- 🛢️ Uses MySQL/MariaDB for persistent data
- ⚡ PHP built-in development server – no Apache needed

---

## 🛠️ Getting Started

### 1. Create Your Project Directory

```bash
mkdir -p ~/projects/crudapp
cd ~/projects/crudapp
```

### 2. Create the PHP Files

Make sure you have:
- `index.php`
- `create.php`
- `update.php`
- `delete.php`
- `db.php`

### 3. Configure Database Connection (`db.php`)

Edit `db.php` to match your MySQL settings:

```php
<?php
$host = 'localhost';
$db   = 'crud_db';
$user = 'your_mysql_user';
$pass = 'your_mysql_password';
$charset = 'utf8mb4';

$dsn = "mysql:host=$host;dbname=$db;charset=$charset";
$options = [
    PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $user, $pass, $options);
} catch (\PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}
?>
```

### 4. Start the Built-In PHP Server

```bash
php -S localhost:8000
```

Then open in browser:
```
http://localhost:8000
```

---

## 🗄️ Database Setup

Login to MySQL and run:

```sql
CREATE DATABASE crud_db;

USE crud_db;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## 📁 File Structure

```
crudapp/
│
├── index.php       # List users
├── create.php      # Add user
├── update.php      # Edit user
├── delete.php      # Delete user
├── db.php          # MySQL connection
└── README.md       # This file
```
