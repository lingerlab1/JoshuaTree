sudo sh -c 'echo "deb [arch=amd64] http://apt.postgresql.org/pub/repos/apt focal-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
sudo sh -c "echo 'deb https://packagecloud.io/timescale/timescaledb/ubuntu/ focal main' > /etc/apt/sources.list.d/timescaledb.list"
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
wget --quiet -O - https://packagecloud.io/timescale/timescaledb/gpgkey | sudo apt-key add -

sudo apt update
sudo apt -y install postgresql
sudo apt -y install timescaledb-2-postgresql-14

