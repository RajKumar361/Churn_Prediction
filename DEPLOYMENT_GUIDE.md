# GitHub Pages Deployment Guide

## Project Structure for GitHub Pages

Your project has been reorganized for GitHub Pages deployment:

```
project/
├── docs/                              # GitHub Pages source folder
│   ├── index.html                     # Main page (static)
│   ├── assets/
│   │   ├── css/
│   │   │   └── style.css              # Stylesheet
│   │   ├── js/
│   │   │   └── main.js                # JavaScript
│   │   └── images/
│   │       ├── dashboard.png
│   │       └── churn.png
│   └── _config.yml                    # Jekyll configuration (optional)
├── .nojekyll                          # Disables Jekyll processing
├── .github/
│   └── workflows/
│       └── deploy.yml                 # GitHub Actions workflow
├── Backend Files (for reference)
│   ├── app.py
│   ├── prediction_db.py
│   ├── train_new_model.py
│   ├── requirements.txt
│   └── models/
└── README.md
```

## Deployment Steps

### Step 1: Prepare Images

Copy your images to the `docs/assets/images/` folder:

- `dashboard.png`
- `churn.png`

If images don't exist, the site will still work but show broken image placeholders.

### Step 2: Push to GitHub

```bash
git add .
git commit -m "Prepare for GitHub Pages deployment"
git push origin Readytogo
```

### Step 3: Enable GitHub Pages

1. Go to your repository on GitHub
2. Navigate to **Settings → Pages**
3. Under "Build and deployment":
   - **Source**: Select "GitHub Actions"
   - **Branch**: Select the branch with your `docs` folder
   - **Folder**: Select `/ (root)` or `/docs` depending on your setup

### Step 4: Verify Deployment

- Wait 1-2 minutes for deployment
- Your site will be available at: `https://yourusername.github.io/Churn_Prediction`
- Check the **Actions** tab in GitHub to see deployment status

## Features

✅ **Fully Static** - Works on GitHub Pages (no backend needed)  
✅ **Responsive Design** - Works on mobile, tablet, and desktop  
✅ **Interactive Charts** - Uses Chart.js for data visualization  
✅ **Professional UI** - Dark blue theme with animations  
✅ **Demo Prediction** - Frontend-only prediction (random for demo)

## Important Notes

### Frontend-Only Deployment

This is a **static website only**. The prediction form generates random results for demonstration purposes.

### For Full Functionality with Backend

If you want the full ML prediction functionality:

1. **Deploy Backend Separately:**
   - Deploy `app.py` to Heroku, Railway, Vercel, or similar
   - Update API URLs in `docs/assets/js/main.js`

2. **Example Backend Deployment (Heroku):**

   ```bash
   heroku create your-app-name
   git push heroku main
   ```

3. **Update Frontend API Endpoint:**
   In `docs/index.html`, update the form submission to call your API:
   ```javascript
   const response = await fetch("https://your-backend-url/predict", {
     method: "POST",
     body: JSON.stringify(formData),
   });
   ```

## Troubleshooting

### Site Not Showing

- Verify `docs` folder is in root
- Check GitHub Pages settings
- Ensure `.nojekyll` file exists

### Images Not Loading

- Check image paths: `./assets/images/filename.png`
- Verify images exist in `docs/assets/images/`
- Use relative paths only

### CSS/JS Not Loading

- Check file paths in HTML
- Ensure `./assets/` prefix is used
- Clear browser cache (Ctrl+Shift+Delete)

### Forms Not Working

- Frontend form submission is for demo only
- To connect to real API, update JavaScript
- Add CORS headers if calling external API

## File Sizes & Performance

- `index.html`: ~15 KB
- `style.css`: ~12 KB
- `main.js`: <1 KB
- Images: Optimize for web (< 500 KB each)

**Total:** < 1 MB (excellent for GitHub Pages)

## Next Steps

1. Copy your images to `docs/assets/images/`
2. Push to GitHub
3. Enable GitHub Pages in repository settings
4. Share your site URL!

For questions or updates, refer to [GitHub Pages Documentation](https://docs.github.com/en/pages)
