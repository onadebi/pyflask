printf "\n*************STOPPING CONTAINER SCRIPT*************\n"


printf "\n>>STOP CONTAINER: courseslocal\n"
docker container stop courseslocal

printf "\n>>DESTROY CONTAINER: courseslocal\n"
docker container rm courseslocal

printf "\n>>DESTROY IMAGE: onadebi/courses\n"
docker image rm onadebi/courses