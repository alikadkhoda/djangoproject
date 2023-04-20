from django.contrib import admin

# Register your models here.
from researchActivities.models import Paper, Conference, Journal, Jozveh, Presentation

class PaperAdmin(admin.ModelAdmin):
    list_display = ('title', 'doi', 'author1', 'author2', 'publication_date', 'conference', 'paper_image')

class ConferenceAdmin(admin.ModelAdmin):
    list_display = ('confTopic', 'confType', 'title', 'event_date', 'event_place')
class JournalAdmin(admin.ModelAdmin):
    list_display = ('journalType', 'title', 'issn', 'volume', 'publisher', 'rank')

admin.site.register(Paper, PaperAdmin)
admin.site.register(Conference, ConferenceAdmin)
admin.site.register(Journal, JournalAdmin)
admin.site.register(Jozveh)
admin.site.register(Presentation)