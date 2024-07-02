echo "🐳 Build docker image…"
docker build -t requester .
echo "Docker image built successfully!\n\n"

echo "⏯️ Running docker image…"
docker run --rm -it requester