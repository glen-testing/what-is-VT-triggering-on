# what-is-VT-triggering-on
A script to repeatedly upload chunks of a script until we determine what virus total is triggering on.

Haven't written this today, but this is a rewrite of a local thing I wrote back in 2012 when I was at a client.
That tool separated a flagged file into chunks until it stopped being flagged by the local AV client.

VT api public access is 4 requests per minute. This will default to that first. Potentially allow for api keys in a future version.
V1 will work on scripts.
1: Submit script to VT, see if it detects.
	If not, great!
	If it detects, we split the script into 4 chunks and see which one(s) detect.
		(wait time for api reset) 
		recurse until we get the smallest match(s) and report num_lines in match.

This shows us what AVs are detecting on.
Also record matches in a csv/json/tbd format to determine when AVs cut off.

Later ideas for future projects:
	Submit scripts with a nop added (language specific) to throw off checksums and see if that works.
	Code cave (add bulk of program at the end of benign program and put program in a packed format (previously used UPX here) that runs after insertion hook is triggered)
	Base64 custom (just reordered) alphabet encode/decode. AV won't know beable to decode without the custom alphabet, may hook it and run their own normal alphabet.
	Run timer and execute after timer (solarwinds 2 weeks, haha, if I do >15min it's usually pretty good. Gotta keep our own clock to thwart time skew in AV sandboxes)
	Detect sandbox and hide if sandboxed.
