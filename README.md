# LinkeFly - 150+ Online Web Tools & 30 SEO Blog Posts Platform
### Complete Production Backup & One-Click Deployment Package

This repository contains the complete production-ready source code, assets, database, and configurations for **LinkeFly** (built on SumoWebTools / Laravel 8+). It includes **150+ high-traffic online web utilities**, **30 comprehensive pillar SEO blog posts** (each equipped with 2 dark-theme inline technical infographics and high-res featured images), full multi-locale support across **10 languages**, Google AdSense legal compliance pages, and a modern Deep Indigo & Royal Blue UI theme.

---

## 📦 What Is Included in This Repository

1. **Complete Web Application Code**:
   - `components/`: Full Laravel application (models, controllers, routes, views, translations, vendor packages).
   - `assets/`: Custom modern stylesheet (`app.min.css`), JS bundles, fonts, SVG icons, and 90 high-resolution blog images in `assets/img/blog/`.
   - `index.php`, `.htaccess`, `robots.txt`, `ads.txt`, `favicon.ico`: Optimized for Apache / LiteSpeed / Nginx.
2. **Complete MySQL Database Dump**:
   - `database.sql` (3.4 MB): Full MySQL dump with all 28 tables, 150 tools, 30 blog posts, 1,870 translation records across 10 locales, user roles, footers, headers, and SEO metadata.
3. **Stand-Alone Deployment ZIP**:
   - `linkefly_complete_backup_with_db.zip`: Pre-packaged 120 MB archive ready to upload directly to cPanel / File Manager for instant migration to any new hosting or domain.
4. **Automation & Management Scripts**:
   - `scripts/`: Python scripts for database migrations, blog generation, Pillow infographic generation, and remote FTP management.

---

## 🚀 Easy Hosting Deployment Guide (cPanel / Hostinger / CyberPanel / DirectAdmin)

Follow these simple steps to deploy this website on any new domain or hosting server in under 5 minutes:

### Step 1: Upload Files via File Manager
1. Log in to your hosting control panel (cPanel, Hostinger hPanel, DirectAdmin, or CyberPanel).
2. Open **File Manager** and navigate to your domain's public directory (usually `public_html` or `public_html/yourdomain.com`).
3. Upload `linkefly_complete_backup_with_db.zip` (or all files from this repository).
4. Right-click the uploaded `.zip` file and select **Extract** directly into `public_html`.

### Step 2: Create a MySQL Database
1. In your hosting panel, navigate to **MySQL Databases** (or **Databases**).
2. Create a new database (e.g., `user_toolsdb`).
3. Create a new database user (e.g., `user_toolsuser`) and set a strong password.
4. Add the user to the database and ensure you grant **ALL PRIVILEGES**. Note down your DB Name, DB User, and DB Password.

### Step 3: Import the Database (`database.sql`)
1. In your hosting panel, open **phpMyAdmin**.
2. From the left sidebar, click on your newly created database.
3. Click the **Import** tab at the top.
4. Click **Choose File** and select `database.sql` from the extracted files.
5. Click **Import** (or **Go**) at the bottom. Wait for the green success checkmark confirming all 28 tables were imported.

### Step 4: Configure `components/.env`
1. In File Manager, navigate inside the `components` directory and edit the `.env` file (ensure "Show Hidden Files" is enabled in File Manager settings):
2. Update the following lines with your new domain and database credentials:
   ```env
   APP_NAME="LinkeFly"
   APP_ENV=production
   APP_KEY=base64:7j89K2L... (keep existing or run php artisan key:generate)
   APP_DEBUG=false
   APP_URL=https://your-new-domain.com

   DB_CONNECTION=mysql
   DB_HOST=127.0.0.1
   DB_PORT=3306
   DB_DATABASE=your_new_database_name
   DB_USERNAME=your_new_database_user
   DB_PASSWORD=your_new_database_password
   ```
3. Save changes.

### Step 5: Verify Permissions
Ensure the following directories have write permissions (chmod `755` or `775`):
- `storage/`
- `components/storage/`
- `components/storage/framework/`
- `components/storage/logs/`
- `components/bootstrap/cache/`

### Step 6: Test Your Live Website!
Visit `https://your-new-domain.com` in your web browser:
- Homepage displays all 150 online tools categorized with modern deep indigo & royal blue styling.
- `/blog` displays all 30 long-form pillar posts with high-res featured images and inline infographics.
- `/privacy-policy`, `/terms-of-service`, `/about-us`, `/contact`, and `/disclaimer` are pre-configured for Google AdSense compliance.

---

## ⚙️ Technical Requirements
- **Web Server**: Apache 2.4+ (with `mod_rewrite`), LiteSpeed, or Nginx.
- **PHP Version**: PHP 8.1, 8.2, or 8.3.
- **PHP Extensions**: `pdo_mysql`, `mbstring`, `openssl`, `tokenizer`, `xml`, `ctype`, `json`, `fileinfo`, `curl`, `zip`, `gd` (or `imagick`).
- **Database**: MySQL 5.7+ or MariaDB 10.3+.

---

## 📝 License & Attribution
- Built with SumoWebTools & Laravel.
- Customized, themed, and enhanced by CodeStackLab / LinkeFly.
