.PHONY: init plan apply destroy

ENV ?= dev

init:
	cd environments/$(ENV) && terraform init

plan:
	cd environments/$(ENV) && terraform plan

apply:
	cd environments/$(ENV) && terraform apply -auto-approve

destroy:
	cd environments/$(ENV) && terraform destroy -auto-approve
