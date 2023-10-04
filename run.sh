
set -e

for compose in "docker-compose" "docker compose"
do 
    export COMPOSE=$compose
    $compose up
done


