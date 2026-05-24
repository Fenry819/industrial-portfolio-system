from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    short_description = models.CharField(max_length=255, help_text="A one-liner for the grid card.")
    full_description = models.TextField(help_text="Detailed breakdown of architecture and problem solved.")
    tech_stack = models.CharField(max_length=255, help_text="Comma separated (e.g., Python, Django, Gemini 2.5)")
    
    # Links
    github_link = models.URLField(blank=True, null=True)
    live_link = models.URLField(blank=True, null=True)
    
    # Media & Sorting
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    is_featured = models.BooleanField(default=False, help_text="Check this to give it the massive hero-grid treatment (e.g., AI Research Studio).")
    order = models.IntegerField(default=0, help_text="Lower numbers appear first.")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title

    def get_tech_list(self):
        return [tech.strip() for tech in self.tech_stack.split(',')]