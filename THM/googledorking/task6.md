# What is Google Dorking?

## Notes
- To narrow down the search results
- `"search query"` will look for exact match
- `site` and query to search the specific site. `site: bbc.co.uk gchq news`
- Few common terms we can search and combine:
|Term|Action
|-----|-----|
|filetype:|Search for a file by its extension (e.g. PDF)|
|cache:|View Google's Cached version of a specified URL|
|intitle:|The specified phrase MUST appear in the title of the page|

- Example: `site:bbc.co.uk filetype:pdf`


## Questions
1. What would be the format used to query the site bbc.co.uk about flood defences
```
site: bbc.co.uk flood defences
```

2. What term would you use to search by file type?
```
filetype:
```

3. What term can we use to look for login pages?
```
intitle: login
```