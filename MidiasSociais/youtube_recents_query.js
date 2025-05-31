db.youtube_recents.find({ })
   .projection({"items.snippet.title": 1, "items.snippet.publishedAt" : 1)
   .sort({})
   .limit(100)