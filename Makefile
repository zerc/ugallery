heroku-install:
	heroku create
	git push heroku master
	heroku ps:scale web=1
	heroku open
