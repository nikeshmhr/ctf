# Robots.txt

## Notes
- First thing indexed by crawlers
Here we have a few keywords...

|Keyword|Function|
|-----|------|
User-agent|Specify the type of "Crawler" that can index your site (the asterisk being a wildcard, allowing all "User-agents"
Allow|Specify the directories or file(s) that the "Crawler" can index
Disallow|Specify the directories or file(s) that the "Crawler" cannot index
Sitemap|Provide a reference to where the sitemap is located (improves SEO as previously discussed, we'll come to sitemaps in the next task)


## Questions
1. Where would "robots.txt" be located on the domain "ablog.com"
```
ablog.com/robots.txt
```

2. If a website was to have a sitemap, where would that be located?
```
/sitemap.xml
```

3. How would we only allow "Bingbot" to index the website?
```
User-agent: Bingbot
```

4. How would we prevent a "Crawler" from indexing the directory "/dont-index-me/"?
```
Disallow:/dont-index-me/
```

5. What is the extension of a Unix/Linux system configuration file that we might want to hide from "Crawlers"?
```
.conf
```