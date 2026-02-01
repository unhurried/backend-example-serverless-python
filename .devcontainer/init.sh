#!/usr/bin/env bash
set -e

echo "Installing AWS CDK CLI..."
npm install -g aws-cdk@latest

echo "Installing AWS SAM CLI..."
wget -q https://github.com/aws/aws-sam-cli/releases/latest/download/aws-sam-cli-linux-x86_64.zip -O aws-sam-cli-linux-x86_64.zip
unzip -q aws-sam-cli-linux-x86_64.zip -d sam-installation
sudo ./sam-installation/install
rm -f aws-sam-cli-linux-x86_64.zip
rm -rf ./sam-installation

echo "All development tools installed successfully!"
