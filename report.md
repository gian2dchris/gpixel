# GPixel

Please note that Tracking Pixels that only utilize  `<img>` tags have the following limitations:

- Cannot be fired multiple times on each page load 
- Cannot track standard or custom events triggered by UI interactions (e.g., a button click) 
- Subject to HTTP GET limits in sending custom data or long URLs 
- Cannot be loaded asynchronously

**`referrerpolicy`**  

A string indicating which referrer to use when fetching the resource: 

- `no-referrer`: The [`Referer`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referer) header will not be sent.
- `no-referrer-when-downgrade`: No `Referer` header is sent when navigating to an origin without [HTTPS](https://developer.mozilla.org/en-US/docs/Glossary/HTTPS). This is the default if no policy is otherwise specified.
- `origin`: The `Referer` header will include the page's origin (scheme, [host](https://developer.mozilla.org/en-US/docs/Glossary/host), and [port](https://developer.mozilla.org/en-US/docs/Glossary/port)).
- `origin-when-cross-origin`: Navigating to other origins will limit the included referral data to the scheme, host, and port,  while navigating from the same origin will include the full path and  query string.
- `unsafe-url`: The `Referer` header will always include the origin, path and query string, but not the fragment, password, or username. **This is unsafe** because it can leak information from TLS-protected resources to insecure origins.

## Google analytics Privacy Information

**Privacy Policy:**

Collected: Anonymous (Ad Views, Analytics, Browser Information, Cookie Data , Date/Time,  Demographic Data, Hardware/Software Type, Internet Service Provider,  Interaction Data , Page Views , Serving Domains)

Pseudonymous (IP Address (EU PII), Search History, Location Based Data, Device ID (EU PII))

PII (Name , Address, Phone Number, Email Address, Login, EU- IP Address, EU- Unique Device ID )

**Data Sharing:**

Aggregate data is shared with 3rd parties.

Anonymous data is shared with 3rd parties.

PII data is shared with 3rd parties.

Sensitive data is shared with 3rd parties.

**Google operates:**

AdMeld, AdMob, Adometry, Apture, Channel Intelligence,  Custom Search Ads, DoubleClick, DoubleClick Ad Exchange-Buyer,  DoubleClick Ad Exchange-Seller, DoubleClick Bid Manager, DoubleClick  DART, DoubleClick Floodlight, DoubleClick Spotlight, Doubleclick Video  Stats, FeedBurner, GA Audiences, GDN Notice, Google Ads Measurement,  Google Adsense, Google Adsense, Google Adsense Asynchronous, Google  AdServices, Google AdWords Conversion, Google Adwords User Lists, Google Affiliate Network, Google AJAX Search API, Google Analytics, Google  API, Google Commerce, Google Custom Search, Google Custom Search Engine, Google Display Network, Google Dynamic Remarketing, Google Fonts,  Google FriendConnect, Google IMA, Google Interactive Media, Google JSAPI Stats Collection, Google Pingback, Google Publisher Tags, Google  Safeframe, Google Shopping Reviews, Google Syndication, Google Tag  Manager, Google Translate, Google Travel Adds, Google Trusted Stores,  Google Users, Google Website Optimizer, Google Widgets, Google+  Platform, Gstatic, Maps, Meebo Bar, Mindset Media, PostRank, Swiffy

https://www.pixelstech.net/article/1561789561-A-mini-guide-to-HTTP-referer

https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img#attr-referrerpolicy

https://developers.facebook.com/docs/facebook-pixel/advanced#installing-the-pixel-using-an-img-tag

https://developers.facebook.com/docs/facebook-pixel/implementation/conversion-tracking

https://developers.facebook.com/docs/facebook-pixel/implementation/pixel-for-official-events