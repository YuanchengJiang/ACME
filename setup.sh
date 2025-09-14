docker run -dit --name questdb -p 9000:9000 -p 8812:8812 questdb/questdb:nightly
docker run --name postgres -e POSTGRES_PASSWORD=12344321 -p 5432:5432 -dit postgres:14.0
source pyenv/bin/activate
