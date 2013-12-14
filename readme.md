Learning Dokku
==============

This repository is being used as a simple project to deploy to [Dokku](https://github.com/progrium/dokku) or any provider that will deploy a Procfile based environment, like Heroku.

Why not use the nodejs app in the Dokku readme? Because.

Things to test out
------------------

- [x] Deploy this repo as a Dokku app
- [x] Dokku Postgres Plugin
- [ ] Running DB Migrations on Deploy
- [ ] Running Procfile workers (multiple processes)

Deploy this repo as a Dokku app
-------------------------------

Dokku setup is outside the scope of this walkthrough. There are many guides online.

Once Dokku is setup, you should be able to run these commands on your local machine (the one from which you pushed the public key to Dokku):

```bash
$ git clone https://github.com/sherzberg/learning-dokku.git
$ git remote add apps $DOMAIN:learning-dokku
$ git push apps master
```

If these commands were successful, you should be able to navigate to http://$DOMAIN:learning-dokku in your browser.

Dokku Postgres Plugin
---------------------

This walkthrough uses the [posgresql](https://github.com/Kloadut/dokku-pg-plugin) dokku plugin.

To setup the plugin, run these commands on the **__dokku__** host:

```bash
$ cd /var/lib/dokku/plugins
$ git clone https://github.com/Kloadut/dokku-pg-plugin postgresql
$ dokku plugins-install
$ dokku help
```

This will spew a bunch of logs about building and tagging a dockker instance. If you see a command that starts with _postgresql_, the plugin is successfully installed.

Now create a linked database for the _learning-dokku_ app we setup earlier (from the **__dokku__** host):

```bash
$ dokku postgresql:create learning-dokku
```

This command runs a postgresql instance on the Dokku host machine and sets will automatically set an environment variable DATABASE_URL for the _learning-dokku_ app. The simple Django app in this repo is already setup to accept this environment variable so lets push the change from your **__local machine__**:

```bash
$ git push apps master
```

The console should spit out some information about pushing the code to _apps_ and linking the database.

License
=======

MIT. See LICENSE file.
