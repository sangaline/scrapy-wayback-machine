![The Scrapy Wayback Machine Logo](img/logo.png)

# Scrapy Wayback Machine Middleware

This project provides a [Scrapy](https://scrapy.org) middleware for scraping archived snapshots of webpages as they appear on [archive.org](http://archive.org)'s [Wayback Machine](https://archive.org/web/).
This can be useful if you're trying to scrape a site that has scraping measures that make direct scraping impossible or prohibitively slow.
It's also useful if you want to scrape a website as it appeared at some point in the past or to scrape information that changes over time.

If you're just just interested in mirroring page content or would like to parse the HTML content in a language other than python then you should check out [the Wayback Machine Scraper](https://github.com/sangaline/wayback-machine-scraper).
It's a command-line utility that uses the middleware provided here to crawl through historical snapshots of a website and save them to disk.
It's highly configurable in terms of what it scrapes but it only saves the unparsed content of the pages on the site.
This may or may not suit your needs.

If you're using [Scrapy](https://scrapy.org) already or interested in parsing the data that is crawled then this `WaybackMachineMiddleware` is probably what you want.
This middleware handles all of the tricky parts and passes normal `response` objects to your [Scrapy](https://scrapy.org) spiders with archive timestamp information attached.
The middleware is very unobtrusive and should work seamlessly with existing [Scrapy](https://scrapy.org) middlewares, extensions, and spiders.

## Installation

The package can be installed using `pip`.

```bash
pip install scrapy-wayback-machine
```

## Usage

To enable the middleware you simply have to add

```python
DOWNLOADER_MIDDLEWARES = {
    'scrapy_wayback_machine.WaybackMachineMiddleware    ': 5,
}

WAYBACK_MACHINE_TIME_RANGE = (start_time, end_time)
```

to your [Scrapy](https://scrapy.org) settings.
The start and end times can be specified as `datetime.datetime` objects, Unix timestamps, `YYYYmmdd` timestamps, or `YYYYmmddHHMMSS` timestamps.
The type will be automatically inferred from the content and the ranges will limit the range of snapshots to crawl.
You can also pass a single time if you would like to scrape pages as they appeared at that time.

After configuration, responses will be passed to your spiders as they normally would.
Both `response.url` and all links within `response.body` point to the unarchived content so your parsing code should work the same regardless of whether or not the middleware is enabled.
If you need to access either the time of the snapshot or the [archive.org](http://archive.org) URL for a response then this information is easily available as metadata attached to the response.
Namely, `response.meta['wayback_machine_time']` contains a `datetime.datetime` corresponding to the time of the crawl and `response.meta['wayback_machine_url']` contains the actual URL that was requested.
Unless you're scraping a single point in time, you will almost certainly want to include the timestamp in the items that your spiders produce to differentiate items scraped from the same URL.

### Example

[The Wayback Machine Scraper](https://github.com/sangaline/wayback-machine-scraper) command-line utility is a good example of how to use the middleware.
The necessary settings are defined in [\_\_main\_\_.py](https://github.com/sangaline/wayback_machine_scraper/scraper/__main__.py) and the handling of responses is done in [mirror_spider.py](https://github.com/sangaline/wayback_machine_scraper/scraper/mirror_spider.py).
The `MirrorSpider` class simply uses the `response.meta['wayback_machine_time']` information attached to each response to construct the snapshot filenames and is otherwise a fairly generic spider.
