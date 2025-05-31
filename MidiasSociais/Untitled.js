db.USA.find({})
   .projection({"items.snippet.title": 1, "items.snippet.publishedAt" : 1})
   .sort({ "items.snippet.publishedAt": -1})
   .limit(0)