const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("MetaEarthToken", function () {
  let Token, token, owner, addr1, addr2;

  beforeEach(async function () {
    // Deploy the token contract
    Token = await ethers.getContractFactory("MetaEarthToken");
    [owner, addr1, addr2] = await ethers.getSigners();
    token = await Token.deploy();
    await token.deployed();
  });

  it("Should assign the total supply of tokens to the owner", async function () {
    const ownerBalance = await token.balanceOf(owner.address);
    const totalSupply = await token.totalSupply();
    expect(ownerBalance).to.equal(totalSupply);
  });

  it("Should allow tokens to be transferred between accounts", async function () {
    // Transfer 100 tokens from owner to addr1
    await token.transfer(addr1.address, 100);
    const addr1Balance = await token.balanceOf(addr1.address);
    expect(addr1Balance).to.equal(100);

    // Transfer 50 tokens from addr1 to addr2
    await token.connect(addr1).transfer(addr2.address, 50);
    const addr2Balance = await token.balanceOf(addr2.address);
    expect(addr2Balance).to.equal(50);
  });

  it("Should allow the owner to mint new tokens", async function () {
    // Mint 1000 new tokens to addr1
    await token.mint(addr1.address, 1000);
    const addr1Balance = await token.balanceOf(addr1.address);
    expect(addr1Balance).to.equal(1000);
  });

  it("Should allow the owner to burn tokens", async function () {
    // Burn 500 tokens from owner
    const initialOwnerBalance = await token.balanceOf(owner.address);
    await token.burn(owner.address, 500);
    const finalOwnerBalance = await token.balanceOf(owner.address);
    expect(finalOwnerBalance).to.equal(initialOwnerBalance.sub(500));
  });

  it("Should not allow non-owners to mint or burn tokens", async function () {
    await expect(token.connect(addr1).mint(addr1.address, 1000)).to.be.revertedWith("Ownable: caller is not the owner");
    await expect(token.connect(addr1).burn(addr1.address, 1000)).to.be.revertedWith("Ownable: caller is not the owner");
  });
});
