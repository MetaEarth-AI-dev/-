// scripts/deploy_staking.js

async function main() {
    const [deployer] = await ethers.getSigners();

    console.log("Deploying the MetaEarthStaking contract with the account:", deployer.address);

    const tokenAddress = "YOUR_TOKEN_CONTRACT_ADDRESS"; // Replace with the deployed token contract address
    const rewardRate = ethers.utils.parseEther("0.1"); // Reward rate

    const Staking = await ethers.getContractFactory("MetaEarthStaking");
    const staking = await Staking.deploy(tokenAddress, rewardRate);

    await staking.deployed();

    console.log("MetaEarthStaking deployed to:", staking.address);
}

// Run the script and handle errors
main()
    .then(() => process.exit(0))
    .catch((error) => {
        console.error(error);
        process.exit(1);
    });
