const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("MetaEarthDAO", function () {
  let Token, token, DAO, dao, owner, addr1, addr2, addr3;

  beforeEach(async function () {
    // Deploy the token contract
    Token = await ethers.getContractFactory("MetaEarthToken");
    token = await Token.deploy();
    await token.deployed();

    // Deploy the DAO contract
    DAO = await ethers.getContractFactory("MetaEarthDAO");
    dao = await DAO.deploy(token.address, 3600); // 1-hour voting period
    await dao.deployed();

    // Distribute tokens to addr1, addr2, and addr3 for voting
    [owner, addr1, addr2, addr3] = await ethers.getSigners();
    await token.transfer(addr1.address, ethers.utils.parseEther("100"));
    await token.transfer(addr2.address, ethers.utils.parseEther("200"));
    await token.transfer(addr3.address, ethers.utils.parseEther("300"));

    // Approve DAO contract to spend tokens for voting
    await token.connect(addr1).approve(dao.address, ethers.utils.parseEther("100"));
    await token.connect(addr2).approve(dao.address, ethers.utils.parseEther("200"));
    await token.connect(addr3).approve(dao.address, ethers.utils.parseEther("300"));
  });

  it("Should allow users to create proposals", async function () {
    await dao.connect(addr1).createProposal("Increase staking rewards");
    const proposal = await dao.proposals(0);

    expect(proposal.id).to.equal(0);
    expect(proposal.description).to.equal("Increase staking rewards");
    expect(proposal.proposer).to.equal(addr1.address);
    expect(proposal.executed).to.be.false;
  });

  it("Should allow users to vote on proposals", async function () {
    await dao.connect(addr1).createProposal("Increase staking rewards");

    // addr2 votes in favor
    await dao.connect(addr2).vote(0, true);

    const proposal = await dao.proposals(0);
    expect(proposal.votesFor).to.equal(ethers.utils.parseEther("200"));
    expect(proposal.votesAgainst).to.equal(0);

    // addr3 votes against
    await dao.connect(addr3).vote(0, false);

    const updatedProposal = await dao.proposals(0);
    expect(updatedProposal.votesFor).to.equal(ethers.utils.parseEther("200"));
    expect(updatedProposal.votesAgainst).to.equal(ethers.utils.parseEther("300"));
  });

  it("Should prevent double voting by the same user", async function () {
    await dao.connect(addr1).createProposal("Increase staking rewards");

    await dao.connect(addr2).vote(0, true);
    await expect(dao.connect(addr2).vote(0, true)).to.be.revertedWith("You have already voted on this proposal");
  });

  it("Should not allow voting after the voting period ends", async function () {
    await dao.connect(addr1).createProposal("Increase staking rewards");

    // Advance time beyond the voting period
    await ethers.provider.send("evm_increaseTime", [3600]);
    await ethers.provider.send("evm_mine");

    await expect(dao.connect(addr2).vote(0, true)).to.be.revertedWith("Voting period has ended");
  });

  it("Should execute a proposal if votes in favor exceed votes against", async function () {
    await dao.connect(addr1).createProposal("Increase staking rewards");

    // addr2 votes in favor
    await dao.connect(addr2).vote(0, true);
    // addr3 votes against
    await dao.connect(addr3).vote(0, false);

    // Advance time beyond the voting period
    await ethers.provider.send("evm_increaseTime", [3600]);
    await ethers.provider.send("evm_mine");

    // Execute the proposal
    await dao.connect(owner).executeProposal(0);

    const proposal = await dao.proposals(0);
    expect(proposal.executed).to.be.true;
  });

  it("Should not execute a proposal if votes against exceed votes in favor", async function () {
    await dao.connect(addr1).createProposal("Decrease staking rewards");

    // addr2 and addr3 vote against
    await dao.connect(addr2).vote(0, false);
    await dao.connect(addr3).vote(0, false);

    // Advance time beyond the voting period
    await ethers.provider.send("evm_increaseTime", [3600]);
    await ethers.provider.send("evm_mine");

    // Attempt to execute the proposal
    await dao.connect(owner).executeProposal(0);

    const proposal = await dao.proposals(0);
    expect(proposal.executed).to.be.false;
  });
});
