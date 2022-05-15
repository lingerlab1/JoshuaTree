#sudo sh -c 'echo "deb [arch=amd64] http://apt.postgresql.org/pub/repos/apt focal-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
#sudo sh -c "echo 'deb https://packagecloud.io/timescale/timescaledb/ubuntu/ focal main' > /etc/apt/sources.list.d/timescaledb.list"
#wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
#wget --quiet -O - https://packagecloud.io/timescale/timescaledb/gpgkey | sudo apt-key add -

#sudo apt update
#sudo apt -y install postgresql
#sudo apt -y install timescaledb-2-postgresql-14

docker run -d --name timescaledb --user $(id -u):$(id -g) -p 5432:5432 \
-v $HOME/data:/var/lib/postgresql/data \
-e POSTGRES_PASSWORD=password timescale/timescaledb-ha:pg14-latest

docker exec -i -t timescaledb /bin/bash
