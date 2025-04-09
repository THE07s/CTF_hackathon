# Makefile – CTF hackathon (build + run)

IMAGE := ctf-hackathon
TAG := latest
CONTAINER := ctf_hackathon_ctf
DOCKERFILE := Dockerfile
CONTEXT := .

PORTS := \
    -p 2222:2222 \
    -p 30000:30000 \
    -p 30001:30001 \
    -p 31000-32000:31000-32000

.PHONY: docker clean_container

## docker : Rebuild l’image, lance un nouveau conteneur et supprime l’ancien en arrière-plan
docker: clean_container
    docker build -t $(IMAGE):$(TAG) -f $(DOCKERFILE) $(CONTEXT)
    @echo "▶️  Lancement du nouveau conteneur avec le nom temporaire $(CONTAINER)_new..."
    docker run --name $(CONTAINER)_new -dit $(PORTS) $(IMAGE):$(TAG)
    @echo "🗑️  Suppression de l’ancien conteneur $(CONTAINER) en arrière-plan..."
    ( docker rm -f $(CONTAINER) >/dev/null 2>&1 ) &
    @echo "🔄  Renommage du conteneur temporaire..."
    docker rename $(CONTAINER)_new $(CONTAINER)

## clean_container : Stoppe et supprime l’ancien conteneur s’il existe
clean_container:
    @if [ $$(docker ps -aq -f name=$(CONTAINER)) ]; then \
        echo "🗑️  Un conteneur existant $(CONTAINER) sera supprimé en arrière-plan..."; \
    fi
