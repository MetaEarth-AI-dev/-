#!/bin/bash

echo "Starting deployment of MetaEarth contracts..."

# Compile contracts
echo "Compiling contracts..."
npx hardhat compile

# Deploy Token Contract
echo "Deploying MetaEarthToken..."
TOKEN_ADDRESS=$(npx hardhat run scripts/deploy_token.js --network localhost | grep "MetaEarthToken deployed to" | awk '{print $NF}')
echo "MetaEarthToken deployed at: $TOKEN_ADDRESS"

# Deploy Staking Contract
echo "Deploying MetaEarthStaking..."
STAKING_ADDRESS=$(npx hardhat run scripts/deploy_staking.js --network localhost | grep "MetaEarthStaking deployed to" | awk '{print $NF}')
echo "MetaEarthStaking deployed at: $STAKING_ADDRESS"

# Deploy DAO Contract
echo "Deploying MetaEarthDAO..."
DAO_ADDRESS=$(npx hardhat run scripts/deploy_dao.js --network localhost | grep "MetaEarthDAO deployed to" | awk '{print $NF}')
echo "MetaEarthDAO deployed at: $DAO_ADDRESS"

echo ""
echo "Deployment Summary:"
echo "--------------------"
echo "Token Contract Address: $TOKEN_ADDRESS"
echo "Staking Contract Address: $STAKING_ADDRESS"
echo "DAO Contract Address: $DAO_ADDRESS"
echo ""
echo "All contracts deployed successfully!"
