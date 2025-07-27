# appscripts
A collection of useful build step scripts for iOS apps

To reduce your app’s size these scripts can be invoked as a build step like the following.

```
if [ "${CONFIGURATION}" = "Release" ]; then

python3 Scripts/plist-minify.py
python3 Scripts/json-minify.py

fi
```

This will
- Re-encode plists to binary where it saves space
- Strip whitespace from JSON files

More details [here](https://objectionable-c.com/posts/shrink-static-files/)