printf "\n*************RUNNING SHELL SCRIPT*************\n"
# RUN chmod +x start.sh && ./start.sh

# Build the Docker image
docker build -t onadebi/courses .

# Run the container based on the image
docker run -d --name courseslocal -p 5000:5000 onadebi/courses

# Start the container
docker start courseslocal

# gunicorn -b 0.0.0.0:5000 main:app
printf "\n*************END OF SHELL RUN**************\n"


