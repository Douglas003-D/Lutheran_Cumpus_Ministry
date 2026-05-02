-- 1. Database Initialization
CREATE DATABASE IF NOT EXISTS lcm;
USE lcm;

-- 2. Admin & Authentication
CREATE TABLE IF NOT EXISTS admin (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 3. Students & Membership
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    phone VARCHAR(20),
    school_campus VARCHAR(100), 
    registered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 4. Events Tracking
CREATE TABLE IF NOT EXISTS events (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    description TEXT,
    event_date DATE NOT NULL,
    location VARCHAR(200),
    image VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 5. Gallery
CREATE TABLE IF NOT EXISTS gallery (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(200),
    image_path VARCHAR(255) NOT NULL,
    category VARCHAR(50) DEFAULT 'General',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 6. Downloads & Resources
CREATE TABLE IF NOT EXISTS downloads (
    id INT AUTO_INCREMENT PRIMARY KEY,
    display_name VARCHAR(200) NOT NULL,
    filename VARCHAR(255) NOT NULL,
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 7. Contact Messages
CREATE TABLE IF NOT EXISTS contact_messages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(20),
    inquiry_type VARCHAR(100),
    message TEXT NOT NULL,
    is_read BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 8. Core Site Settings
CREATE TABLE IF NOT EXISTS site_settings (
    id INT PRIMARY KEY,
    office_location VARCHAR(255) DEFAULT 'Main Campus',
    paybill_no VARCHAR(255),
    paybill_acc_no VARCHAR(255),
    bank_name VARCHAR(255),
    account_no VARCHAR(255),
    account_name VARCHAR(255),
    paypal_email VARCHAR(255),
    mpesa_name VARCHAR(255),
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- 9. Alumni Network (UPDATED & FINAL)
CREATE TABLE IF NOT EXISTS alumni (
    id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,           -- Added: To match your dashboard/export
    grad_year INT NOT NULL,
    course_studied VARCHAR(255) NOT NULL,
    location VARCHAR(100),
    profession VARCHAR(255),               -- Added: To match your dashboard/export
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Ensure default site settings row exists
INSERT IGNORE INTO site_settings (id, office_location) VALUES (1, 'Main Campus');