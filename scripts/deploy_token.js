// scripts/deploy_token.js

async function main() {
    const [deployer] = await ethers.getSigners();

    console.log("Deploying the MetaEarthToken contract with the account:", deployer.address);

    const Token = await ethers.getContractFactory("MetaEarthToken");
    const token = await Token.deploy();

    await token.deployed();

    console.log("MetaEarthToken deployed to:", token.address);
}

// Run the script and handle errors
main()
    .then(() => process.exit(0))
    .catch((error) => {
        console.error(error);
        process.exit(1);
    });
