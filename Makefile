# Makefile – CTF Hackaton (build + run)

IMAGE := ctf-hackaton
TAG := latest
CONTAINER := ctf_hackaton_ctf
DOCKERFILE := Dockerfile
CONTEXT := .

PORTS := \
	-p 2222:2222 \
	-p 30000:30000 \
	-p 30001:30001 \
	-p 31000-32000:31000-32000

.PHONY: docker clean_container

## docker : Rebuild l’image, supprime le conteneur existant et relance un propre
docker: clean_container
	docker build -t $(IMAGE):$(TAG) -f $(DOCKERFILE) $(CONTEXT)
	docker run --name $(CONTAINER) -dit $(PORTS) $(IMAGE):$(TAG)

## clean_container : Stoppe et supprime le conteneur s’il existe
clean_container:
	@if [ $$(docker ps -aq -f name=$(CONTAINER)) ]; then \
		echo "🗑️  Suppression de l’ancien conteneur $(CONTAINER)"; \
		docker rm -f $(CONTAINER); \
	fi
