# Deployment Guide - Grocery Tracker

This guide will help you deploy your Flask grocery tracker application so it's available to everyone on the internet.

## 🚀 Deployment Options (Easiest to Hardest)

### Option 1: Render.com (RECOMMENDED - Free & Easy)
**Best for beginners, free tier available**

#### Steps:
1. **Create Account**: Go to https://render.com and sign up (free)

2. **Create New Web Service**:
   - Click "New +" → "Web Service"
   - Connect your GitHub repository (or upload files)

3. **Configure Settings**:
   - **Name**: grocery-tracker (or any name)
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Plan**: Free

4. **Environment Variables** (if needed):
   - Add any secret keys or configuration

5. **Deploy**: Click "Create Web Service"
   - Your app will be live at: `https://your-app-name.onrender.com`

---

### Option 2: Railway.app (Free Tier Available)
**Simple deployment, good for beginners**

#### Steps:
1. Go to https://railway.app and sign up
2. Click "New Project" → "Deploy from GitHub repo"
3. Select your repository
4. Railway auto-detects Flask and deploys
5. Your app will be live automatically!

---

### Option 3: PythonAnywhere (Free Tier)
**Good for Python apps, free tier available**

#### Steps:
1. Sign up at https://www.pythonanywhere.com
2. Go to "Web" tab → "Add a new web app"
3. Choose Flask and Python version
4. Upload your files via Files tab
5. Configure WSGI file to point to your app
6. Reload web app

---

### Option 4: Heroku (Paid, but has free alternatives)
**Note**: Heroku removed free tier, but you can use alternatives

---

### Option 5: VPS (Virtual Private Server)
**For more control (DigitalOcean, AWS, etc.)**

---

## 📋 Pre-Deployment Checklist

### 1. Update app.py for Production
Make sure your `app.py` has production-ready settings:

```python
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Remove db.drop_all() for production!
    app.run(debug=False, host='0.0.0.0', port=5000)  # debug=False in production
```

### 2. Environment Variables
Create a `.env` file for sensitive data (don't commit this):
```
SECRET_KEY=your-secret-key-here
DATABASE_URL=mysql+pymysql://USER:PASSWORD@HOST:3306/grocery_tracker?charset=utf8mb4
```

### 3. Database Considerations
- This app uses MySQL; apply `schema.sql` to create the database and tables.
- URL-encode special characters in `DATABASE_URL` credentials, or use separate `MYSQL_USER`, `MYSQL_PASSWORD`, `MYSQL_HOST`, `MYSQL_PORT`, and `MYSQL_DATABASE` variables as supported in `app.py`.

---

## 🔧 Quick Setup for Render.com (Recommended)

1. **Push to GitHub**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin your-github-repo-url
   git push -u origin main
   ```

2. **On Render.com**:
   - Connect GitHub repo
   - Use these settings:
     - Build Command: `pip install -r requirements.txt`
     - Start Command: `gunicorn app:app --bind 0.0.0.0:$PORT`
   - Add environment variable: `PORT=10000` (if needed)

3. **Deploy!**

---

## 🌐 Making it Accessible

Once deployed, your app will have a public URL like:
- `https://your-app-name.onrender.com`
- `https://your-app-name.railway.app`

Share this URL with anyone to access your application!

---

## ⚠️ Important Notes

1. **Never call `db.drop_all()`** in production (it is not used in the app entrypoint).
2. **Set `debug=False`** in production
3. **Use environment variables** for secrets
4. **Use MySQL** with `schema.sql` (or managed MySQL) for production data
5. **Set up proper backups** for production data

---

## 🆘 Troubleshooting

- **App won't start**: Check logs in deployment platform
- **Database errors**: Ensure MySQL is running, the database exists (`schema.sql`), and `DATABASE_URL` / `MYSQL_*` settings are correct
- **Import errors**: Check requirements.txt has all packages
- **Port issues**: Use `$PORT` environment variable

---

## 📞 Need Help?

Check the deployment platform's documentation or support forums.

