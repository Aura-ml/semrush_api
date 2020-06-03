# semrush_api

buid app
```
docker build -t app
docker run  -p 127.0.0.1:5000:5000 app
```

app request
```
. http://localhost:5000/StartingNewProjetFlask/<querystring>/<payload>
. http://localhost:5000/ActiverAudit/<querystring>/<payload>/<id_projet>
. http://localhost:5000/ExecuterAuditFlask/<querystring>/<id_projet>
. http://localhost:5000/ObtenirRapportFlask/<querystring>/<id_projet>
```
