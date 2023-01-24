#!/bin/bash

#Creates a new project
gcloud projects create adsgproject

#Shows all the project in the cloud
gcloud projects list

#Sets the new project
gcloud config set project adsgproject