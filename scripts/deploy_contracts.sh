#!/bin/bash

echo "Deploying MetaEarth contracts..."

# Compile the contracts
npx hardhat compile

# Deploy the token contract
echo "Deploying Token Contract..."
TOKEN_ADDRESS=$(npx hardhat run scripts/deploy_token.js --network localhost)
echo "Token Contract deployed at: $TOKEN_ADDRESS"

# Deploy the staking contract
echo "Deploying Staking Contract..."
STAKING_ADDRESS=$(npx hardhat run scripts/deploy_staking.js --network localhost)
echo "Staking Contract deployed at: $STAKING_ADDRESS"

# Deploy the DAO contract
echo "Deploying DAO Contract..."
DAO_ADDRESS=$(npx hardhat run scripts/deploy_dao.js --network localhost)
echo "DAO Contract deployed at: $DAO_ADDRESS"

echo "All contracts deployed successfully!"
