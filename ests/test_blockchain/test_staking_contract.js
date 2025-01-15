const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("MetaEarthStaking", function () {
  let Token, token, Staking, staking, owner, addr1, addr2;

  beforeEach(async function () {
    // Deploy the token contract
    Token = await ethers.getContractFactory("MetaEarthToken");
    token = await Token.deploy();
    await token.deployed();

    // Deploy the staking contract
    Staking = await ethers.getContractFactory("MetaEarthStaking");
    staking = await Staking.deploy(token.address, ethers.utils.parseEther("0.1")); // Reward rate: 0.1 tokens per second per staked token
    await staking.deployed();

    // Distribute some tokens to addr1 and addr2 for staking
    [owner, addr1, addr2] = await ethers.getSigners();
    await token.transfer(addr1.address, ethers.utils.parseEther("1000"));
    await token.transfer(addr2.address, ethers.utils.parseEther("1000"));

    // Approve the staking contract to spend tokens on behalf of addr1 and addr2
    await token.connect(addr1).approve(staking.address, ethers.utils.parseEther("1000"));
    await token.connect(addr2).approve(staking.address, ethers.utils.parseEther("1000"));
  });

  it("Should allow users to stake tokens", async function () {
    await staking.connect(addr1).stake(ethers.utils.parseEther("100"));
    const stakedAmount = await staking.stakers(addr1.address);
    expect(stakedAmount.stakedAmount).to.equal(ethers.utils.parseEther("100"));
  });

  it("Should calculate rewards correctly over time", async function () {
    await staking.connect(addr1).stake(ethers.utils.parseEther("100"));

    // Advance time by 10 seconds
    await ethers.provider.send("evm_increaseTime", [10]);
    await ethers.provider.send("evm_mine");

    const staker = await staking.stakers(addr1.address);
    expect(staker.rewardDebt).to.be.closeTo(ethers.utils.parseEther("1"), ethers.utils.parseEther("0.1")); // 100 tokens staked * 0.1 reward rate * 10 seconds
  });

  it("Should allow users to claim rewards", async function () {
    await staking.connect(addr1).stake(ethers.utils.parseEther("100"));

    // Advance time by 10 seconds
    await ethers.provider.send("evm_increaseTime", [10]);
    await ethers.provider.send("evm_mine");

    await staking.connect(addr1).claimRewards();
    const balance = await token.balanceOf(addr1.address);
    expect(balance).to.be.closeTo(ethers.utils.parseEther("901"), ethers.utils.parseEther("0.1")); // Original balance - staked amount + rewards
  });

  it("Should allow users to unstake tokens", async function () {
    await staking.connect(addr1).stake(ethers.utils.parseEther("100"));

    // Advance time by 10 seconds
    await ethers.provider.send("evm_increaseTime", [10]);
    await ethers.provider.send("evm_mine");

    await staking.connect(addr1).unstake(ethers.utils.parseEther("50"));
    const staker = await staking.stakers(addr1.address);
    expect(staker.stakedAmount).to.equal(ethers.utils.parseEther("50"));
  });

  it("Should not allow unstaking more than staked amount", async function () {
    await staking.connect(addr1).stake(ethers.utils.parseEther("100"));

    await expect(
      staking.connect(addr1).unstake(ethers.utils.parseEther("200"))
    ).to.be.revertedWith("Insufficient staked amount");
  });

  it("Should update total staked correctly", async function () {
    await staking.connect(addr1).stake(ethers.utils.parseEther("100"));
    await staking.connect(addr2).stake(ethers.utils.parseEther("200"));

    const totalStaked = await staking.totalStaked();
    expect(totalStaked).to.equal(ethers.utils.parseEther("300"));
  });
});
