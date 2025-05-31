db.mostpopular.find({})
.project({"items.snippet.title": 1, "items.snippet.publishedAt" : 1})