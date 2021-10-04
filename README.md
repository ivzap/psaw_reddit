# Simple Reddit PSAW Wrapper Usage:
![image](https://user-images.githubusercontent.com/64557487/135790349-c9f526d2-ef4d-4832-9f0e-3ccaee5b5da3.png)

### Historical Posts:
> Parameters

| Name   |     Type      | Description  |
| -------------       | ------------- |------------- |
| after  | String     |the date to start collecting data(inclusive)              |
| before  | String    |the date to stop grabbing data(inclusive)              |
| subreddit | String  |the subreddit to get posts from              |
| limit  | Int        | the max amount of posts to collect             |

```python
after = "2021-08-20"
before = "2021-08-30"
subreddit = "wallstreetbets"
limit = 1000
get_reddit_histo(after, before, subreddit, limit)
```

### Recent Posts:
> Parameters

| Name   |     Type      | Description  |
| -------------       | ------------- |------------- |
| minutes  | Int     |get all the posts in the last n minutes              |
| subreddit  | String    |the subreddit to get posts from              |

```python
minutes = 5
subreddit = "wallstreetbets"
get_reddit_recent(minutes, subreddit)
```
