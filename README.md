# 📰 pyWebScraper — Hacker News Filter Tool

A Python script that scrapes **Hacker News** and filters articles based on community interest.  
This tool was inspired by the **Zero to Mastery (ZTM)** Python course and focuses on extracting **relevant, high-quality stories** using upvote thresholds.

---

## 💡 Overview

This scraper pulls article data from Hacker News and returns only the most relevant stories — currently defined as articles with **100+ upvotes**, though this can be easily adjusted.

The script demonstrates:

- Web scraping without a frontend
- HTML parsing and data extraction
- Sorting and filtering scraped data
- Clean, readable Python functions

---

## ✨ Features

| Feature | Description |
|--------|-------------|
| 🔍 Scrape Hacker News | Pulls article titles & links |
| 📊 Filter Top Stories | Shows only articles above a set vote threshold |
| 📈 Sort by Popularity | Sorted from highest to lowest votes |
| 🔧 Easily Adjustable | Change vote threshold or sorting rules |

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|--------|
| Python | Logic & parsing |
| `requests` | Retrieve HTML |
| `BeautifulSoup` | Parse page content |

> Note: Some versions of ZTM examples used `bs4`. Make sure it is installed if not already.

---

## 🚀 Running the Script

### 🔧 Requirements

Install dependencies:

```bash
pip install requests bs4

# Run app
python pyWebScraper.py
```

## 📓 Example Output
- 📌 245 votes — "New Python Web Framework Announced"  
- 🔗 https://news.ycombinator.com/example-link

## 🔮 Future Improvements
- 🌐 Expand to scrape additional tech news sites
- 🖥️ Create a frontend UI to display results
- ⏱️ Add scheduled running or auto-refresh
- 💾 Save results to a file or database
- 📱 Convert into a mobile “tech news filter” app

## 🎓 Attribution
Inspired by the Zero to Mastery Python Developer course.
