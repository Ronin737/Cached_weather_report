The application has been developed using django-framework with redis-cache.

Based on the station code provided to the URL, it will fetch the METAR report from the given URL and display the data in JSON format.

The data is cached using Redis, unless the nocache parameter is specified, in which case, only live data is loaded.

The valid URLs are defined in Report.urls.py. The URLs point towards class-based views which have been defined by  inheriting django's View class.

No data is stored locally, unless its cached.

Use runserver command to start the server locally on the default port. Provide one of the valid URLs for getting JSON display.

All dependencies have been specified in requirements.txt.

