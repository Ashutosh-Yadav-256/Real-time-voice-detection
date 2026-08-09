.PHONY: test-ml test-services lint deploy

test-ml:
	$(MAKE) -C ml test

test-services:
	$(MAKE) -C services test

lint:
	$(MAKE) -C ml lint
	$(MAKE) -C services lint

deploy:
	$(MAKE) -C infra apply
	helm upgrade --install voice-detector helm/voice-detector
