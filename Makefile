heroku-install:
	heroku create
	git push heroku master
	heroku ps:scale web=1
	heroku open

heroku-deploy:
	git push heroku master
