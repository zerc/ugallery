# uGallery

Is a simple gallery example based on [Uploadcare](https://uploadcare.com/)  (these good comrades will take care of all of your precious files), [Django](https://www.djangoproject.com/), [Bootstrap](http://getbootstrap.com/) and [Fotorama](http://fotorama.io).


## Easiest way to deploy it

Of course you can deploy it anywhere  because it is a simple django's project. But easiest way to deploy it is using [Heroku](https://www.heroku.com/).

First you'll need an account (it's free), heroku's [toolbelt](https://devcenter.heroku.com/articles/quickstart#step-2-install-the-heroku-toolbelt) and some terminal-like stuff.

After that execute next commands in your terminal:

```shell
$ git clone git@github.com:zerc/ugallery.git
$ cd ugallery
$ make heroku-install
```

### Setup GitHub application

Project uses authorization based on GitHub accounts. To make it work needed:

1. Create own GitHub application [here](https://github.com/settings/applications/new)

2. Configure system variables:

```
$ heroku config:add GITHUB_APP_ID='Your_Application_Client ID'
$ heroku config:add GITHUB_API_SECRET='Your_Application_Client_Secret'
```

### Storage

uGallery uses [Uploadcare](https://uploadcare.com/) to store files — its demo account by default:

* all files are stored for one day, and **DELETED** after.

If you want a persistent storage, get the Uploadcare
[subscription](https://uploadcare.com/accounts/create/) and set obtained keys:

```term
heroku config:set UPLOADCARE_PUBLIC_KEY='MY_PUBLIC_KEY'
heroku config:set UPLOADCARE_SECRET_KEY='MY_SECRET_KEY'
```
