# 🚀 Deployment Instructions

## ✅ Git Repository Ready!

Your code is committed and ready to push to GitHub.

## 📤 Push to GitHub (Manual Steps)

### Option 1: Create New Repository on GitHub

1. Go to https://github.com/new
2. Repository name: `talking-rabbitt-mvp`
3. Description: `Conversational Analytics MVP with Streamlit`
4. Keep it Public (required for free Streamlit Cloud)
5. DO NOT initialize with README (we already have one)
6. Click "Create repository"

### Option 2: Run These Commands

After creating the repository on GitHub, run:

```bash
cd "/Users/virmani/Downloads/rabbit/untitled folder"
git remote add origin https://github.com/YOUR_USERNAME/talking-rabbitt-mvp.git
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username.

## ☁️ Deploy to Streamlit Cloud

### Step 1: Go to Streamlit Cloud
Visit: https://share.streamlit.io

### Step 2: Sign In
- Click "Sign in with GitHub"
- Authorize Streamlit Cloud

### Step 3: Deploy New App
1. Click "New app" button
2. Select your repository: `YOUR_USERNAME/talking-rabbitt-mvp`
3. Branch: `main`
4. Main file path: `app.py`
5. Click "Deploy!"

### Step 4: Wait for Deployment
- Takes 2-3 minutes
- You'll get a public URL like: `https://YOUR_USERNAME-talking-rabbitt-mvp.streamlit.app`

## 🎉 Your App Will Be Live!

Share the URL with anyone to demo your conversational analytics MVP.

## 📁 Repository Location
Local path: `/Users/virmani/Downloads/rabbit/untitled folder`

## 📋 Files Committed
- app.py (main application)
- requirements.txt (dependencies)
- sample_sales.csv (sample data)
- README.md (documentation)
- .gitignore (git exclusions)

## 🔑 Need GitHub Authentication?

If you need to authenticate with GitHub:

```bash
# Using HTTPS (will prompt for credentials)
git remote add origin https://github.com/YOUR_USERNAME/talking-rabbitt-mvp.git

# Or using SSH (if you have SSH keys set up)
git remote add origin git@github.com:YOUR_USERNAME/talking-rabbitt-mvp.git
```

## 🆘 Troubleshooting

**If push fails:**
- Make sure you're logged into GitHub
- Check repository name matches
- Ensure repository is created on GitHub first

**If deployment fails:**
- Check requirements.txt is present
- Verify app.py is in root directory
- Check Streamlit Cloud logs for errors
