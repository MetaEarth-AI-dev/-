// scripts/deploy_dao.js

async function main() {
    const [deployer] = await ethers.getSigners();

    console.log("Deploying the MetaEarthDAO contract with the account:", deployer.address);

    const tokenAddress = "YOUR_TOKEN_CONTRACT_ADDRESS"; // Replace with the deployed token contract address
    const votingPeriod = 3600; // 1-hour voting period in seconds

    const DAO = await ethers.getContractFactory("MetaEarthDAO");
    const dao = await DAO.deploy(tokenAddress, votingPeriod);

    await dao.deployed();

    console.log("MetaEarthDAO deployed to:", dao.address);
}

// Run the script and handle errors
main()
    .then(() => process.exit(0))
    .catch((error) => {
        console.error(error);
        process.exit(1);
    });
