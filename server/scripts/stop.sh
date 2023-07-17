#!/bin/bash


set -e

lsof -i:7080 |  awk '{print $2}' | tail -n -1 | xargs kill -9