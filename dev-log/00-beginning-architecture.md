## Beginnings

Today is December 2nd, 2025.

I'm embarking on a personal journey of self-discovery. Project Purple is an effort to create a a nice social forum that hearkens back to websites like Xanga, LiveJournal, and Myspace, for the asexual and aromantic community.

This project will require a lot of the skills I've developed over the past few years as a Software QA Engineer, along with the technical knowledge I have on Software Develop. It will also challenge me to create a front-end application using a modern library like React, instead of just templates.

I began the Purple Project by outlining what I want the website to process from a data perspective. I've established that, for now, I'd like to get the basics worked out before growing with additional features. I created three models:

1. Profile
2. Post
3. Comment

These models contain the basic information I'd like to elaborate on as I create the site. 

One of the things that I've had to learn is how Django Rest Framework works. I quickly learned that there's a difference between how regular Django and the DRF work. I find the DRF to be slightly quicker because you can make all your models under the api folder, instead of having to create a new project/app with Django.

It's been great revisiting Django after all these years. Their documentation remains undefeated.

[I found their documentation on the fields for their models very helpful](https://docs.djangoproject.com/en/5.2/ref/models/fields/#django.db.models.DateTimeField)

While I've spent a lot of time creating automation libraries using languages like Java, and reviewing code for things like Spring and Spring-Boot, there's something very primal about Django. I've always loved the batteries included philosophy behind it.

Below is an example of the different fields I've established for the Profile model to have. I've included things like `background_color` because the plan is to allow users to have some form of customization to their website, like Myspace or Xanga back in the day.

`class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, 
                                on_delete=models.CASCADE) 
    
    sexual_orientation = models.CharField(max_length=50, blank=True, null=True)
    aro_spec_identity = models.CharField(max_length=50, blank=True, null=True)
    ace_spec_identity = models.CharField(max_length=50, blank=True, null=True)
    pronouns = models.CharField(max_length=20, blank=True, null=True)
    relationship_style = models.CharField(max_length=50, blank=True, null=True)

    background_color = models.CharField(max_length=7, default='#FFFFFF')
    accent_color = models.CharField(max_length=7, default='#000000')
    identity_block_text = models.TextField(blank=True)

    bio = models.TextField()
    birthdate = models.DateField(null=True, blank=True)
`

## Final Thoughts
I'm proud of my progress so far. I feel like I've done a lot today, but as the days go on, I'm sure my progress will be slower due to the amount of other areas of DRF I'll have to spend to pouring over in their documentation. 

I plan to spend a lot of time in the backend, and even more time in the frontend. I have little to know experience with React, but have had a rotation of Youtube videos playing in the background. I understand why it's such an appealing library.

I'll keep updating these logs everytime with progress, problems, and frustrations, until this project sees a beta release in about 6 months time. 
