IMAGE="pipes-example:v1"

# Build docker image
docker build -t $IMAGE . || exit 1

# Load the image
minikube image load $IMAGE
