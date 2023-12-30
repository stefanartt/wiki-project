from django.shortcuts import render
import markdown
from . import util

def conver_md_to_html(title):
    content = util.get_entry(title)
    markdowner = markdown.Markdown()
    if content == None:
        return None
    else:
        return markdowner.convert(content)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    if conver_md_to_html(title) == None:
        return render(request, "encyclopedia/error.html", {
            "message": "This page does not exist"
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": conver_md_to_html(title)
        })
    
def search(request):
    if request.method == "POST":
        entry_search = request.POST['q']
        if conver_md_to_html(entry_search) is not None:
            return render(request, "encyclopedia/entry.html", {
            "title": entry_search,
            "content": conver_md_to_html(entry_search)
        })
        else:
            recommendation = []
            allEntries = util.list_entries()
            for entry in allEntries:
                if entry_search.lower() in entry.lower():
                    recommendation.append(entry)
            return render(request, "encyclopedia/search.html", {
                "recommendation": recommendation,
                "search_results": entry_search
            })
         
    

